import os

from PIL import Image

from utils.image_utils import (
    generate_heatmap
)
from utils.temp_manager import (
    temp_file
)


class CompareService:

    def generate_bitplane(
        self,
        image_path,
        bit
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

        output = temp_file(".png")

        plane.save(output)

        return output

    def generate_heatmap(
        self,
        original,
        stego
    ):

        return generate_heatmap(
            original,
            stego
        )

    def build_report(
        self,
        original,
        stego
    ):

        return (
            f"Original: {original}\n"
            f"Stego: {stego}\n"
            f"Original Size: {os.path.getsize(original)}\n"
            f"Stego Size: {os.path.getsize(stego)}"
        )