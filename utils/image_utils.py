import os
import numpy as np

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from PIL import Image
from PIL import ImageChops
from PIL import ImageOps
from PIL import ImageFilter
import matplotlib.pyplot as plt
from termcolor import colored

from utils.temp_manager import temp_file

def load_pix(path, w=600, h=450):

    if os.path.exists(path):

        return QPixmap(path).scaled(
            w,
            h,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

    return QPixmap()


def generate_heatmap(
    original,
    stego,
    out = temp_file(".png")
):

    img1 = Image.open(original).convert("RGB")
    img2 = Image.open(stego).convert("RGB")

    arr1 = np.array(img1).astype(np.int16)
    arr2 = np.array(img2).astype(np.int16)

    # Pixel difference
    diff = np.abs(arr1 - arr2)

    # Collapse channels
    diff = diff.mean(axis=2)

    # MASSIVE amplification
    diff = diff * 120

    diff = np.clip(diff, 0, 255)

    diff = diff.astype(np.uint8)

    # Smooth gradients
    heat = Image.fromarray(diff)
    heat = heat.filter(ImageFilter.GaussianBlur(radius=6))

    heat_np = np.array(heat)

    # Thermal colormap
    colored = np.zeros((heat_np.shape[0], heat_np.shape[1], 3), dtype=np.uint8)

# Bright forensic glow
    colored[:, :, 0] = np.clip(heat_np * 2, 0, 255)        # Red
    colored[:, :, 1] = np.clip(heat_np * 0.3, 0, 255)      # Green
    colored[:, :, 2] = np.clip(255 - heat_np, 0, 255)      # Blue

    # ORIGINAL IMAGE AS SILHOUETTE
    base = np.array(img1).astype(np.uint8)

    # Darken original image heavily
    base = (base * 0.25).astype(np.uint8)

    # Blend heatmap with silhouette
    final = np.clip(base + colored, 0, 255)

    final_img = Image.fromarray(final.astype(np.uint8))

    final_img.save(out)

    return out


def generate_bitplane(
    image_path,
    bit=0,
    output=None
):

    img = Image.open(image_path).convert("L")

    px = img.load()

    w, h = img.size

    plane = Image.new("L", (w, h))

    for y in range(h):

        for x in range(w):

            val = (px[x, y] >> bit) & 1

            plane.putpixel(
                (x, y),
                255 if val else 0
            )

    plane.save(output)

    return output