import random
import string
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

# Get input
plaintext = input("Enter a message to encrypt: ")

# Encrypt (symmetric)
ciphertext = ""
for letter in plaintext:
    index = chars.index(letter)
    ciphertext += key[index]

# Decrypt (symmetric)
decrypted = ""
for letter in ciphertext:
    index = key.index(letter)
    decrypted += chars[index]

print("\n--- Symmetric (Substitution Cipher) ---")
print(f"Original message : {plaintext}")
print(f"Encrypted message: {ciphertext}")
print(f"Decrypted message: {decrypted}")


# Asymmetric Encryption (RSA)


# Generate RSA keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Encrypt (asymmetric)
asym_cipher = public_key.encrypt(
    plaintext.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt (asymmetric)
asym_plain = private_key.decrypt(
    asym_cipher,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
).decode()

print("\n--- Asymmetric (RSA) ---")
print(f"Original message : {plaintext}")
print(f"Encrypted message: {asym_cipher}")  
print(f"Decrypted message: {asym_plain}")
