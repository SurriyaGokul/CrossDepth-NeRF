import os
import cv2
import torch
import numpy as np
import matplotlib.pyplot as plt
from depth_anything_v2.dpt import DepthAnythingV2

def generate_colored_depth(image_path, save_path, model_path='checkpoints/depth_anything_v2_vitl.pth'):
    # Load image
    raw_img = cv2.imread(image_path)
    if raw_img is None:
        raise FileNotFoundError(f"Cannot read image at {image_path}")
    
    # Load model
    model = DepthAnythingV2(encoder='vitl', features=256, out_channels=[256, 512, 1024, 1024])
    model.load_state_dict(torch.load(model_path, map_location='cpu'))
    model.eval()

    # Infer raw depth
    depth = model.infer_image(raw_img)  # H x W

    # Normalize and colorize
    norm_depth = (depth - depth.min()) / (depth.max() - depth.min() + 1e-6)
    cmap = plt.get_cmap('inferno')
    colored_depth = cmap(norm_depth)[:, :, :3]
    colored_depth_uint8 = (colored_depth * 255).astype(np.uint8)
    colored_depth_bgr = cv2.cvtColor(colored_depth_uint8, cv2.COLOR_RGB2BGR)

    # Save result
    cv2.imwrite(save_path, colored_depth_bgr)
    print(f"Saved depth map at {save_path}")
