from poly_alpha_cipher import PolyAlphabeticCipher as PAC


def create_code():
    message = input("Type your secret message: ")
    code = PAC(message=message)
    code.encode()
    return code


def decipher_code():
    ciphertext = input("Input the ciphertext you wish to decode: ")
    code = PAC(ciphertext=ciphertext)
    code.decode()
    return code


def main():
    print("Greetings, and welcome to the improved encryption application.")
    print("What do you want to do?\n")
    choice = int(input("1.) Create a secret code\n2.) Decipher an ecrypted message\n\n> "))

    if choice == 1:
        print(create_code().ciphertext)
    elif choice == 2:
        print(decipher_code().message)


if __name__ == "__main__":
    main()