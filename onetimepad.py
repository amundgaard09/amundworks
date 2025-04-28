#onetimepad decryption and encryption | copyright AWS 2025

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
    
    
OTP_encrypt()
OTP_decrypt()