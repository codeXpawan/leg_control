import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, Float64MultiArray
from sensor_msgs.msg import JointState
import numpy as np

class MotorSimNode(Node):
    def __init__(self):
        super().__init__('motor_sim_node')
        
        # Declare parameters
        self.declare_parameter('motor_nominal_voltage', 50.0)
        self.declare_parameter('moment_of_inertia', 0.0001)
        self.declare_parameter('armature_damping_ratio', 0.0001)
        self.declare_parameter('electromotive_force_constant', 0.056)
        self.declare_parameter('electric_resistance', 0.186)
        self.declare_parameter('electric_inductance', 0.000138)
        self.declare_parameter('gear_ratio', 50.0)
        self.declare_parameter('update_rate', 50.0)
        self.declare_parameter('command_topic', '/motor_voltage/command')
        self.declare_parameter('joint_state_topic', '/joint_states')
        self.declare_parameter('output_torque_topic', '/motor_effort/command')
        self.declare_parameter('motor_name', 'motor_joint')

        # Get parameters
        self.V_nom = self.get_parameter('motor_nominal_voltage').value
        self.J = self.get_parameter('moment_of_inertia').value
        self.b = self.get_parameter('armature_damping_ratio').value
        self.Kt = self.get_parameter('electromotive_force_constant').value
        self.Ke = self.Kt  # Typically Kt = Ke in SI units
        self.R = self.get_parameter('electric_resistance').value
        self.L = self.get_parameter('electric_inductance').value
        self.G = self.get_parameter('gear_ratio').value
        self.dt = 1.0 / self.get_parameter('update_rate').value
        self.motor_name = self.get_parameter('motor_name').value

        # State variables
        self.current_voltage = 0.0
        self.current_velocity_joint = 0.0
        self.armature_current = 0.0
        
        # Subscriptions
        self.cmd_sub = self.create_subscription(
            Float64MultiArray,
            self.get_parameter('command_topic').value,
            self.command_callback,
            10
        )
        self.js_sub = self.create_subscription(
            JointState,
            self.get_parameter('joint_state_topic').value,
            self.joint_state_callback,
            10
        )
        
        # Publisher
        self.torque_pub = self.create_publisher(
            Float64MultiArray,
            self.get_parameter('output_torque_topic').value,
            10
        )
        
        # Timer for simulation loop
        # self.timer = self.create_timer(self.dt, self.timer_callback)
        
        self.get_logger().info(f'Motor Sim Node started for motor: {self.motor_name}')

    def command_callback(self, msg):
        # Input is voltage (or normalized -1 to 1 which we scale by V_nom)
        # Assuming input is actual voltage for now
        if len(msg.data) > 0:
            self.current_voltage = msg.data[0]
            omega_motor = self.current_velocity_joint * self.G
        
            # Steady-state current approximation (V = iR + Ke*omega => i = (V - Ke*omega)/R)
            # This is more stable than di/dt integration when L/R << dt
            # Clamp voltage to nominal
            v_clamped = np.clip(self.current_voltage, -self.V_nom, self.V_nom)
            
            self.armature_current = (v_clamped - self.Ke * omega_motor) / self.R
            
            # Motor Torque
            torque_motor = self.Kt * self.armature_current
            
            # Joint Torque (accounting for gear ratio)
            # Torque_joint = Torque_motor * gear_ratio (assuming 100% efficiency for now)
            torque_joint = torque_motor * self.G
            
            # Publish torque (as Float64MultiArray for JointGroupEffortController)
            msg = Float64MultiArray()
            msg.data = [float(torque_joint)]
            self.torque_pub.publish(msg)


    def joint_state_callback(self, msg):
        if self.motor_name in msg.name:
            idx = msg.name.index(self.motor_name)
            self.current_velocity_joint = msg.velocity[idx]

    def timer_callback(self):
        # DC Motor Equations:
        # V = i*R + L*di/dt + Ke*omega_motor
        # Torque_motor = Kt * i
        # omega_motor = omega_joint * gear_ratio
        
        omega_motor = self.current_velocity_joint * self.G
        
        # Steady-state current approximation (V = iR + Ke*omega => i = (V - Ke*omega)/R)
        # This is more stable than di/dt integration when L/R << dt
        # Clamp voltage to nominal
        v_clamped = np.clip(self.current_voltage, -self.V_nom, self.V_nom)
        
        self.armature_current = (v_clamped - self.Ke * omega_motor) / self.R
        
        # Motor Torque
        torque_motor = self.Kt * self.armature_current
        
        # Joint Torque (accounting for gear ratio)
        # Torque_joint = Torque_motor * gear_ratio (assuming 100% efficiency for now)
        torque_joint = torque_motor * self.G
        
        # Publish torque (as Float64MultiArray for JointGroupEffortController)
        msg = Float64MultiArray()
        msg.data = [float(torque_joint)]
        self.torque_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MotorSimNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
