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

def get_filename_from_json(file_code):
    with open("filename.json", 'r') as file:
        json_data = json.load(file)
    if file_code in json_data:
        return json_data[file_code]
    
@app.route('/')
def send_report():
    return send_from_directory('./public', 'index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = file.filename
    encrypted_filename = encrypt_file(file, filename)
    return f'File "{filename}" uploaded and encrypted. File Code:{encrypted_filename}.'

@app.route('/download/<file_code>', methods=['GET'])
def download(file_code):
    decrypted_filename = decrypt_file(file_code)
    path_decrypted_file = os.path.join(decrypted_folder, decrypted_filename)
    return send_file(path_decrypted_file, as_attachment=True)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


if __name == '__main':
    key = generate_key()
    app.run()