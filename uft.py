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


def merge_pdfs(output_path, *input_files):
    """Merge multiple PDF files into one."""
    try:
        writer = PdfWriter()
        for file_path in input_files:
            reader = PdfReader(file_path)
            for page in reader.pages:
                writer.add_page(page)
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)
        print(f"PDFs merged successfully into {output_path}.")
    except Exception as e:
        print(f"Error merging PDFs: {e}")


def split_pdf(file_path):
    """Split a PDF file into individual pages."""
    try:
        reader = PdfReader(file_path)
        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)
            output_path = os.path.splitext(file_path)[0] + f"_page_{i + 1}.pdf"
            with open(output_path, "wb") as output_pdf:
                writer.write(output_pdf)
        print("PDF split successfully.")
    except Exception as e:
        print(f"Error splitting PDF: {e}")


def extract_pages(file_path):
    """Extract specific pages from a PDF."""
    try:
        reader = PdfReader(file_path)
        writer = PdfWriter()
        pages = input("Enter page numbers to extract (comma-separated, e.g., 1,3,5): ")
        pages = [int(p) - 1 for p in pages.split(",")]
        for page_num in pages:
            writer.add_page(reader.pages[page_num])
        output_path = os.path.splitext(file_path)[0] + "_extracted.pdf"
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)
        print("Pages extracted successfully.")
    except Exception as e:
        print(f"Error extracting pages: {e}")


def rotate_pages(file_path):
    """Rotate specific pages in a PDF."""
    try:
        reader = PdfReader(file_path)
        writer = PdfWriter()
        pages = input("Enter page numbers to rotate (comma-separated, e.g., 1,3,5): ")
        pages = [int(p) - 1 for p in pages.split(",")]
        angle = int(input("Enter angle to rotate (90, 180, 270): "))
        for i, page in enumerate(reader.pages):
            if i in pages:
                page.rotate_clockwise(angle)
            writer.add_page(page)
        output_path = os.path.splitext(file_path)[0] + "_rotated.pdf"
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)
        print("Pages rotated successfully.")
    except Exception as e:
        print(f"Error rotating pages: {e}")


def compress_pdf(file_path):
    """Compress a PDF by reducing its quality."""
    try:
        reader = PdfReader(file_path)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.add_metadata(reader.metadata)
        output_path = os.path.splitext(file_path)[0] + "_compressed.pdf"
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)
        print(f"PDF compressed successfully into {output_path}.")
    except Exception as e:
        print(f"Error compressing PDF: {e}")


def count_words(file_path):
    """Count the number of words in a text file."""
    try:
        with open(file_path, "r") as file:
            text = file.read()
        word_count = len(text.split())
        print(f"Word count: {word_count}")
    except Exception as e:
        print(f"Error counting words: {e}")


def count_lines(file_path):
    """Count the number of lines in a text file."""
    try:
        with open(file_path, "r") as file:
            line_count = sum(1 for line in file)
        print(f"Line count: {line_count}")
    except Exception as e:
        print(f"Error counting lines: {e}")


def find_and_replace(file_path):
    """Find and replace text in a file."""
    try:
        find_text = input("Enter the text to find: ")
        replace_text = input("Enter the text to replace with: ")
        with open(file_path, "r") as file:
            content = file.read()
        content = content.replace(find_text, replace_text)
        with open(file_path, "w") as file:
            file.write(content)
        print("Text replaced successfully.")
    except Exception as e:
        print(f"Error finding and replacing text: {e}")


def convert_case(file_path):
    """Convert text to uppercase or lowercase."""
    try:
        print("1. Convert to Uppercase")
        print("2. Convert to Lowercase")
        choice = input("Select option: ")
        with open(file_path, "r") as file:
            content = file.read()
        if choice == "1":
            content = content.upper()
        elif choice == "2":
            content = content.lower()
        else:
            print("Invalid option selected.")
            return
        with open(file_path, "w") as file:
            file.write(content)
        print("Text case converted successfully.")
    except Exception as e:
        print(f"Error converting text case: {e}")


def append_text(file_path):
    """Append text to a file."""
    try:
        new_text = input("Enter text to append: ")
        with open(file_path, "a") as file:
            file.write(new_text)
        print("Text appended successfully.")
    except Exception as e:
        print(f"Error appending text: {e}")


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
    print("2. Merge PDFs")
    print("3. Split PDF")
    print("4. Extract Pages from PDF")
    print("5. Rotate Pages in PDF")
    print("6. Compress PDF")
    choice = input("Select option: ")
    if choice == "1":
        pdf_to_text(file_path)
    elif choice == "2":
        output_path = input("Enter output file path for merged PDF: ")
        input_files = input("Enter input PDF files to merge (comma-separated): ").split(",")
        merge_pdfs(output_path, *input_files)
    elif choice == "3":
        split_pdf(file_path)
    elif choice == "4":
        extract_pages(file_path)
    elif choice == "5":
        rotate_pages(file_path)
    elif choice == "6":
        compress_pdf(file_path)
    else:
        print("Invalid option selected.")


def handle_text(file_path):
    print("1. Count Words")
    print("2. Count Lines")
    print("3. Find and Replace Text")
    print("4. Convert Text Case")
    print("5. Append Text")
    choice = input("Select option: ")
    if choice == "1":
        count_words(file_path)
    elif choice == "2":
        count_lines(file_path)
    elif choice == "3":
        find_and_replace(file_path)
    elif choice == "4":
        convert_case(file_path)
    elif choice == "5":
        append_text(file_path)
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
    elif file_extension == ".txt":
        handle_text(file_path)
    else:
        print("Unsupported file type.")


if __name__ == "__main__":
    main()
