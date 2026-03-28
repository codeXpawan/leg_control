import os
import time
import subprocess
import rclpy
from rclpy.parameter import Parameter
from rcl_interfaces.srv import SetParameters
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURATION ---
URDF_PATH = "/home/pika/Hari/leg/oslsim/src/ros2_jazzy/urdf/newoslsim.xacro"
NODE_NAME = "/robot_state_publisher"
# ---------------------

class UrdfUpdateHandler(FileSystemEventHandler):
    def __init__(self, node):
        self.node = node
        self.client = self.node.create_client(SetParameters, f'{NODE_NAME}/set_parameters')

    def on_modified(self, event):
        if event.src_path == URDF_PATH:
            print(f"🔄 Change detected. Updating...")
            self.reload_urdf()

    def reload_urdf(self):
        try:
            # 1. Generate URDF from Xacro
            cmd = f"ros2 run xacro xacro {URDF_PATH} mesh_dir:=package://ros2_jazzy"
            urdf_content = subprocess.check_output(cmd, shell=True).decode('utf-8')
            
            # 2. Wait for service
            if not self.client.wait_for_service(timeout_sec=1.0):
                print(f"❌ Service {NODE_NAME} not available. Is the node running?")
                return

            # 3. Prepare Parameter Update Request
            param = Parameter('robot_description', Parameter.Type.STRING, urdf_content)
            request = SetParameters.Request()
            request.parameters = [param.to_parameter_msg()]
            
            # 4. Call Service
            future = self.client.call_async(request)
            print("✅ Parameter update sent to robot_state_publisher!")
            
        except Exception as e:
            print(f"❌ Update failed: {e}")

def main():
    rclpy.init()
    node = rclpy.create_node('urdf_live_reloader')
    
    event_handler = UrdfUpdateHandler(node)
    observer = Observer()
    observer.schedule(event_handler, os.path.dirname(URDF_PATH), recursive=False)
    
    print(f"🚀 Pipeline active. Watching: {URDF_PATH}")
    observer.start()
    
    try:
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.1)
    except KeyboardInterrupt:
        pass
    finally:
        observer.stop()
        observer.join()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
