"""
Tabula Recta
--Polyalphabetic Cipher Object--

Author: Gavin Mallott
Created: July 20, 2017
Lasted Edited: October 24, 2017
Last Edit: Adding docstrings/annotations
"""


from tr_table import tabula_recta, query
from create_key import key as key_text
from create_key import stripper
import conversions


class PolyAlphabeticCipher(object):
    """Object that controls the encryption, decryption, and key management for a poly-alphabetic, running key cipher"""

    def __init__(self, message="", ciphertext=""):
        """
        Initializes the object by passing an optional message or ciphertext, 
        generates basic class variables, 
        and creates the key based on the data in key.txt
        """

        self.key_init = key_text
        self.message = stripper(message)
        self.ciphertext = stripper(ciphertext)
        self.tab = tabula_recta

        key_list = []
        if self.message == "":
            for x, i in enumerate(self.ciphertext):
                key_list.append(self.key_init[i])
            self.key = ''.join(key_list)

        elif self.ciphertext == "":
            for x, i in enumerate(self.message):
                key_list.append(self.key_init[i])
            self.key = ''.join(key_list)
        

    def encode(self):
        """Sets self.ciphertext by encrypting self.message using the Tabula Recta and self.key, and sets self.message to ''"""
        ciphertext_list = []
        for i in range(len(self.message)):
            ciphertext_list.append(query(self.message[i], self.key[i]))
        self.ciphertext = ''.join(ciphertext_list)
        self.message = ""


    def decode(self):
        """Sets self.message by decrypting self.ciphertext with the Tabula Recta and self.key, and sets self.ciphertext to ''"""

        i = 0
        nums = []
        bob = []
        for number in self.key:
            x = int(conversions.ascii_to_decimal(number)) - 65
            letter = tabula_recta[x].index(self.ciphertext[i])
            nums.append(letter)
            i += 1

        for num in nums:
            letter = conversions.decimal_to_ascii(num+65)
            bob.append(letter)
        self.message = ''.join(bob)
        self.ciphertext = ""


if __name__ == "__main__":

    code = PolyAlphabeticCipher(message="LUCIANISAGOODCHAMPION")
    fred = PolyAlphabeticCipher(ciphertext="SLKDJGLSDKJG")
    
    fred.decode()
    print(fred.message)


    """
    print(code.message)
    code.encode()
    print(code.ciphertext)
    print(code.message)
    code.decode()
    print(code.message)
    """
