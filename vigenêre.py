
# Vigenère cipher

def decrypt_vigenere():
    '''vigenere cipher decryption module'''
    ciphertext = str(input("Enter ciphertext: "))
    key = str(input("Enter key: "))
    plaintext = ""

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                plaintext += chr((ord(ciphertext[i]) - ord(key[i % len(key)].upper()) + 26) % 26 + ord("A"))
            else:
                plaintext += chr((ord(ciphertext[i]) - ord(key[i % len(key)].lower()) + 26) % 26 + ord("a"))
        else:
            plaintext += ciphertext[i]
    print("Plaintext:", plaintext)
def encrypt_vigenere():
    '''vigenere cipher encryption module'''
    ciphertext = str(input("Enter ciphertext: "))
    key = str(input("Enter key: "))
    plaintext = ""

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                plaintext += chr((ord(ciphertext[i]) - ord(key[i % len(key)].upper()) + 26) % 26 + ord("A"))
            else:
                plaintext += chr((ord(ciphertext[i]) - ord(key[i % len(key)].lower()) + 26) % 26 + ord("a"))
        else:
            plaintext += ciphertext[i]
    print("Plaintext:", plaintext)
while True:
    moo = int(input("1. Encrypt\n2. Decrypt\nChoose mode of operation: "))
    if moo == 1:
        encrypt_vigenere()
    elif moo == 2:
        decrypt_vigenere()

           