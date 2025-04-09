


def binary_encrypt():
    inputstr = input("plaintext:")
    tran = ''.join(format(ord(i), '08b') for i in inputstr)
    outputstr = ' '.join(tran[i:i+8] for i in range(0, len(tran), 8))
    print("binary: ",outputstr)  
def binary_decrypt():
    inputstr = input("binary: ")
    tran = ''.join(chr(int(b, 2)) for b in inputstr.split())
    print("plaintext: ", tran)

while True:
    #moo = mode of operations
    MOO = int(input("encrypt (1)\ndecrypt (2)\nexit (3)\n:")) 
    #encrypter
    if MOO == 1:
        binary_encrypt()
    #decrypter
    elif MOO == 2:
        binary_decrypt()
    #exiter
    elif MOO == 3:
        print("Goodbye")
        break