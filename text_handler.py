import os
import hashlib
from cryptography.fernet import Fernet

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
        with open(file_path, "r") as file:
            content = file.read()
        print("1. Convert to UPPERCASE")
        print("2. Convert to lowercase")
        choice = input("Select option: ")
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

def text_to_pdf(file_path):
    """Convert a text file to a PDF."""
    try:
        pdf_path = os.path.splitext(file_path)[0] + ".pdf"
        with open(file_path, "r") as file:
            text = file.read()
        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.drawString(72, 720, text)
        c.save()
        print(f"Text file converted to PDF successfully: {pdf_path}")
    except Exception as e:
        print(f"Error converting text to PDF: {e}")

def calculate_hash(file_path, algorithm="sha256"):
    """Calculate the hash of a file."""
    try:
        hash_function = getattr(hashlib, algorithm)
        hasher = hash_function()
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                hasher.update(chunk)
        hash_value = hasher.hexdigest()
        print(f"{algorithm.upper()} hash of {file_path}: {hash_value}")
    except Exception as e:
        print(f"Error calculating hash: {e}")

def aes_encrypt(file_path):
    """Encrypt a text file using AES."""
    try:
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        with open(file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = cipher_suite.encrypt(file_data)
        encrypted_file_path = os.path.splitext(file_path)[0] + "_encrypted.txt"
        with open(encrypted_file_path, "wb") as file:
            file.write(encrypted_data)
        print(f"File encrypted successfully. Key: {key.decode()}")
    except Exception as e:
        print(f"Error encrypting file: {e}")

def aes_decrypt(file_path, key):
    """Decrypt a text file using AES."""
    try:
        cipher_suite = Fernet(key.encode())
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        decrypted_file_path = os.path.splitext(file_path)[0] + "_decrypted.txt"
        with open(decrypted_file_path, "wb") as file:
            file.write(decrypted_data)
        print("File decrypted successfully.")
    except Exception as e:
        print(f"Error decrypting file: {e}")

def handle_text(file_path):
    print("1. Count Words")
    print("2. Count Lines")
    print("3. Find and Replace Text")
    print("4. Convert Text Case")
    print("5. Append Text")
    print("6. Convert Text to PDF")
    print("7. Calculate Hash (SHA-256, SHA-1, MD5)")
    print("8. Encrypt Text with AES")
    print("9. Decrypt Text with AES")
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
    elif choice == "6":
        text_to_pdf(file_path)
    elif choice == "7":
        print("1. SHA-256\n2. SHA-1\n3. MD5")
        hash_choice = input("Select hashing algorithm: ")
        if hash_choice == "1":
            calculate_hash(file_path, "sha256")
        elif hash_choice == "2":
            calculate_hash(file_path, "sha1")
        elif hash_choice == "3":
            calculate_hash(file_path, "md5")
        else:
            print("Invalid option selected.")
    elif choice == "8":
        aes_encrypt(file_path)
    elif choice == "9":
        key = input("Enter the AES decryption key: ")
        aes_decrypt(file_path, key)
    else:
        print("Invalid option selected.")
