import conversions
import binary_operands
from tabula_recta import tablula_recta
from create_key import key as key_bulk


message = "TIMISABADBLADELOCK"


def query(plaintext, key):
    x = int(conversions.ascii_to_decimal(key)) - 65
    y = int(conversions.ascii_to_decimal(plaintext)) - 65
    l = tablula_recta[x][y]
    return l


def splice_key(message):
    key = []
    for i in range(len(message)):
        key.append(key_bulk[i])
    return ''.join(key)


def create_ciphertext(message, key):
    ciphertext = []
    for i in range(len(message)):
        ciphertext.append(query(message[i], key[i]))
    return ''.join(ciphertext)


def encode(message):
    return create_ciphertext(message, splice_key(message))
    
print(encode(message))


def decode(ciphertext):
    i = 0
    nums = []
    message = []
    key = splice_key(ciphertext)
    for number in key:
        x = int(conversions.ascii_to_decimal(number)) - 65
        letter = tablula_recta[x].index(ciphertext[i])
        nums.append(letter)
        i += 1

    for num in nums:
        letter = conversions.decimal_to_ascii(num+65)
        message.append(letter)
    return ''.join(message)

print(decode(encode(message)))