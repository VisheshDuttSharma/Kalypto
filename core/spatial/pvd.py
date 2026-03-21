from PIL import Image
from .utils import text_to_binary, binary_to_text, add_delimiter, normalize_output_path


def get_bits(diff):
    return 2 if diff < 32 else 3


def encode(image_path, message, output_path):
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception as e:
        print("❌ Error opening image:", e)
        return

    pixels = list(img.getdata())

    binary = add_delimiter(text_to_binary(message))
    idx = 0

    new_pixels = []

    i = 0
    while i < len(pixels) - 1:
        r1, g1, b1 = pixels[i]
        r2, g2, b2 = pixels[i + 1]

        diff = abs(r1 - r2)
        bits = get_bits(diff)

        # Build value
        value = 0
        for _ in range(bits):
            if idx < len(binary):
                value = (value << 1) | int(binary[idx])
                idx += 1

        # Embed in r2
        r2 = (r2 & ~((1 << bits) - 1)) | value

        new_pixels.extend([(r1, g1, b1), (r2, g2, b2)])

        i += 2

        if idx >= len(binary):
            break

    # Add remaining pixels
    new_pixels.extend(pixels[i:])

    img.putdata(new_pixels)

    output_path = normalize_output_path(output_path)

    try:
        img.save(output_path, format="PNG")
        print(f"✅ PVD Saved as {output_path}")
    except Exception as e:
        print("❌ Error saving image:", e)


def decode(image_path):
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception as e:
        print("❌ Error opening image:", e)
        return

    pixels = list(img.getdata())

    binary = ""

    i = 0
    while i < len(pixels) - 1:
        r1, g1, b1 = pixels[i]
        r2, g2, b2 = pixels[i + 1]

        diff = abs(r1 - r2)
        bits = get_bits(diff)

        value = r2 & ((1 << bits) - 1)
        binary += format(value, f'0{bits}b')

        i += 2

    message = binary_to_text(binary)
    print("🔓 Decoded message:", message)