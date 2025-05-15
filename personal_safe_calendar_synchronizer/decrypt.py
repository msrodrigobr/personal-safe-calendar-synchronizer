import hashlib
import json
import os
from base64 import b64encode, b64decode

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def decrypt_json_simple(encrypted: dict, password: str) -> dict:
    iv = b64decode(encrypted["iv"])
    ciphertext = b64decode(encrypted["data"])
    key = hashlib.sha256(password.encode()).digest()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    json_bytes = unpadder.update(padded_data) + unpadder.finalize()
    return json.loads(json_bytes.decode('utf-8'))