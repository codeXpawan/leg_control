#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from gazebo_msgs.msg import ContactsState

class Loadcell(Node):
    def __init__(self):
        super().__init__('loadcell')
        self.pub_fx = self.create_publisher(Float32, '/oslsim/loadcell_fx', 10)
        self.pub_fy = self.create_publisher(Float32, '/oslsim/loadcell_fy', 10)
        self.pub_fz = self.create_publisher(Float32, '/oslsim/loadcell_fz', 10)

    def publish_fx(self, val=0.0):
        msg = Float32()
        msg.data = val
        self.pub_fx.publish(msg)

    def publish_fy(self, val=0.0):
        msg = Float32()
        msg.data = val
        self.pub_fy.publish(msg)

    def publish_fz(self, val=0.0):
        msg = Float32()
        msg.data = val
        self.pub_fz.publish(msg)

class LoadcellSub(Node):
    def __init__(self):
        super().__init__('loadcell_sub')
        self.lc = Loadcell()
        self.sub = self.create_subscription(
            ContactsState,
            '/oslsim/loadcell',
            self.loadcell_callback,
            10
        )

    def loadcell_callback(self, data):
        x = 0.0
        y = 0.0
        z = 0.0

        if len(data.states)>0:
            x = data.states[-1].wrenches[0].force.x
            y = data.states[-1].wrenches[0].force.y
            z = data.states[-1].wrenches[0].force.z

        self.lc.publish_fx(x)
        self.lc.publish_fy(y)
        self.lc.publish_fz(z)

def main(args=None):
    rclpy.init(args=args)

    # Create nodes
    loadcell_sub_node = LoadcellSub()
    
    try:
        rclpy.spin(loadcell_sub_node)
    except KeyboardInterrupt:
        pass

    loadcell_sub_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()