"""
Project 2: Basic Encryption & Decryption (Caesar Cipher)
DecodeLabs - Cyber Security Industrial Training Kit

Goal: Implement a simple encryption and decryption technique.
- Encrypt user text using a basic logic (Caesar cipher)
- Decrypt the encrypted text
- Display both encrypted and decrypted output
"""


def encrypt(text: str, shift: int) -> str:
    """Encrypt text using a Caesar cipher shift."""
    result = ""
    shift = shift % 26  # normalize shift in case user enters >26 or negative
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Leave spaces, punctuation, numbers, symbols unchanged
            result += char
    return result


def decrypt(text: str, shift: int) -> str:
    """Decrypt Caesar cipher text by reversing the shift."""
    return encrypt(text, -shift)


def get_shift_key() -> int:
    """Prompt the user for a valid integer shift key."""
    while True:
        try:
            return int(input("Enter shift key (e.g. 3): ").strip())
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def run_demo():
    """Interactive command-line demo of the Caesar cipher."""
    print("=" * 50)
    print("  CAESAR CIPHER - Encryption & Decryption Tool")
    print("=" * 50)

    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Encrypt then decrypt (verify round-trip)")
        print("4. Exit")
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            text = input("Enter text to encrypt: ")
            shift = get_shift_key()
            print(f"\nOriginal Text : {text}")
            print(f"Encrypted Text: {encrypt(text, shift)}")

        elif choice == "2":
            text = input("Enter text to decrypt: ")
            shift = get_shift_key()
            print(f"\nEncrypted Text: {text}")
            print(f"Decrypted Text: {decrypt(text, shift)}")

        elif choice == "3":
            text = input("Enter your message: ")
            shift = get_shift_key()
            encrypted = encrypt(text, shift)
            decrypted = decrypt(encrypted, shift)
            print(f"\nOriginal Text : {text}")
            print(f"Encrypted Text: {encrypted}")
            print(f"Decrypted Text: {decrypted}")
            match = "YES ✅" if decrypted == text else "NO ❌"
            print(f"Matches original: {match}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    run_demo()
