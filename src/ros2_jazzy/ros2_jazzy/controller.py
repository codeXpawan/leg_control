#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import Imu
from sensor_msgs.msg import JointState
from pid_tune.msg import PidTune
from ament_index_python.packages import get_package_share_directory
from tf_transformations import euler_from_quaternion

import numpy as np
import pickle
import os


class JointCmds:
    def __init__(self, node: Node, joints, path):
        self.jnt_cmd_dict = {}
        self.joints_list = joints
        self.t = 0.0
        self.path = path + '/data/'

        self.osl_knee_pose = 0.0
        self.osl_ankle_pose = 0.0

        self.setpoint_knee = 0.0
        self.error_knee = 0.0
        self.errord_knee = 0.0
        self.errori_knee = 0.0
        self.preverror_knee = 0.0

        self.setpoint_ankle = 0.0
        self.error_ankle = 0.0
        self.errord_ankle = 0.0
        self.errori_ankle = 0.0
        self.preverror_ankle = 0.0

        self.kp_knee = 300 * 0.01
        self.ki_knee = 0 * 0.01
        self.kd_knee = 30 * 0.01

        self.kp_ankle = 300 * 0.01
        self.ki_ankle = 0 * 0.01
        self.kd_ankle = 30 * 0.01

        # Clamping parameters
        self.max_errori = 0.5    # rad-sec (integrator limit)
        self.max_voltage = 10.0  # Nominal voltage

        # self.js_sub = node.create_subscription(JointState, '/joint_states', self.joint_state_cb, 10)
        self.knee_imu_sub = node.create_subscription(Imu, '/imu/osl_shank', self.imu_shank_cb, 10)
        self.ankle_imu_sub = node.create_subscription(Imu, '/imu/foot', self.imu_foot_cb, 10)
        self.pid_knee_sub = node.create_subscription(PidTune, '/oslsim/osl_knee/pid', self.osl_knee_pid_cb, 10)
        self.pid_ankle_sub = node.create_subscription(PidTune, '/oslsim/osl_ankle/pid', self.osl_ankle_pid_cb, 10)
        self.pub = node.create_publisher(Float64MultiArray, '/controller_debug', 10)

    def osl_knee_pid_cb(self,data):
        self.kp_knee=float(data.kp)*0.01
        self.kd_knee=float(data.kd)*0.01
        self.ki_knee=float(data.ki)*0.01
        
    def osl_ankle_pid_cb(self,data):
        self.kp_ankle=float(data.kp)*0.01
        self.kd_ankle=float(data.kd)*0.01
        self.ki_ankle=float(data.ki)*0.01

    def imu_shank_cb(self, data):
        temp = [data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w]
        # print(f'Knee IMU - Quaternion: {temp}')
        (roll, pitch, yaw) = euler_from_quaternion(temp)
        # print(f'Knee IMU - Roll: {roll:.4f}, Pitch: {pitch:.4f}, Yaw: {yaw:.4f}')
        self.osl_knee_pose = 0

    def imu_foot_cb(self, data):
        temp = [data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w]
        # print(f'Ankle IMU - Quaternion: {temp}')
        (roll, pitch, yaw) = euler_from_quaternion(temp)
        # print(f'Ankle IMU - Roll: {roll:.4f}, Pitch: {pitch:.4f}, Yaw: {yaw:.4f}')
        self.osl_ankle_pose = 0
    

    # def joint_state_cb(self, msg):
    #     if 'osl_knee' in msg.name:
    #         idx = msg.name.index('osl_knee')
    #         self.osl_knee_pose = msg.position[idx]

    #     if 'osl_ankle' in msg.name:
    #         idx = msg.name.index('osl_ankle')
    #         self.osl_ankle_pose = msg.position[idx]

    def update(self, dt):
        with open(self.path + 'angles.pkl', 'rb') as f:
            angles = pickle.load(f)

        # -------------------------------------- #
       
        raw_knee = list(angles['angle_knee'].values())
        raw_ankle = list(angles['angle_ankle'].values())

        n = -15
        angle_knee = raw_knee[n:]
        angle_knee.extend(raw_knee[:n])

        angle_ankle = raw_ankle[n:]
        angle_ankle.extend(raw_ankle[:n])

        self.setpoint_knee = -0.0174533 * angle_knee[int((self.t * 10) % 100)]
        self.setpoint_ankle = 0.0174533 * angle_ankle[int((self.t * 10) % 100)]

        self.pub.publish(Float64MultiArray(data=[self.setpoint_knee, self.osl_knee_pose, self.setpoint_ankle, self.osl_ankle_pose]))

        self.error_knee = self.setpoint_knee - self.osl_knee_pose
        self.errord_knee = (self.error_knee - self.preverror_knee) / dt
        self.errori_knee += self.error_knee * dt

        self.error_ankle = self.setpoint_ankle - self.osl_ankle_pose
        self.errord_ankle = (self.error_ankle - self.preverror_ankle) / dt
        self.errori_ankle += self.error_ankle * dt

        # Integrator Anti-Windup (Clamping)
        self.errori_knee = np.clip(self.errori_knee, -self.max_errori, self.max_errori)
        self.errori_ankle = np.clip(self.errori_ankle, -self.max_errori, self.max_errori)

        # -------------------------------------- #

        v_ankle = (self.kp_ankle*self.error_ankle) + (self.kd_ankle*self.errord_ankle) + (self.ki_ankle*self.errori_ankle)
        v_knee = (self.kp_knee*self.error_knee) + (self.kd_knee*self.errord_knee) + (self.ki_knee*self.errori_knee)

        # Output Voltage Clamping
        self.jnt_cmd_dict['osl_ankle'] = np.clip(v_ankle, -self.max_voltage, self.max_voltage) * -0.3424183
        self.jnt_cmd_dict['osl_knee'] = np.clip(v_knee, -self.max_voltage, self.max_voltage) * 0.327 

        # -------------------------------------- #

        self.preverror_knee = self.error_knee
        self.preverror_ankle = self.error_ankle
        self.t += dt
        return self.jnt_cmd_dict

class Controller(Node):
    def __init__(self, joints, hz):
        super().__init__('oslsim_controller')

        self.joints = joints
        self.dt = 1.0 / hz

        pkg_path = get_package_share_directory('ros2_jazzy')

        self.joints_publishers = {}
        for j in joints:
            self.joints_publishers[j] = self.create_publisher(
                Float64MultiArray,
                f'/{j}_controller/commands',
                10
            )

        self.jntcmds = JointCmds(self, joints, pkg_path)

        self.create_timer(self.dt, self.control_loop)

    def control_loop(self):
        jnt_cmd_dict = self.jntcmds.update(self.dt)
        for j, val in jnt_cmd_dict.items():
            msg = Float64MultiArray()
            msg.data = [float(val)]
            self.joints_publishers[j].publish(msg)

        # Throttled logging — every 1 second
        # self.get_logger().info(
        #     f"KNEE: SP={self.jntcmds.setpoint_knee:.3f}, Pose={self.jntcmds.osl_knee_pose:.3f}, V={jnt_cmd_dict['osl_knee']:.3f} | "
        #     f"ANKLE: SP={self.jntcmds.setpoint_ankle:.3f}, Pose={self.jntcmds.osl_ankle_pose:.3f}, V={jnt_cmd_dict['osl_ankle']:.3f}",
        #     throttle_duration_sec=1.0
        # )

def main():
    rclpy.init()
    joints = ['osl_knee', 'osl_ankle']
    node = Controller(joints=joints, hz=10)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
