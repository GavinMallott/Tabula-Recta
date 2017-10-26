"""
Tabula Recta
--Basic GUI conroller--

Author: Gavin Mallott
Created: July 21, 2017
Lasted Edited: October 24, 2017
Last Edit: Adding docstrings/annotations
"""


from poly_alpha_cipher import PolyAlphabeticCipher as PAC
from create_key import write_key_file


def create_code():
    """Initializes PAC object message with user input and returns the encrypted object"""

    message = input("Type your secret message: ")
    code = PAC(message=message)
    code.encode()
    return code


def decipher_code():
    """Initializes PAC object ciphertext using user input and returns the decrypted object"""

    ciphertext = input("Input the ciphertext you wish to decode: ")
    code = PAC(ciphertext=ciphertext)
    code.decode()
    return code


def main():
    """Basic GUI controlling the encyption and decryption process"""

    print("What do you want to do?\n")
    choice = int(input("1.) Create a secret code\n2.) Decipher an ecrypted message\n3.) Create a new key\n\n> "))

    if choice == 1:
        print(create_code().ciphertext)
    elif choice == 2:
        print(decipher_code().message)
    elif choice == 3:
        write_key_file(input("Input new key: "))
    

if __name__ == "__main__":
    main()
