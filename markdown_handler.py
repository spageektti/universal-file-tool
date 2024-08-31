import os
import markdown
import subprocess

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

def lint_markdown_file(file_path):
    """Lint a Markdown file using tldr-lint."""
    try:
        result = subprocess.run(['tldr-lint', file_path], capture_output=True, text=True)
        if result.returncode == 0:
            print("Linting successful. No issues found.")
        else:
            print("Linting issues found:")
            print(result.stdout)
            print(result.stderr)
    except FileNotFoundError:
        print("tldr-lint is not installed. Please install it to use this feature.")
    except Exception as e:
        print(f"Error linting Markdown file: {e}")

def preview_markdown(file_path):
    """Preview the Markdown file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as md_file:
            text = md_file.read()
        print("Markdown Preview:")
        print(text)
    except Exception as e:
        print(f"Error previewing Markdown file: {e}")

def count_words_in_markdown(file_path):
    """Count the number of words in the Markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as md_file:
            text = md_file.read()
        word_count = len(text.split())
        print(f"Word count: {word_count}")
    except Exception as e:
        print(f"Error counting words in Markdown file: {e}")

def list_headings_in_markdown(file_path):
    """List all headings in the Markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as md_file:
            text = md_file.readlines()
        headings = [line.strip() for line in text if line.startswith('#')]
        print("Headings found in the Markdown file:")
        for heading in headings:
            print(heading)
    except Exception as e:
        print(f"Error listing headings in Markdown file: {e}")

def append_content_to_markdown(file_path):
    """Append content to an existing Markdown file."""
    try:
        content = input("Enter the content to append to the Markdown file:\n")
        with open(file_path, 'a', encoding='utf-8') as md_file:
            md_file.write("\n" + content)
        print(f"Content appended successfully to: {file_path}")
    except Exception as e:
        print(f"Error appending content to Markdown file: {e}")

def handle_markdown(file_path):
    """Handle Markdown file operations."""
    print("1. Convert Markdown to HTML")
    print("2. Extract Text from Markdown")
    print("3. Create a New Markdown File")
    print("4. Lint Markdown File with tldr-lint (requires tldr-lint to be installed)")
    print("5. Preview Markdown File")
    print("6. Count Words in Markdown File")
    print("7. List Headings in Markdown File")
    print("8. Append Content to Markdown File")
    choice = input("Select option: ")
    if choice == "1":
        convert_markdown_to_html(file_path)
    elif choice == "2":
        extract_text_from_markdown(file_path)
    elif choice == "3":
        new_file_path = input("Enter the new Markdown file path: ")
        create_markdown_file(new_file_path)
    elif choice == "4":
        lint_markdown_file(file_path)
    elif choice == "5":
        preview_markdown(file_path)
    elif choice == "6":
        count_words_in_markdown(file_path)
    elif choice == "7":
        list_headings_in_markdown(file_path)
    elif choice == "8":
        append_content_to_markdown(file_path)
    else:
        print("Invalid option selected.")
