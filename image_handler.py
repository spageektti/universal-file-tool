import os
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
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

def adjust_brightness(file_path):
    """Adjust the brightness of an image."""
    try:
        img = Image.open(file_path)
        factor = float(input("Enter brightness factor (0.0 - 2.0): "))
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(factor)
        img.save(file_path)
        print("Brightness adjusted successfully.")
    except Exception as e:
        print(f"Error adjusting brightness: {e}")

def adjust_contrast(file_path):
    """Adjust the contrast of an image."""
    try:
        img = Image.open(file_path)
        factor = float(input("Enter contrast factor (0.0 - 2.0): "))
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(factor)
        img.save(file_path)
        print("Contrast adjusted successfully.")
    except Exception as e:
        print(f"Error adjusting contrast: {e}")

def add_border(file_path):
    """Add a border around the image."""
    try:
        img = Image.open(file_path)
        border_size = int(input("Enter border size (in pixels): "))
        bordered_img = Image.new("RGB", (img.width + 2 * border_size, img.height + 2 * border_size), "black")
        bordered_img.paste(img, (border_size, border_size))
        bordered_img.save(file_path)
        print("Border added successfully.")
    except Exception as e:
        print(f"Error adding border: {e}")

def create_thumbnail(file_path):
    """Create a thumbnail version of the image."""
    try:
        img = Image.open(file_path)
        size = (128, 128)
        img.thumbnail(size)
        thumbnail_path = os.path.splitext(file_path)[0] + "_thumbnail.jpg"
        img.save(thumbnail_path, "JPEG")
        print(f"Thumbnail created successfully: {thumbnail_path}")
    except Exception as e:
        print(f"Error creating thumbnail: {e}")

def overlay_text(file_path):
    """Overlay text on an image."""
    try:
        img = Image.open(file_path)
        draw = ImageDraw.Draw(img)
        text = input("Enter text to overlay: ")
        font_size = int(input("Enter font size: "))
        font = ImageFont.load_default()
        text_width, text_height = draw.textsize(text, font=font)
        position = (img.width // 2 - text_width // 2, img.height // 2 - text_height // 2)
        draw.text(position, text, (255, 255, 255), font=font) 
        img.save(file_path)
        print("Text overlay added successfully.")
    except Exception as e:
        print(f"Error overlaying text: {e}")

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
    print("8. Adjust Brightness")
    print("9. Adjust Contrast")
    print("10. Add Border")
    print("11. Create Thumbnail")
    print("12. Overlay Text")
    print("13. Add Image to PDF")
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
        adjust_brightness(file_path)
    elif choice == "9":
        adjust_contrast(file_path)
    elif choice == "10":
        add_border(file_path)
    elif choice == "11":
        create_thumbnail(file_path)
    elif choice == "12":
        overlay_text(file_path)
    elif choice == "13":
        pdf_path = input("Enter the PDF file path to add the image to: ")
        add_image_to_pdf(pdf_path, file_path)
    else:
        print("Invalid option selected.")
