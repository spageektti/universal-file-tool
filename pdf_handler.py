import os
from PyPDF2 import PdfReader, PdfWriter

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
