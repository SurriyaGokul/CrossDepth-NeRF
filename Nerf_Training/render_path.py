import os

def render_path(config_yaml, camera_path_json, output_video_path="/kaggle/working/my_render.mp4"):
    """
    Render using Nerfstudio CLI and a custom camera path.
    """
    os.system(f"ns-render camera-path --load-config {config_yaml} --camera-path-filename {camera_path_json} --output-path {output_video_path}")
    print("Render completed.")
