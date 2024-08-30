import argparse
import os
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter

def resize_image(file_path):
    """Resize an image."""
    try:
        img = Image.open(file_path)
        print(f"Current size: {img.size}")
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))
        img = img.resize((width, height))
        img.save(file_path)
        print("Image resized successfully.")
    except Exception as e:
        print(f"Error resizing image: {e}")

def convert_image(file_path):
    """Convert image to another format."""
    try:
        img = Image.open(file_path)
        format_map = {"1": "JPEG", "2": "PNG", "3": "BMP", "4": "GIF"}
        print("Choose format to convert to:")
        print("1. JPEG\n2. PNG\n3. BMP\n4. GIF")
        choice = input("Select option: ")
        format_to = format_map.get(choice, "JPEG")
        new_file_path = os.path.splitext(file_path)[0] + f".{format_to.lower()}"
        img.save(new_file_path, format_to)
        print(f"Image converted to {format_to} successfully.")
    except Exception as e:
        print(f"Error converting image: {e}")

def rotate_image(file_path):
    """Rotate an image."""
    try:
        img = Image.open(file_path)
        angle = int(input("Enter angle to rotate (in degrees): "))
        img = img.rotate(angle)
        img.save(file_path)
        print("Image rotated successfully.")
    except Exception as e:
        print(f"Error rotating image: {e}")

def flip_image(file_path):
    """Flip an image."""
    try:
        img = Image.open(file_path)
        print("1. Flip horizontally")
        print("2. Flip vertically")
        choice = input("Select option: ")
        if choice == "1":
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif choice == "2":
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            print("Invalid option selected.")
            return
        img.save(file_path)
        print("Image flipped successfully.")
    except Exception as e:
        print(f"Error flipping image: {e}")

def grayscale_image(file_path):
    """Convert image to grayscale."""
    try:
        img = Image.open(file_path)
        img = img.convert("L")
        img.save(file_path)
        print("Image converted to grayscale successfully.")
    except Exception as e:
        print(f"Error converting image to grayscale: {e}")

def crop_image(file_path):
    """Crop an image."""
    try:
        img = Image.open(file_path)
        print(f"Current size: {img.size}")
        left = int(input("Enter left coordinate: "))
        top = int(input("Enter top coordinate: "))
        right = int(input("Enter right coordinate: "))
        bottom = int(input("Enter bottom coordinate: "))
        img = img.crop((left, top, right, bottom))
        img.save(file_path)
        print("Image cropped successfully.")
    except Exception as e:
        print(f"Error cropping image: {e}")

def compress_image(file_path):
    """Compress an image by adjusting quality."""
    try:
        img = Image.open(file_path)
        quality = int(input("Enter compression quality (1-100): "))
        img.save(file_path, quality=quality)
        print("Image compressed successfully.")
    except Exception as e:
        print(f"Error compressing image: {e}")

def pdf_to_text(file_path):
    """Convert PDF to text."""
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        text_file_path = os.path.splitext(file_path)[0] + ".txt"
        with open(text_file_path, "w") as text_file:
            text_file.write(text)
        print("PDF converted to text successfully.")
    except Exception as e:
        print(f"Error converting PDF to text: {e}")

def handle_image(file_path):
    print("1. Resize Image")
    print("2. Convert Image")
    print("3. Rotate Image")
    print("4. Flip Image")
    print("5. Convert to Grayscale")
    print("6. Crop Image")
    print("7. Compress Image")
    choice = input("Select option: ")
    if choice == "1":
        resize_image(file_path)
    elif choice == "2":
        convert_image(file_path)
    elif choice == "3":
        rotate_image(file_path)
    elif choice == "4":
        flip_image(file_path)
    elif choice == "5":
        grayscale_image(file_path)
    elif choice == "6":
        crop_image(file_path)
    elif choice == "7":
        compress_image(file_path)
    else:
        print("Invalid option selected.")

def handle_pdf(file_path):
    print("1. Convert PDF to Text")
    choice = input("Select option: ")
    if choice == "1":
        pdf_to_text(file_path)
    else:
        print("Invalid option selected.")

def main():
    parser = argparse.ArgumentParser(description="Universal File Tool (UFT)")
    parser.add_argument("file", help="The file to be processed")
    args = parser.parse_args()
    file_path = args.file

    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    if file_extension in [".jpg", ".jpeg", ".png", ".bmp", ".gif"]:
        handle_image(file_path)
    elif file_extension == ".pdf":
        handle_pdf(file_path)
    else:
        print("Unsupported file type.")

if __name__ == "__main__":
    main()
