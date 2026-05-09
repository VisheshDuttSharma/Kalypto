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

        img = Image.open(
            str(image_path)
        ).convert("L")

        px = img.load()

        w, h = img.size

        plane = Image.new(
            "L",
            (w, h)
        )

        for y in range(h):

            for x in range(w):

                val = (
                    (px[x, y] >> bit) & 1
                )

                plane.putpixel(
                    (x, y),
                    255 if val else 0
                )

        output = temp_file(
            f"bitplane_{bit}.png"
        )

        plane.save(str(output))

        return str(output)

    def generate_heatmap(
        self,
        original,
        stego
    ):

        return generate_heatmap(
            str(original),
            str(stego)
        )

    def build_report(
        self,
        original,
        stego
    ):

        report = []

        report.append(
            "=== KALYPTO ANALYSIS REPORT ==="
        )

        report.append("")

        report.append(
            f"Original File: {original}"
        )

        report.append(
            f"Stego File: {stego}"
        )

        report.append("")

        report.append(
            "Analysis Modules:"
        )

        report.append(
            "- Visual Compare"
        )

        report.append(
            "- Heatmap Analysis"
        )

        report.append(
            "- Bit Plane Extraction"
        )

        report.append("")

        report.append(
            "Cross-platform compatibility enabled."
        )

        report.append(
            "Filesystem abstraction active."
        )

        return "\n".join(report)