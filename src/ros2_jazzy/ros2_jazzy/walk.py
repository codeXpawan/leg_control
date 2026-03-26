#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from ament_index_python.packages import get_package_share_directory
import pickle
class JointCmds:
    def __init__(self, node: Node, joints, path):
        self.jnt_cmd_dict = {}
        self.joints_list = joints
        self.t = 0.0
        self.path = path + '/data/'
        self.node = node

    def update(self, dt):
        sign = 1.0

        if self.t%100 > 50:
            sign = -1.0

        with open(self.path + 'angles.pkl', 'rb') as f:
            angles = pickle.load(f)

        # -------------------------------------- #

        self.jnt_cmd_dict['osl_hip'] = 0.0174533 * angles['angle_thigh'][self.t%100]
        self.jnt_cmd_dict['ankle'] = -0.0174533 * (angles['angle_ankle'][abs(50 + sign * (self.t%100))])
        self.jnt_cmd_dict['hip'] = 0.0174533 * (angles['angle_thigh'][abs(50 + sign * (self.t%100))])
        self.jnt_cmd_dict['knee'] = -0.0174533 * (angles['angle_knee'][abs(50 + sign * (self.t%100))])
        # self.node.get_logger().info(f"Joint commands: {self.jnt_cmd_dict}")

        # -------------------------------------- #

        self.t += dt
        return self.jnt_cmd_dict


class WalkerNode(Node):
    def __init__(self, joints, hz):
        super().__init__('oslsim_walker')
        cwd = get_package_share_directory('ros2_jazzy')

        self.jntcmds = JointCmds(node=self, joints=joints, path=cwd)
        self.pub = {}
        ns_str = '/'
        cont_str = '_position_controller'

        for j in joints:
            self.pub[j] = self.create_publisher(Float64MultiArray, ns_str + j + cont_str + '/commands', 10)

        timer_period = 1.0 / hz
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        jnt_cmd_dict = self.jntcmds.update(1)
        for jnt in jnt_cmd_dict.keys():
            msg = Float64MultiArray()
            msg.data = [jnt_cmd_dict[jnt]]
            self.pub[jnt].publish(msg)


def main(args=None):
    rclpy.init(args=args)
    joints = ['hip', 'knee', 'ankle', 'osl_hip']
    hz = 10
    node = WalkerNode(joints, hz)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()