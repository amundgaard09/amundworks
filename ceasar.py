
while True:
    # MOO = Mode Of Operations
    MOO = int(input("Encrypt (1)\nKey Decrypt (2)\nBruteforce Decrypt (3)\nExit (4)"))
    # Program killer
    if MOO == 4:
        print("Goodbye!")
        break
    # Encryption Module
    if MOO == 1:
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
    # Key Decryption Module
    if MOO == 2:
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
    # Bruteforce Decryption Module
    if MOO == 3:
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