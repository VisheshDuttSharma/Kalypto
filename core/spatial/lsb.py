from PIL import Image
from .utils import text_to_binary, binary_to_text, add_delimiter, normalize_output_path

def encode(image_path, message, output_path):
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception as e:
        print("❌ Error opening image:", e)
        return

    pixels = img.load()
    width, height = img.size

    binary = add_delimiter(text_to_binary(message))
    idx = 0

    max_capacity = width * height
    if len(binary) > max_capacity:
        print("❌ Error: Message too large for this image.")
        return

    for y in range(height):
        for x in range(width):
            if idx >= len(binary):
                break

            r, g, b = pixels[x, y]
            r = (r & ~1) | int(binary[idx])
            idx += 1

            pixels[x, y] = (r, g, b)

    output_path = normalize_output_path(output_path)

    try:
        img.save(output_path, format="PNG")
        print(f"✅ Saved as {output_path}")
    except Exception as e:
        print("❌ Error saving image:", e)


def decode(image_path):
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception as e:
        print("❌ Error opening image:", e)
        return

    pixels = img.load()
    width, height = img.size

    binary = ""

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary += str(r & 1)

    message = binary_to_text(binary)
    print("🔓 Decoded message:", message)