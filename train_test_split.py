import json
import random
from pathlib import Path

def split_transforms_json(json_path_str):
    """
    Split transforms.json into train/val/test and clean paths.
    """
    json_path = Path(json_path_str)

    with open(json_path, "r") as f:
        data = json.load(f)

    for frame in data["frames"]:
        fname = Path(frame["file_path"]).name
        base = fname.split(".")[0]
        frame["file_path"] = f"./images/{base}.jpg"

    random.seed(42)
    random.shuffle(data["frames"])

    n = len(data["frames"])
    n_train = int(0.8 * n)
    n_val = int(0.1 * n)
    n_test = n - n_train - n_val

    frames_train = data["frames"][:n_train]
    frames_val = data["frames"][n_train:n_train+n_val]
    frames_test = data["frames"][n_train+n_val:]

    base_out = json_path.parent
    for name, frames in [("train", frames_train), ("val", frames_val), ("test", frames_test)]:
        out_data = data.copy()
        out_data["frames"] = frames
        out_path = base_out / f"transforms_{name}.json"
        with open(out_path, "w") as f:
            json.dump(out_data, f, indent=4)
        print(f"Saved {name}: {out_path} with {len(frames)} frames")
