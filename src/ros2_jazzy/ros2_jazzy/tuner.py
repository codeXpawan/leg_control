#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from pid_tune.msg import PidTune
from tkinter import *

class PID(Node):
	def __init__(self, title, topic, kp=100, ki=0, kd=0, queue_size=1000):
		super().__init__('pid_gui_' + topic.replace('/', '_'))
		self.pub_pid = self.create_publisher(PidTune, topic, queue_size)
		self.pid_params = PidTune()

		self.root = Tk()
		self.root.configure()
		self.root.title(title)
		self.root.attributes("-topmost", True)
		self.root.geometry('320x240') 

		self.kpscale = Scale(self.root, orient='horizontal', highlightthickness=0, bd=0, fg="black", troughcolor="#00274C", from_=0, to=1200, label= 'Proportional gain (Kp):', width = "15", length = "300", sliderlength="15")
		self.kiscale = Scale(self.root, orient='horizontal', highlightthickness=0, bd=0, fg="black", troughcolor="#00274C", from_=0, to=1200, label= 'Integral gain (Ki):', width = "15", length = "300", sliderlength="15")
		self.kdscale = Scale(self.root, orient='horizontal', highlightthickness=0, bd=0, fg="black", troughcolor="#00274C", from_=0, to=1200, label= 'Derivative gain (Kd):', width = "15", length = "300", sliderlength="15")

		self.kpscale.set(kp)
		self.kiscale.set(ki)
		self.kdscale.set(kd)

		self.kpscale.pack(pady=2)
		self.kiscale.pack(pady=2)
		self.kdscale.pack(pady=2)

		self.set_value()

		Button(self.root, highlightthickness=0, bd=0, bg="#FFCB05", activeforeground="white", activebackground="#00274C", text='Update', command=self.set_value, height=2, width=8).pack(pady=10)

	def set_value(self):

		self.pid_params.kp = float(self.kpscale.get())
		self.pid_params.ki = float(self.kiscale.get())
		self.pid_params.kd = float(self.kdscale.get())
		self.pub_pid.publish(self.pid_params)

def main(args=None):
    rclpy.init(args=args)

    # Create PID GUIs
    osl_knee_pid = PID(title='OSL Knee PID', topic='/oslsim/osl_knee/pid', kp=250, ki=4, kd=1)
    osl_ankle_pid = PID(title='OSL Ankle PID', topic='/oslsim/osl_ankle/pid', kp=50, ki=0, kd=0)

    # Start Tkinter GUI mainloops
    osl_knee_pid.root.mainloop()
    osl_ankle_pid.root.mainloop()

    # Cleanup
    osl_knee_pid.destroy_node()
    osl_ankle_pid.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()