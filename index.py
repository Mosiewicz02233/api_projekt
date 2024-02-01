#biblioteki uzytkowe

from flask import Flask, request, send_file
from cryptography.fernet import Fernet
import os
import uuid
import json
from flask import send_from_directory

def get_filename_from_json(file_code):
    with open("filename.json", 'r') as file:
        json_data = json.load(file)
    if file_code in json_data:
        return json_data[file_code]
    
def generate_key():
    if not os.path.exists(key_path):
        key = Fernet.generate_key()
        with open(key_path, 'wb') as file_key:
            file_key.write(key)

def get_key():
    with open (key_path, 'rb') as file_key:
        key = file_key.read()
        return key
    
def encrypt_files(file,filename):
    if not os.path.exists(encrypted_folder):
        os.makedirs(encrypted_folder)
    key = get_key()
    cipher = Fernet(key)
    data = file.read()
    encrypted_data = cipher.encrypt(data)
    encrypted_filename = str (uuid.uuid4().hex) + ".enc"
    write_filename_to_json(encrypted_Filename, filename)
    with open(os.path.join(encrypted_folder, encrypted_filename), 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    return encrypted_filename    

def decrypt_file(file_code):
    if not os.path.exists(decrypted_folder):
        os.makedirs(decrypted_folder)
    key = get_key()
    cipher = Fernet(key)
    with open(os.path.join(encrypted_folder, file_code), 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        decrypted_filename = get_filename_from_json(file_code)
        print(decrypted_filename)
        with open(os.path.join(decrypted_folder, decrypted_filename), 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
        return decrypted_filename