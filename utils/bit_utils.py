def bytes_to_bits(data: bytes) -> list[int]:
    bits = []
    for byte in data:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)
    return bits


def bits_to_bytes(bits: list[int]) -> bytes:
    """
    Convert list of bits back to bytes
    Safe conversion with alignment handling    """

    # Trim extra bits (preferred)
    usable_length = (len(bits) // 8) * 8
    bits = bits[:usable_length]

    result = bytearray()

    for i in range(0, usable_length, 8):
        byte = 0
        for bit in bits[i:i+8]:
            byte = (byte << 1) | bit
        result.append(byte)

    return bytes(result)