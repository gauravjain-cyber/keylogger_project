from cryptography.fernet import Fernet, InvalidToken

log_file = "logs/keylogs.txt"
key_file = "secret.key"

with open(key_file, "rb") as f:
    key = f.read()

cipher = Fernet(key)

print("\nDecrypted Logs\n")

with open(log_file, "rb") as f:
    for line in f:

        try:
            decrypted = cipher.decrypt(line.strip())
            print(decrypted.decode())

        except InvalidToken:
            continue
