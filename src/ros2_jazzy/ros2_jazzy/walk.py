#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from ament_index_python.packages import get_package_share_directory
import pickle

class JointCmds:
    def __init__(self, joints, path):
        self.jnt_cmd_dict = {}
        self.joints_list = joints
        self.t = 0
        self.path = path + '/data/'
        
        try:
            with open(self.path + 'angles.pkl', 'rb') as f:
                self.angles = pickle.load(f)
            print(f"Loaded angles successfully. Keys: {self.angles.keys()}")
            print(f"Thigh angles length: {len(self.angles['angle_thigh'])}")
            print(f"Ankle angles length: {len(self.angles['angle_ankle'])}")
            print(f"Knee angles length: {len(self.angles['angle_knee'])}")
        except Exception as e:
            print(f"Error loading angles: {e}")
            self.angles = None
    
    def update(self, dt):
        if self.angles is None:
            print("No angle data loaded!")
            return self.jnt_cmd_dict
        
        current_idx = self.t % 100
        sign = 1.0 if current_idx <= 50 else -1.0
        opposite_idx = int((50 + sign * current_idx) % 100)
        
        # Update joint commands
        self.jnt_cmd_dict['osl_hip'] = 0.0174533 * self.angles['angle_thigh'][current_idx]
        self.jnt_cmd_dict['ankle'] = -0.0174533 * self.angles['angle_ankle'][opposite_idx]
        self.jnt_cmd_dict['hip'] = 0.0174533 * self.angles['angle_thigh'][opposite_idx]
        self.jnt_cmd_dict['knee'] = -0.0174533 * self.angles['angle_knee'][opposite_idx]
        
        self.t += dt
        return self.jnt_cmd_dict


class WalkerNode(Node):
    def __init__(self, joints, hz):
        super().__init__('oslsim_walker')
        cwd = get_package_share_directory('ros2_jazzy')
        self.jntcmds = JointCmds(joints=joints, path=cwd)
        self.pub = {}
        ns_str = '/oslsim/'
        cont_str = '_position_controller'
        
        for j in joints:
            self.pub[j] = self.create_publisher(Float64, ns_str + j + cont_str + '/command', 10)
        
        timer_period = 1.0 / hz
        self.timer = self.create_timer(timer_period, self.timer_callback)
    
    def timer_callback(self):
        jnt_cmd_dict = self.jntcmds.update(1)
        
        for jnt in jnt_cmd_dict.keys():
            msg = Float64()
            msg.data = jnt_cmd_dict[jnt]
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