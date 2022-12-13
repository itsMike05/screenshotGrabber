from datetime import datetime

import pyscreenshot as ImageGrab
import schedule
import time 

def take_screenshot():

    print("Taking screenshot...")
    screenshot_name = f"screenshot-{str(datetime.now())}"
    screenshot = ImageGrab.grab()
    filepath = f"./screenshots/{screenshot_name}.png"
    image_name = filepath.replace(":","")

    screenshot.save(image_name)

    print(f"Screenshot saved to {image_name}")

    return filepath

def main():

    seconds = input("Every how many seconds do you want to take a screenshot?")

    if int(seconds) == 0:
        print("Please enter a number")
    else:

        schedule.every(int(seconds)).seconds.do(take_screenshot)

        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    main()