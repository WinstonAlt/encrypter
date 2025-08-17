import webbrowser
from cryptography.fernet import Fernet

# ---------- LINKS ----------
def open_links():
    # Open https link
    webbrowser.open("https://example.com")   # 👈 replace with your site

# ---------- ENCRYPTION ----------
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved to secret.key")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = f.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

    print(f"[+] File '{filename}' encrypted to '{filename}.enc'")

def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted = f.decrypt(encrypted_data)

    original_name = filename.replace(".enc", "")
    with open(original_name, "wb") as file:
        file.write(decrypted)

    print(f"[+] File '{filename}' decrypted to '{original_name}'")

# ---------- MAIN ----------
if __name__ == "__main__":
    # 🚀 Always open website on startup
    open_links()

    print("1) Generate key")
    print("2) Encrypt file")
    print("3) Decrypt file")
    choice = input("Select option: ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        fname = input("Enter filename to encrypt: ")
        encrypt_file(fname)
    elif choice == "3":
        fname = input("Enter filename to decrypt: ")
        decrypt_file(fname)
    else:
        print("Invalid choice")
