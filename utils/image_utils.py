from pathlib import Path
import numpy as np

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from PIL import Image
from PIL import ImageFilter

from utils.temp_manager import temp_file


def load_pix(path, w=600, h=450):

    path = str(Path(path))

    if Path(path).exists():

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
    out=None
):

    if out is None:
        out = temp_file("heatmap.png")

    img1 = Image.open(original).convert("RGB")
    img2 = Image.open(stego).convert("RGB")

    arr1 = np.array(img1).astype(np.int16)
    arr2 = np.array(img2).astype(np.int16)

    diff = np.abs(arr1 - arr2)

    diff = diff.mean(axis=2)

    diff = diff * 120

    diff = np.clip(diff, 0, 255)

    diff = diff.astype(np.uint8)

    heat = Image.fromarray(diff)
    heat = heat.filter(ImageFilter.GaussianBlur(radius=6))

    heat_np = np.array(heat)

    colored_map = np.zeros(
        (heat_np.shape[0], heat_np.shape[1], 3),
        dtype=np.uint8
    )

    colored_map[:, :, 0] = np.clip(heat_np * 2, 0, 255)
    colored_map[:, :, 1] = np.clip(heat_np * 0.3, 0, 255)
    colored_map[:, :, 2] = np.clip(255 - heat_np, 0, 255)

    base = np.array(img1).astype(np.uint8)

    base = (base * 0.25).astype(np.uint8)

    final = np.clip(base + colored_map, 0, 255)

    final_img = Image.fromarray(final.astype(np.uint8))

    final_img.save(str(out))

    return str(out)


def generate_bitplane(
    image_path,
    bit=0,
    output=None
):

    if output is None:
        output = temp_file(f"bitplane_{bit}.png")

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

    plane.save(str(output))

    return str(output)