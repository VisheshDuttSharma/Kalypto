from PIL import Image


def get_intensity(pixel):
    return sum(pixel) // 3


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
            intensity = get_intensity((r, g, b))

            channels = [r, g, b]

            # High intensity → embed more aggressively
            if intensity > 128:
                channels_to_use = 3
            else:
                channels_to_use = 1

            for i in range(channels_to_use):
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

            r, g, b = pixels[x, y]
            intensity = get_intensity((r, g, b))

            channels = [r, g, b]

            if intensity > 128:
                channels_to_use = 3
            else:
                channels_to_use = 1

            for i in range(channels_to_use):
                if idx < num_bits:
                    bits.append(channels[i] & 1)
                    idx += 1

        if idx >= num_bits:
            break

    return bits