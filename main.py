import argparse
import os
from image_handler import handle_image
from pdf_handler import handle_pdf
from text_handler import handle_text
from video_handler import handle_video
from markdown_handler import handle_markdown 

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
    elif file_extension in [".mp4", ".avi", ".mov", ".mkv"]:
        handle_video(file_path)
    elif file_extension == ".md":
        handle_markdown(file_path)
    else:
        print("Unsupported file type.")

if __name__ == "__main__":
    main()
