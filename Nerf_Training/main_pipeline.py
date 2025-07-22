from train_test_split import split_transforms_json
from nerf_training import train_scene
from camera_path import create_spiral_camera_path
from render_path import render_path
import yaml
# Load configuration from YAML file
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)
# Extract paths from the configuration
transforms_json = config['transforms_json']
spiral_json = config['spiral_json']
config_yaml = config['config_yaml']
scene_path = config['scene_path']

# Step 1: Train Test split
split_transforms_json(transforms_json)

# Step 2: Train
train_scene(scene_path, max_iters=10)

# Step 3: Create spiral path
create_spiral_camera_path(transforms_json, spiral_json)

# Step 4: Render
render_path(config_yaml, spiral_json)
