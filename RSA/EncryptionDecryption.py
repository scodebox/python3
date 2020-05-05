from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def encrypt(msg):
	public_key = open('public_key.pem', 'r').read()
	rsa_key = RSA.importKey(public_key)
	rsa_key = PKCS1_OAEP.new(rsa_key)

	msg = bytes(msg, 'utf-8')

	cipher_text = rsa_key.encrypt(msg)
	cipher_text = base64.b64encode(cipher_text)
	return cipher_text

def decrypt(cipher_text):
	private_key = open('private_key.pem', 'r').read()
	rsakey = RSA.importKey(private_key)
	rsakey = PKCS1_OAEP.new(rsakey)

	cipher_text = base64.b64decode(cipher_text)
	plain_text = rsakey.decrypt(cipher_text)
	return plain_text.decode()

cipher = encrypt('Hello World!')
print(cipher)
plain = decrypt(cipher)
print(plain)
