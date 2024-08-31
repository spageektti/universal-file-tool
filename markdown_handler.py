import os
import markdown

def convert_markdown_to_html(file_path):
    """Convert Markdown file to HTML."""
    try:
        with open(file_path, 'r', encoding='utf-8') as md_file:
            text = md_file.read()
        html = markdown.markdown(text)
        html_file_path = os.path.splitext(file_path)[0] + ".html"
        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html)
        print(f"Markdown converted to HTML successfully: {html_file_path}")
    except Exception as e:
        print(f"Error converting Markdown to HTML: {e}")

def extract_text_from_markdown(file_path):
    """Extract plain text from a Markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as md_file:
            text = md_file.read()
        plain_text = markdown.markdown(text, extensions=['markdown.extensions.extra'])
        plain_text_file_path = os.path.splitext(file_path)[0] + "_extracted.txt"
        with open(plain_text_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(plain_text)
        print(f"Text extracted from Markdown successfully: {plain_text_file_path}")
    except Exception as e:
        print(f"Error extracting text from Markdown: {e}")

def create_markdown_file(file_path):
    """Create a new Markdown file."""
    try:
        content = input("Enter the content for the new Markdown file:\n")
        with open(file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(content)
        print(f"Markdown file created successfully: {file_path}")
    except Exception as e:
        print(f"Error creating Markdown file: {e}")

def handle_markdown(file_path):
    """Handle Markdown file operations."""
    print("1. Convert Markdown to HTML")
    print("2. Extract Text from Markdown")
    print("3. Create a New Markdown File")
    choice = input("Select option: ")
    if choice == "1":
        convert_markdown_to_html(file_path)
    elif choice == "2":
        extract_text_from_markdown(file_path)
    elif choice == "3":
        new_file_path = input("Enter the new Markdown file path: ")
        create_markdown_file(new_file_path)
    else:
        print("Invalid option selected.")
