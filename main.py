import pyautogui as pag
from time import sleep
import keyboard as kb

MIN_SIMILARITY = .9


def click_emoji():
    sleep(.5)
    emoji = pag.locateOnScreen("emoji.png", confidence=MIN_SIMILARITY)
    sleep(.5)
    if emoji:
        pag.click(emoji)


def click_stickers():
    sleep(.5)
    stickers = pag.locateOnScreen("stickers.png", confidence=MIN_SIMILARITY)
    sleep(.5)
    if stickers:
        pag.click(stickers)


def click_sticker():
    sleep(.01)
    sticker = pag.locateOnScreen("sticker.png", confidence=MIN_SIMILARITY)
    sleep(.01)
    if sticker:
        pag.click(sticker)


if __name__ == "__main__":
    stop_script = False
    sleep(3)
    click_emoji()
    sleep(1.5)
    click_stickers()
    sleep(1.5)

    while not stop_script:
        sleep(.01)
        if kb.is_pressed("c"):
            stop_script = True
        click_sticker()
        sleep(.01)
