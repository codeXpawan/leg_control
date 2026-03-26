#!/usr/bin/env python
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import Imu
from pid_tune.msg import PidTune

from tf_transformations import euler_from_quaternion
from ament_index_python.packages import get_package_share_directory

import numpy as np
import pickle
import os


class JointCmds:
    def __init__(self, node: Node, joints, path):
        self.jnt_cmd_dict = {}
        self.joints_list = joints
        self.t = 0.0
        self.path = path + '/data/'
        

        self.osl_knee_pose = 0
        self.osl_ankle_pose = 0

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

        self.kp_knee = 250 * 0.1
        self.ki_knee = 30 * 0.1
        self.kd_knee = 1 * 0.1

        self.kp_ankle = 50 * 0.1
        self.ki_ankle = 0 * 0.1
        self.kd_ankle = 0 * 0.1

        self.node = node

        self.node.create_subscription(Imu, '/imu/osl_shank', self.osl_knee_pose_cb, 10)
        self.node.create_subscription(Imu, '/imu/foot', self.osl_ankle_pose_cb, 10)
        self.node.create_subscription(PidTune, '/oslsim/osl_knee/pid', self.osl_knee_pid_cb, 10)
        self.node.create_subscription(PidTune, '/oslsim/osl_ankle/pid', self.osl_ankle_pid_cb, 10)

    def osl_knee_pid_cb(self,data):
        self.kp_knee=float(data.kp)*0.1
        self.kd_knee=float(data.kd)*0.1
        self.ki_knee=float(data.ki)*0.1
        
    def osl_ankle_pid_cb(self,data):
        self.kp_ankle=float(data.kp)*0.1
        self.kd_ankle=float(data.kd)*0.1
        self.ki_ankle=float(data.ki)*0.1

    def osl_knee_pose_cb(self, data):
        temp = [data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w]
        # print(f'Knee IMU - Quaternion: {temp}')
        (roll, pitch, yaw) = euler_from_quaternion(temp)
        # print(f'Knee IMU - Roll: {roll:.4f}, Pitch: {pitch:.4f}, Yaw: {yaw:.4f}')
        self.osl_knee_pose = 1.0 * yaw        

    def osl_ankle_pose_cb(self, data):
        temp = [data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w]
        (roll, pitch, yaw) = euler_from_quaternion(temp)
        # print(f'Ankle IMU - Roll: {roll:.4f}, Pitch: {pitch:.4f}, Yaw: {yaw:.4f}')
        self.osl_ankle_pose = 1.0 * yaw

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

        self.setpoint_knee = -0.0174533 * angle_knee[int(self.t%100)]
        self.setpoint_ankle = 0.0174533 * angle_ankle[int(self.t%100)]

        self.node.get_logger().warn(f'Setpoints - Knee: {self.setpoint_knee:.4f}, Ankle: {self.setpoint_ankle:.4f}    Current - Knee: {self.osl_knee_pose:.4f}, Ankle: {self.osl_ankle_pose:.4f}')
        # print(f'Setpoints - Knee: {self.setpoint_knee:.4f}, Ankle: {self.setpoint_ankle:.4f}    Current - Knee: {self.osl_knee_pose:.4f}, Ankle: {self.osl_ankle_pose:.4f}')
        self.error_knee = self.setpoint_knee - self.osl_knee_pose
        self.errord_knee = self.error_knee - self.preverror_knee
        self.errori_knee += self.error_knee

        self.error_ankle = self.setpoint_ankle - self.osl_ankle_pose
        self.errord_ankle = self.error_ankle - self.preverror_ankle
        self.errori_ankle += self.error_ankle

        # -------------------------------------- #

        self.jnt_cmd_dict['osl_ankle'] = (self.kp_ankle*self.error_ankle) + (self.kd_ankle*self.errord_ankle) + (self.ki_ankle*self.errori_ankle)
        self.jnt_cmd_dict['osl_knee'] = (self.kp_knee*self.error_knee) + (self.kd_knee*self.errord_knee) + (self.ki_knee*self.errori_knee)
        # print(f'Commands - Knee: {self.jnt_cmd_dict["osl_knee"]:.4f}, Ankle: {self.jnt_cmd_dict["osl_ankle"]:.4f}')
        self.node.get_logger().warn(f'Commands - Knee: {self.jnt_cmd_dict["osl_knee"]:.4f}, Ankle: {self.jnt_cmd_dict["osl_ankle"]:.4f}')
        # -------------------------------------- #

        self.preverror_knee = self.error_knee
        self.preverror_ankle = self.error_ankle
        self.t += dt
        return self.jnt_cmd_dict

class Controller(Node):
    def __init__(self, joints, hz):
        super().__init__('oslsim_controller')
        self.get_logger().info('Controller node has started.')

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

