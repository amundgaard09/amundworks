
# Vigenère cipher

while True:

    moo = int(input("1. Encrypt\n2. Decrypt\nChoose mode of operation: "))
    
    if moo == 1:

        plaintext = str(input("Enter plaintext: "))
        key = str(input("Enter key: "))
        ciphertext = ""

        for i in range(len(plaintext)):
            if plaintext[i].isalpha():
                if plaintext[i].isupper():
                    ciphertext += chr((ord(plaintext[i]) + ord(key[i % len(key)].upper()) - 2 * ord("A")) % 26 + ord("A"))
                else:
                    ciphertext += chr((ord(plaintext[i]) + ord(key[i % len(key)].lower()) - 2 * ord("a")) % 26 + ord("a"))
            else:
                ciphertext += plaintext[i]
                
        print("Ciphertext:", ciphertext)

    elif moo == 2:

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
            