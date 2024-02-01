from flask import Flask, request, send_file
from cryptography.fernet import Fernet
import os
import uuid
import json
from flask import send_from_directory

app = Flask(__name__)
encrypted_folder = "encrypted_files/"
decrypted_folder = "decrypted_files/"
filename_path = "./filename.json"
key_path = "./key.txt"

def write_filename_to_json(encrypted_filename, filename):
    new_data = {
        encrypted_filename : filename
    }
    data = {}
    if os.path.exists(filename_path):
        with open('filename.json', 'r') as file:
            data = json.load(file)
    data.update(new_data)
    with open("filename.json", "w") as write_file:
        json.dump(data, write_file)