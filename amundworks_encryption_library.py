
# AmundWorks Encryption Library | copyright (c) 2025 AmundWorks

def binary_encrypt():
    inputstr = input("plaintext:")
    tran = ''.join(format(ord(i), '08b') for i in inputstr)
    outputstr = ' '.join(tran[i:i+8] for i in range(0, len(tran), 8))
    print("binary: ",outputstr)  
def binary_decrypt():
    inputstr = input("binary: ")
    tran = ''.join(chr(int(b, 2)) for b in inputstr.split())
    print("plaintext: ", tran)
def csr_encrypt():
    '''caesar encryption module'''
    text = str(input("plaintext: "))
    newtext = ""
    x = int(input("shift? (1-26): "))
    for character in text:
        if character.isalpha():               
            pos = ord(character.lower()) - 96 
            newpos = (pos + x - 1) % 26 + 1   
            newchar = chr(newpos + 96)        
            newtext += newchar                
        else:                                
            newtext += character 
    print("ciphertext: ",newtext) 
def csr_decrypt():
    text = str(input("ciphertext: "))
    newtext = ""
    x = int(input("shift? (1-26): "))
    for character in text:
        if character.isalpha():               
            pos = ord(character.lower()) - 96
            newpos = (pos - x - 1) % 26 + 1   
            newchar = chr(newpos + 96)        
            newtext += newchar                
        else:                                 
            newtext += character              
    print("plaintext: ",newtext)  
def csr_bruteforce():
    '''brute force decryption module'''
    text = str(input("ciphertext: "))
    for shift in range(1, 26):  
        newtext = ""
        for character in text:
            if character.isalpha():
                pos = ord(character.lower()) - 96
                newpos = (pos - shift - 1) % 26 + 1  
                newchar = chr(newpos + 96)
                newtext += newchar
            else:
                newtext += character  
        print(f"Shift {shift}: {newtext}")
def vigenere_decrypt():
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
def vigenere_encrypt():
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