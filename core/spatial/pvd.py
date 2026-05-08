from PIL import Image


def get_range(diff):

    if diff < 8:
        return 1

    elif diff < 16:
        return 2

    elif diff < 32:
        return 3

    else:
        return 4


def embed_bits(image_path, bits, output_path):

    img = Image.open(image_path)

    pixels = img.load()

    width, height = img.size

    idx = 0

    for y in range(height):

        for x in range(0, width - 1, 2):

            if idx >= len(bits):
                break

            p1 = list(pixels[x, y])

            for c in range(3):

                if idx >= len(bits):
                    break

                n_bits = 2

                value = 0

                for _ in range(n_bits):

                    value <<= 1

                    if idx < len(bits):
                        value |= bits[idx]
                        idx += 1

                p1[c] = (p1[c] & ~3) | value

            pixels[x, y] = tuple(p1)

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

        for x in range(0, width - 1, 2):

            if idx >= num_bits:
                break

            p1 = pixels[x, y]

            for c in range(3):

                if idx >= num_bits:
                    break

                value = p1[c] & 3

                for i in range(1, -1, -1):

                    if idx < num_bits:

                        bits.append(
                            (value >> i) & 1
                        )

                        idx += 1

        if idx >= num_bits:
            break

    return bits