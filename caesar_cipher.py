"""Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher"""

# Every possible symbol that can be encrypted/decrypted:
# (!) You can add numbers and punctuation marks to encrypt those
# symbols as well.
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class CaesarCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                shift = ord('A')
                encrypted_char = chr((ord(char) - shift + self.key) % 26 + shift)
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, message):
        decrypted_message = ""
        for char in message:
            if char.isalpha():
                shift = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr((ord(char) - shift - self.key) % 26 + shift)
                decrypted_message += decrypted_char
            else:
                decrypted_message += char
        return decrypted_message


def get_user_mode():
    while True:  # Keep asking until the user enters e or d.
        print("Do you want to (e)ncrypt or (d)ecrypt?")
        response = input("> ").lower()

        if response.startswith("e"):
            return "encrypt"
        elif response.startswith("d"):
            return "decrypt"
        else:
            print("Please enter the letter 'e' or 'd'.")


def get_user_key():
    while True:  # Keep asking until the user enters a valid key.
        max_key = len(SYMBOLS) - 1
        print(f"Please enter the key (0 to {max_key}) to use.")
        response = input("> ")

        if not response.isdecimal():
            continue

        response = int(response)

        if 0 <= response <= max_key:
            return response


def main():
    mode = get_user_mode()  # Let the user enter if they are encrypting or decrypting
    key = get_user_key()  # Let the user enter the key to use

    coder = CaesarCipher(key)

    # Let the user enter the message to encrypt/decrypt
    print(f"Enter the message to {mode}.")
    message = input("> ").upper()  # Caesar cipher only works on uppercase letters

    if mode == "encrypt":
        # Stores the encrypted/decrypted form of the message
        translated = coder.encrypt(message)
    else:
        translated = coder.decrypt(message)

    # Display the encrypted/decrypted string to the screen
    print(translated)


if __name__ == "__main__":
    print("Caesar Cipher")
    print("The algorithm encrypts letters by shifting them over by a")
    print("key number. For example, a key of 2 means the letter A is")
    print("encrypted into C, the letter B encrypted into D, and so on.")
    print()

    while True:
        main()

        print("\n\nDo you want to run cipher one more time? Y or N")
        repeat = input("> ").lower()

        if repeat != "y":
            print("Thank you for using Caesar Cipher.")
            break
