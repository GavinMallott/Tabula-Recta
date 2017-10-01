import re


def write_key_file(x):
    key_file = open("key.txt", 'w+')
    key_file.write(x)
    key_file.close()

def read_key_file():
    key_file = open("key.txt", 'r+')
    key_text = key_file.read()
    key_file.close()
    return key_text

def stripper(text):
    key_text = text
    key_text = re.sub('[\s+\d+\W+]', '', key_text)
    key = key_text.upper()
    return key

key = stripper(read_key_file())


if __name__ == '__main__':
    print(key)