import os
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

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

def add_image_to_pdf(pdf_path, image_path):
    """Add an image to a PDF."""
    try:
        pdf_writer = PdfWriter()
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        img = Image.open(image_path)
        img_pdf_path = os.path.splitext(image_path)[0] + ".pdf"
        img.save(img_pdf_path, "PDF", resolution=100.0)

        img_reader = PdfReader(img_pdf_path)
        for img_page in img_reader.pages:
            pdf_writer.add_page(img_page)

        output_pdf_path = os.path.splitext(pdf_path)[0] + "_with_image.pdf"
        with open(output_pdf_path, "wb") as output_pdf:
            pdf_writer.write(output_pdf)
        print(f"Image added to PDF successfully: {output_pdf_path}")
    except Exception as e:
        print(f"Error adding image to PDF: {e}")

def handle_image(file_path):
    print("1. Resize Image")
    print("2. Convert Image")
    print("3. Rotate Image")
    print("4. Flip Image")
    print("5. Convert to Grayscale")
    print("6. Crop Image")
    print("7. Compress Image")
    print("8. Add Image to PDF")
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
    elif choice == "8":
        pdf_path = input("Enter the PDF file path to add the image to: ")
        add_image_to_pdf(pdf_path, file_path)
    else:
        print("Invalid option selected.")
