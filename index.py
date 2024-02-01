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