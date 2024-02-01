#biblioteki uzytkowe

from flask import Flask, request, send_file
from cryptography.fernet import Fernet
import os
import uuid
import json
from flask import send_from_directory