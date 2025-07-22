import json
import numpy as np

def create_spiral_camera_path(transforms_json_path, output_json_path):
    """
    Create a spiral camera path JSON based on transforms file.
    """
    with open(transforms_json_path, "r") as f:
        transforms = json.load(f)

    camera_positions = [np.array(f["transform_matrix"])[:3, 3] for f in transforms["frames"]]
    camera_positions = np.array(camera_positions)
    look_at = np.mean(camera_positions, axis=0)

    num_frames = 90
    radius = 1.5
    fixed_z = look_at[2] + 0.5
    seconds = 6
    fov = 60
    render_width = 800
    render_height = 800
    up = np.array([0.0, 0.0, 1.0])

    def normalize(v):
        return v / np.linalg.norm(v)

    def create_camera_to_world(position, look_at, up):
        forward = normalize(look_at - position)
        right = normalize(np.cross(forward, up))
        up_corrected = np.cross(right, forward)
        c2w = np.eye(4)
        c2w[:3, 0] = right
        c2w[:3, 1] = up_corrected
        c2w[:3, 2] = -forward
        c2w[:3, 3] = position
        return c2w

    frames = []
    for i in range(num_frames):
        angle = 2 * np.pi * i / num_frames
        x = look_at[0] + radius * np.cos(angle)
        y = look_at[1] + radius * np.sin(angle)
        z = fixed_z

        position = np.array([x, y, z])
        c2w = create_camera_to_world(position, look_at, up)

        frames.append({
            "camera_to_world": c2w.tolist(),
            "fov": fov
        })

    spiral_camera_path = {
        "version": "1.0",
        "seconds": seconds,
        "render_height": render_height,
        "render_width": render_width,
        "camera_path": frames
    }

    with open(output_json_path, "w") as f:
        json.dump(spiral_camera_path, f, indent=2)

    print(f"Spiral camera path saved to {output_json_path}")
