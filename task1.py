def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.

    Parameters:
        text (str): The input text to be encrypted or decrypted.
        shift (int): The number of positions to shift the characters.
        mode (str): Either 'encrypt' to encrypt the text or 'decrypt' to decrypt the text.

    Returns:
        str: The encrypted or decrypted text.
    """
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char

    return result

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    if choice not in ['e', 'd']:
        print("Invalid choice!")
        return

    text = input("Enter your message: ").strip()
    shift = int(input("Enter the shift value: ").strip())

    if choice == 'e':
        encrypted_text = caesar_cipher(text, shift, mode='encrypt')
        print(f"Encrypted message: {encrypted_text}")
    else:
        decrypted_text = caesar_cipher(text, shift, mode='decrypt')
        print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()