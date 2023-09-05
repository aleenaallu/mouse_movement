import logging
from pynput import mouse ,keyboard

# Configure logging
logging.basicConfig(filename='mouse_activity.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Mouse movement event handler
def on_move(x, y):
    logging.info(f"Mouse moved to ({x}, {y})")

# Mouse click event handler
def on_click(x, y, button, pressed):
    action = "Pressed" if pressed else "Released"
    if button == mouse.Button.left:
        button_name = "Left"
    elif button == mouse.Button.right:
        button_name = "Right"
    else:
        button_name = "Unknown"
    logging.info(f"Mouse {action} {button_name} button at ({x}, {y})")

# Mouse scroll event handler
def on_scroll(x, y, dx, dy):
    logging.info(f"Mouse scrolled at ({x}, {y}), delta: ({dx}, {dy})")

    
# Keyboard event handler
def on_key_release(key):
    if key == keyboard.Key.esc:
        # Stop the mouse listener
        mouse_listener.stop()
        # Stop the keyboard listener
        return False
# Set up the listener
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(on_key_release=on_key_release)
# with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
#     listener.join()

# Start both listeners
mouse_listener.start()
keyboard_listener.start()

# Join the listeners
mouse_listener.join()
keyboard_listener.join()
