'''amundworks encryption library'''
# copyright (c) 2025 AmundWorks

def binary_encrypt():
    '''binary encoding module'''
    inputstr = input("plaintext:")
    tran = ''.join(format(ord(i), '08b') for i in inputstr)
    outputstr = ' '.join(tran[i:i+8] for i in range(0, len(tran), 8))
    print("binary: ",outputstr)  
def binary_decrypt():
    '''binary decoding module'''
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
    '''ceasar decryption module'''
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
    '''Vigenere cipher decryption module'''
    ciphertext = input("Enter ciphertext: ")
    key = input("Enter key: ")
    plaintext = ""

    key = key.lower()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char

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
def railfence_encrypt():
    plaintext = str(input("plaintext: "))
    key = int(input("key: "))
    pos = 0
    direction = 1
    rows = [[] for _ in range(key)]

    for char in plaintext:
        rows[pos].append(char)
    
        pos += direction
        if pos == 0 or pos == key - 1:
            direction *= -1
    
    ciphertext = ''.join([''.join(row) for row in rows])
    print("ciphertext:", ciphertext)
def railfence_decrypt():
    ciphertext = input("ciphertext: ")
    key = int(input("key: "))
    length = len(ciphertext)
    pattern = []
    pos = 0
    direction = 1
    for _ in range(length):
        pattern.append(pos)
        pos += direction
        if pos == 0 or pos == key - 1:
            direction *= -1

    counts = [pattern.count(r) for r in range(key)]
    rows = []
    index = 0
    for c in counts:
        rows.append(list(ciphertext[index:index + c]))
        index += c

    plaintext = ''
    row_pointers = [0] * key
    for r in pattern:
        plaintext += rows[r][row_pointers[r]]
        row_pointers[r] += 1

    print("plaintext:", plaintext)
def OTP_encrypt():
    '''One time pad encryption module'''
    inputstr = input("plaintext:")
    keystr = input("key:")
    bitext = ''.join(format(ord(i), '08b') for i in inputstr)
    bikey = ''.join(format(ord(i), '08b') for i in keystr)
    cipher = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(bitext, bikey))
    print("ciphertext in 8-bit groups:", ' '.join(cipher[i:i+8] for i in range(0, len(cipher), 8)))
def OTP_decrypt():
    '''One time pad decryption module'''
    inputstr = input("binary: ")
    keystr = input("key: ")
    bikey = ''.join(format(ord(i), '08b') for i in keystr)
    plaintext_bits = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(inputstr, bikey))
    tran = ''.join(chr(int(plaintext_bits[i:i+8], 2)) for i in range(0, len(plaintext_bits), 8))
    print("plaintext:", tran)