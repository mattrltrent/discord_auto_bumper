import time
import pyautogui
import random

print("Welcome to the Discord auto-bumper.")
print("Developed by Matthew Trent (matthewtrent.me).")
print("Press Ctrl+C or Cmd+C to exit anytime.")
print("\n")


def countdown():
    for i in reversed(range(1, 6)):
        print(i)
        time.sleep(1)


def main():
    input("Press any key + enter to begin... (will start spamming in 5 seconds): ")
    countdown()
    while True:
        pyautogui.typewrite("/bump")
        time.sleep(5)  # allow for discord to realize the command
        pyautogui.press('enter')  # Two "enters" are required to send commands
        pyautogui.press('enter')  # Two "enters" are required to send commands
        # 2 hours + random number of seconds between 50 and 250
        time.sleep(60 * 60 * 2 + random.randint(50, 250))


main()
