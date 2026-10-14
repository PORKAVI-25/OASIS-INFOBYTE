import secrets
import string

def generate_password(length, use_digits=True, use_symbols=True):
    if length < 1:
        raise ValueError("Length must be at least 1.")

    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    return "".join(secrets.choice(characters) for _ in range(length))

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Password length: "))
        digits = input("Include numbers? (y/n): ").strip().lower() == "y"
        symbols = input("Include symbols? (y/n): ").strip().lower() == "y"
        print("Generated password:", generate_password(length, digits, symbols))
    except ValueError as error:
        print("Input error:", error)

if __name__ == "__main__":
    main()
