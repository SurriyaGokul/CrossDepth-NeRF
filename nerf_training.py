import os

def train_scene(scene_path="/kaggle/working/my_scene", max_iters=30000):
    """
    Train Nerfacto scene using ns-train CLI command.
    """
    os.system(f"ns-train nerfacto --data {scene_path} --viewer.quit-on-train-completion True --max-num-iterations {max_iters}")