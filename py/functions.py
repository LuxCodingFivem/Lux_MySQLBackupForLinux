"""
Lux_MySQLBackup

Copyright (c) 2025 LuxCoding

This script is licensed under the MIT License.
For full details, see the LICENSE file in the repository.
"""

#Import Libs to for Genreating Key
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import os
import json

# Get the Script Path 
script_dir = os.path.dirname(__file__)

def Generate_Key():
    try:
        # Generate Key
        key = Fernet.generate_key()
    
        # Saving Key
        with open("./key/key.key", "wb") as key_file2:
            key_file2.write(key)

        # Print Success 
        print("Successfull generated Key")

    except Exception as e:
        print("Error by Creating Key: ", e)

def load_key():
    try:
        script_dir_one_back = os.path.normpath(script_dir[:-3])
        with open(os.path.join(script_dir_one_back, "key/key.key"), "r") as key_file:
            key = key_file.read()
            if key != "":
                return key
            else:
                raise Exception("No Key in Key file")
        
    except Exception as e:
        print("Error by Loading Key: ", e)

def encrypt(plain_text):
    try:
        fernet = Fernet(load_key())
        encrypt = fernet.encrypt(plain_text.encode())
        return f"ENC({encrypt.decode('utf-8')})"
    except Exception as e:
        print("Error by Encrypting: ", e)

def decrypt(encrypted_text):
    try:
        if encrypted_text.startswith("ENC(") and encrypted_text.endswith(")"):
            encrypted_base64 = encrypted_text[4:-1]
            Fernet = Fernet(load_key())
            decrypt = Fernet.decrypt(encrypted_base64.encode())
            return decrypt.decode()
        else:
            return encrypted_text
    except Exception as e:
        print("Error by Decrypting: ", e)
        return encrypted_text

def load_settings():
    try:
        script_dir_one_back = os.path.normpath(script_dir[:-3])
        with open(os.path.join(script_dir_one_back, "json/settings.json"), "r") as f:
            json_str = json.load(f)
            return json_str

    except Exception as e:
        print("Error by Loading Settings: ", e)

def save_settings(Settings):
    try:
        script_dir_one_back = os.path.normpath(script_dir[:-3])
        with open(os.path.join(script_dir_one_back, "json/settings.json"), "w") as f:
            f.write(Settings)

    except Exception as e:
        print("Error by Saveing Settings: ", e)

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(input_file, output_file, password):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()

    with open(input_file, 'rb') as f:
        plaintext = f.read()
    padded_data = padder.update(plaintext) + padder.finalize()
    ciphertext = encryptor.update(padded_data)
    final_data = encryptor.finalize()
    ciphertext += final_data

    with open(output_file, 'wb') as f:
        f.write(salt + iv + ciphertext)

def SQL():
    ...

def log_to_discord():
    ...

def pack_backup_to_zip():
    ...

def send_backup_to_discord():
    ...
