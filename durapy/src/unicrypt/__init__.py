"""
The `DuraPy` `UniPy` `UniCrypt` module.
This module contains all the encryption and decryption functions of the `DuraPy` library.
These include methods such as binary, ceasar, vigenere, railfence and OTP with encryption and decryption for all cryptography methods.
"""

from .unicrypt import (
    binary_encrypt, binary_decrypt,
    ceasar_encrypt, ceasar_decrypt,
    vigenere_encrypt, vigenere_decrypt,
    railfence_encrypt, railfence_decrypt,
    otp_encrypt, otp_decrypt
)

__all__ = [
    "binary_encrypt", "binary_decrypt",
    "ceasar_encrypt", "ceasar_decrypt",
    "vigenere_encrypt", "vigenere_decrypt",
    "railfence_encrypt", "railfence_decrypt",
    "otp_encrypt", "otp_decrypt"
]
