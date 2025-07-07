import subprocess
import os

class SampleScene:
    def __init__(self, scene_name, model_name, timestamp):
        self.scene_name = scene_name
        self.model_name = model_name
        self.timestamp = timestamp
        self.output_path = f"outputs/{scene_name}/{model_name}/{timestamp}"
        
    def render_custom_poses(self, poses_json_path, save_dir="renders/custom_view"):
        if not os.path.exists(poses_json_path):
            raise FileNotFoundError(f"Pose file {poses_json_path} not found.")
        
        os.makedirs(save_dir, exist_ok=True)
        
        command = [
            "ns-render", "images",
            "--load-dir", self.output_path,
            "--pose-source", "filename",
            "--camera-poses", poses_json_path,
            "--output-path", save_dir
        ]
        
        print(f"Running command: {' '.join(command)}")
        subprocess.run(command, check=True)
