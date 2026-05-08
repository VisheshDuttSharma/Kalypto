from PIL import Image


def embed_bits(image_path, bits, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    if len(bits) > width * height * 3:
        raise ValueError("Payload too large")

    idx = 0

    for y in range(height):
        for x in range(width):
            if idx >= len(bits):
                break

            r, g, b = pixels[x, y]

            channels = [r, g, b]

            for i in range(3):
                if idx < len(bits):
                    channels[i] = (channels[i] & ~1) | bits[idx]
                    idx += 1

            pixels[x, y] = tuple(channels)

        if idx >= len(bits):
            break

    img.save(output_path)


def extract_bits(image_path, num_bits):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    bits = []
    idx = 0

    for y in range(height):
        for x in range(width):
            if idx >= num_bits:
                break

            for val in pixels[x, y]:
                if idx < num_bits:
                    bits.append(val & 1)
                    idx += 1

        if idx >= num_bits:
            break

    return bits