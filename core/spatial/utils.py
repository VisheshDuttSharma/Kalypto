def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    result = ""
    for c in chars:
        if c == '11111110':
            break
        result += chr(int(c, 2))
    return result

def add_delimiter(binary):
    return binary + '11111110'


# 🔥 NEW: Normalize output to safe format
def normalize_output_path(filename):
    if not filename.lower().endswith(".png"):
        print("⚠️ Warning: Non-PNG format detected. Converting to PNG for safe steganography.")
        filename = filename.split(".")[0] + ".png"
    return filename