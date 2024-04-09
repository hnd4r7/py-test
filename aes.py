import base64
from ctypes import c_void_p
import hashlib

from Crypto import Random
from Crypto.Cipher import AES

block_size = 16
pad = lambda s: s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)
unpad = lambda s: s[0:-ord(s[-1:])]
iv = Random.new().read(AES.block_size) # Random IV

def get_private_key(secret_key, salt):
    return hashlib.pbkdf2_hmac('SHA256', secret_key.encode(), salt.encode(), 65536, 32)

def encrypt_with_AES(message, secret_key, salt):
    private_key = get_private_key(secret_key, salt)
    message = pad(message)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    cipher_bytes = base64.b64encode(iv + cipher.encrypt(message.encode("utf8")))
    return bytes.decode(cipher_bytes)

def decrypt_with_AES(encoded, secret_key, salt):
    private_key = get_private_key(secret_key, salt)
    cipher_text = base64.b64decode(encoded)
    iv = cipher_text[:AES.block_size]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    plain_bytes = unpad(cipher.decrypt(cipher_text[block_size:]))
    return bytes.decode(plain_bytes)

secret_key = "F2384D7E023B43BDBC5F1CDC356DBB40"
salt = "47B040DEBE3B4D6A8769BEAD2A4419DC"
plain_text = "M0993000353"
# cipher = encrypt_with_AES(plain_text, secret_key, salt)
# print("Cipher: " + cipher)
cipher = "oJpQsjNutFGKPnhbAYOrVfaODjWuw0Kl/qZTcXGMP+k="

decrypted = decrypt_with_AES(cipher, secret_key, salt)
print("Decrypted " + decrypted)