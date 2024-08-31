import os
from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path

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

def add_watermark(input_pdf_path, watermark_pdf_path, output_pdf_path):
    """Add a watermark to each page of a PDF."""
    try:
        reader = PdfReader(input_pdf_path)
        watermark = PdfReader(watermark_pdf_path)
        writer = PdfWriter()

        for page in reader.pages:
            page.merge_page(watermark.pages[0])
            writer.add_page(page)

        with open(output_pdf_path, "wb") as output_pdf:
            writer.write(output_pdf)
        print(f"Watermark added successfully to {output_pdf_path}.")
    except Exception as e:
        print(f"Error adding watermark: {e}")

def search_text_in_pdf(file_path):
    """Search for specific text in a PDF and return the pages where it is found."""
    try:
        reader = PdfReader(file_path)
        search_text = input("Enter text to search for: ")
        found_pages = []

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text and search_text in text:
                found_pages.append(i + 1)

        if found_pages:
            print(f"Text found on pages: {', '.join(map(str, found_pages))}")
        else:
            print("Text not found in the PDF.")
    except Exception as e:
        print(f"Error searching text in PDF: {e}")

def extract_images_from_pdf(file_path):
    """Extract images from a PDF and save them as separate files."""
    try:
        reader = PdfReader(file_path)
        image_count = 0

        for i, page in enumerate(reader.pages):
            images = page.images
            for img_index, img in enumerate(images):
                image_count += 1
                image_data = img.data
                image_file_path = os.path.splitext(file_path)[0] + f"_image_{image_count}.png"
                with open(image_file_path, "wb") as img_file:
                    img_file.write(image_data)
                print(f"Extracted image saved as {image_file_path}.")

        if image_count == 0:
            print("No images found in the PDF.")
    except Exception as e:
        print(f"Error extracting images from PDF: {e}")

def convert_pdf_to_image(file_path):
    """Convert each page of a PDF to an image."""
    try:
        images = convert_from_path(file_path)
        image_count = 0
        for i, image in enumerate(images):
            image_count += 1
            image_file_path = os.path.splitext(file_path)[0] + f"_page_{image_count}.png"
            image.save(image_file_path, "PNG")
            print(f"Converted page {i + 1} to image: {image_file_path}.")
    except Exception as e:
        print(f"Error converting PDF to image: {e}")

def merge_pdf_with_password(output_path, password, *input_files):
    """Merge multiple PDF files into one with password protection."""
    try:
        writer = PdfWriter()
        for file_path in input_files:
            reader = PdfReader(file_path)
            for page in reader.pages:
                writer.add_page(page)
        writer.encrypt(password)
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)
        print(f"PDFs merged successfully into {output_path} with password protection.")
    except Exception as e:
        print(f"Error merging PDFs with password: {e}")

def remove_password_from_pdf(file_path):
    """Remove password protection from a PDF."""
    try:
        password = input("Enter the password to unlock the PDF: ")
        reader = PdfReader(file_path)
        if reader.is_encrypted:
            reader.decrypt(password)
            output_path = os.path.splitext(file_path)[0] + "_unlocked.pdf"
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            with open(output_path, "wb") as output_pdf:
                writer.write(output_pdf)
            print(f"Password removed successfully. Unlocked PDF saved as {output_path}.")
        else:
            print("The PDF is not password protected.")
    except Exception as e:
        print(f"Error removing password from PDF: {e}")

def handle_pdf(file_path):
    print("1. Convert PDF to Text")
    print("2. Merge PDFs")
    print("3. Split PDF")
    print("4. Extract Pages from PDF")
    print("5. Rotate Pages in PDF")
    print("6. Compress PDF")
    print("7. Add Watermark to PDF")
    print("8. Search Text in PDF")
    print("9. Extract Images from PDF")
    print("10. Convert PDF to Image")
    print("11. Merge PDFs with Password Protection")
    print("12. Remove Password from PDF")
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
    elif choice == "7":
        watermark_pdf_path = input("Enter watermark PDF file path: ")
        output_path = input("Enter output file path for watermarked PDF: ")
        add_watermark(file_path, watermark_pdf_path, output_path)
    elif choice == "8":
        search_text_in_pdf(file_path)
    elif choice == "9":
        extract_images_from_pdf(file_path)
    elif choice == "10":
        convert_pdf_to_image(file_path)
    elif choice == "11":
        output_path = input("Enter output file path for merged PDF with password: ")
        password = input("Enter password for the merged PDF: ")
        input_files = input("Enter input PDF files to merge (comma-separated): ").split(",")
        merge_pdf_with_password(output_path, password, *input_files)
    elif choice == "12":
        remove_password_from_pdf(file_path)
    else:
        print("Invalid option selected.")

# Example usage:
# handle_pdf("path_to_your_pdf_file.pdf")
