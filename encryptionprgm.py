import string
import random

chars=" " + string.punctuation + string.ascii_letters + string.digits
chars=list(chars)
key=chars.copy()
random.shuffle(key)


plain_text=input("Enter a text to encrypt: ")
cipher_text=""
new_text=""

for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]

print(f"encrypted message:{cipher_text}")

enc=input("enter mssg to decrypt:")
for _ in enc:
    index=key.index(_)
    new_text+=chars[index]
print(f"decrypted msg:{new_text}")

