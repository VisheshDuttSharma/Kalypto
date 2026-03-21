from core.spatial.lsb import encode as lsb_encode, decode as lsb_decode
from core.spatial.adaptive_lsb import encode as alsb_encode, decode as alsb_decode
from core.spatial.utils import normalize_output_path
from core.spatial.pvd import encode as pvd_encode, decode as pvd_decode

def main():
    print("1. Basic LSB")
    print("2. Adaptive LSB")
    print("3. PVD")

    choice = input("Select method: ")

    image_path = input("Enter input image path: ")
    message = input("Enter message: ")
    output_file = input("Enter output file name (optional extension): ")

    output_file = normalize_output_path(output_file)

    if choice == "1":
        lsb_encode(image_path, message, output_file)
        lsb_decode(output_file)

    elif choice == "2":
        alsb_encode(image_path, message, output_file)
        alsb_decode(output_file)

    elif choice == "3":
        pvd_encode(image_path, message, output_file)
        pvd_decode(output_file)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()