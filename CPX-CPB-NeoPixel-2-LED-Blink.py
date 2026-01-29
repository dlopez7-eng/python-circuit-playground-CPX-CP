import time
import board
from rainbowio import colorwheel
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

bounce_rainbow_demo = 1

def bounce_rainbow(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = (i * 8 + j) & 255
            pixels[i] = colorwheel(idx)
        pixels.show()
        time.sleep(wait)

    for j in range(255, 0, -1):
        for i in range(len(pixels)):
            idx = (i * 8 + j) & 255
            pixels[i] = colorwheel(idx)
        pixels.show()
        time.sleep(wait)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

while True:
    if bounce_rainbow_demo:
        bounce_rainbow(0.05)
