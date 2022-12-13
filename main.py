from datetime import datetime

import pyscreenshot as ImageGrab


def take_screenshot():

    screenshot_name = f"screenshot-{str(datetime.now())}.png"
    screenshot = ImageGrab.grab()
    filepath = f"./screenshots/{screenshot_name}"
    screenshot.save(filepath)

    return filepath


def main():



