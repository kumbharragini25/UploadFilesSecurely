
from cryptography.fernet import Fernet

def encrypt_file(file_path):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    with open(file_path, 'rb') as f:
        file_data = f.read()

    encrypted_data = cipher_suite.encrypt(file_data)

    with open(file_path, 'wb') as f:
        f.write(encrypted_data)

    return key