import os
import sys
import argparse
from cryptography.fernet import Fernet

class DeltaBox:
    def __init__(self, key_file='deltabox.key'):
        self.key_file = key_file
        self.key = None

    def generate_key(self):
        """Generate a new encryption key."""
        self.key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(self.key)
        print("Encryption key generated and saved.")

    def load_key(self):
        """Load the encryption key from a file."""
        if not os.path.exists(self.key_file):
            raise FileNotFoundError(f"Key file '{self.key_file}' not found. Generate a key first.")
        
        with open(self.key_file, 'rb') as key_file:
            self.key = key_file.read()
        print("Encryption key loaded.")

    def encrypt_file(self, file_path):
        """Encrypt a file."""
        if not self.key:
            self.load_key()

        with open(file_path, 'rb') as file:
            file_data = file.read()

        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(file_data)

        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
        print(f"File '{file_path}' encrypted successfully.")

    def decrypt_file(self, file_path):
        """Decrypt a file."""
        if not self.key:
            self.load_key()

        with open(file_path, 'rb') as file:
            encrypted_data = file.read()

        fernet = Fernet(self.key)
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
        print(f"File '{file_path}' decrypted successfully.")

def main():
    parser = argparse.ArgumentParser(description="DeltaBox - Easy-to-use encryption for files on Windows devices.")
    parser.add_argument('action', choices=['generate_key', 'encrypt', 'decrypt'], help='Action to perform')
    parser.add_argument('target', nargs='?', help='File to encrypt or decrypt')
    args = parser.parse_args()

    deltabox = DeltaBox()

    if args.action == 'generate_key':
        deltabox.generate_key()
    elif args.action == 'encrypt':
        if not args.target:
            print("Please specify a file to encrypt.")
            sys.exit(1)
        deltabox.encrypt_file(args.target)
    elif args.action == 'decrypt':
        if not args.target:
            print("Please specify a file to decrypt.")
            sys.exit(1)
        deltabox.decrypt_file(args.target)

if __name__ == "__main__":
    main()