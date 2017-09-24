from tabula_recta import tabula_recta, query
from create_key import key as key_text
from create_key import stripper
import conversions


class PolyAlphabeticCipher(object):
    def __init__(self, message="", ciphertext=""):
        self.key_init = key_text
        self.message = stripper(message)
        self.ciphertext = stripper(ciphertext)
        self.tab = tabula_recta

        key_list = []
        if self.message == "":
            for i in range(len(self.ciphertext)):
                key_list.append(self.key_init[i])
            self.key = ''.join(key_list)

        elif self.ciphertext == "":
            for i in range(len(self.message)):
                key_list.append(self.key_init[i])
            self.key = ''.join(key_list)
        
        

    def encode(self):
        ciphertext_list = []
        for i in range(len(self.message)):
            ciphertext_list.append(query(self.message[i], self.key[i]))
        self.ciphertext = ''.join(ciphertext_list)
        self.message = ""


    def decode(self):
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