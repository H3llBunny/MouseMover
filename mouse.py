import pyautogui as pag
import random
import time
import keyboard

def mouse_action():
    """
    Moves the mouse to a random position within a defined range,
    performs a scroll, and then clicks the left mouse button.
    """
    # Choose random coordinates in the given ranges
    x = random.randint(2500, 2600)
    y = random.randint(800, 900)

    # Move mouse smoothly to the new position (duration = 0.3s)
    pag.moveTo(x, y, duration=0.3)

    # Scroll down slightly
    pag.scroll(-100)

    # Perform a left mouse button click
    # pag.click()


def main():
    """
    Continuously monitors mouse activity.
    If the mouse is idle for longer than the threshold,
    it triggers mouse_action.
    """
    idle_threshold = 20  # seconds of inactivity before triggering
    last_pos = pag.position()  # starting mouse position
    last_move_time = time.time()  # last time the mouse moved

    print("Running... Press CTRL+ALT+Q to quit or close the terminal.")

    while True:
        if keyboard.is_pressed("ctrl+alt+q"):
            print("Exiting program...")
            break

        current_pos = pag.position()  # get current position

        # If the mouse was moved manually, reset timer
        if current_pos != last_pos:
            last_move_time = time.time()
            last_pos = current_pos

        # If idle time exceeds threshold, trigger auto movement
        if time.time() - last_move_time > idle_threshold:
            mouse_action()
            last_move_time = time.time()
            last_pos = pag.position()

        time.sleep(1)  # check every second

if __name__ == "__main__":
    main()