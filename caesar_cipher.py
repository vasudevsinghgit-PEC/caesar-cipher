"""
Caesar Cipher
A command-line program for encoding and decoding messages with a Caesar shift.
"""


def print_banner():
    print(r"""
  CCCCC      AAAAA     EEEEEEE      SSSSS        AAAAA      RRRRR
 C          A     A    E           S           A     A     R    R
 C          AAAAAAA    EEEEE        SSSSS       AAAAAAA     RRRRR
 C          A     A    E                S      A     A     R   R
  CCCCC     A     A    EEEEEEE      SSSSS       A     A     R    R


  CCCCC  IIIIIII    PPPPPP   H   H   EEEEEEE   RRRRR
 C          I       P    P   H   H   E         R    R
 C          I       PPPPPP   HHHHH   EEEEE     RRRRR
 C          I       P        H   H   E         R   R
  CCCCC  IIIIIII    P        H   H   EEEEEEE   R    R
""")
    print("       >>> ENCRYPT. DECRYPT. CONQUER. <<<\n")


def caesar(original_text, shift_amount, direction):
    """Return the message encoded or decoded with a Caesar shift."""
    if direction == "decode":
        shift_amount = -shift_amount

    result = []

    for character in original_text:
        if character.isascii() and character.isalpha():
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if character.isupper() else "abcdefghijklmnopqrstuvwxyz"
            old_index = alphabet.index(character)
            new_index = (old_index + shift_amount) % 26
            result.append(alphabet[new_index])
        else:
            # Preserve spaces, punctuation, digits, and other characters.
            result.append(character)

    return "".join(result)


def get_shift():
    """Ask for an integer shift, retrying if the input is invalid."""
    while True:
        try:
            return int(input("Enter the shift number: ").strip())
        except ValueError:
            print("Please enter a whole number, such as 3 or 12.")


def main():
    print_banner()

    while True:
        start = input(
            "Do you want to start encryption or decryption? (yes/no): "
        ).strip().lower()

        if start in ("no", "n"):
            print("Thanks for using Caesar Cipher. Goodbye!")
            break
        if start not in ("yes", "y"):
            print("Please enter yes or no.")
            continue

        while True:
            direction = input(
                "Type 'encode' to encrypt or 'decode' to decrypt: "
            ).strip().lower()
            if direction in ("encode", "decode"):
                break
            print("Invalid choice. Please type encode or decode.")

        message = input("Type your message: ")
        shift = get_shift()

        result = caesar(message, shift, direction)
        action = "encoded" if direction == "encode" else "decoded"

        print(f"\nYour {action} message is: {result}\n")


if __name__ == "__main__":
    main()
