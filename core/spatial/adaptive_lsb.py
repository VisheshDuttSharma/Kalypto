from PIL import Image
from .utils import text_to_binary, binary_to_text, add_delimiter, normalize_output_path


def get_bits(x, y):
    return 2 if (x + y) % 2 == 0 else 1


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

    max_capacity = width * height * 2
    if len(binary) > max_capacity:
        print("❌ Error: Message too large for this image.")
        return

    for y in range(height):
        for x in range(width):
            if idx >= len(binary):
                break

            r, g, b = pixels[x, y]
            bits = get_bits(x, y)

            value = 0
            for i in range(bits):
                if idx < len(binary):
                    value = (value << 1) | int(binary[idx])
                    idx += 1

            r = (r & ~((1 << bits) - 1)) | value
            pixels[x, y] = (r, g, b)

    output_path = normalize_output_path(output_path)

    try:
        img.save(output_path, format="PNG")
        print(f"✅ Adaptive LSB Saved as {output_path}")
    except Exception as e:
        print("❌ Error saving image:", e)


def decode(image_path):
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception as e:
        print("❌ Error opening image:", e)
        return None

    pixels = img.load()
    width, height = img.size

    binary = ""

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            bits = get_bits(x, y)

            value = r & ((1 << bits) - 1)
            binary += format(value, f'0{bits}b')

    message = binary_to_text(binary)
    print("🔓 Decoded message:", message)

    return message  # 🔥 IMPORTANT FIX