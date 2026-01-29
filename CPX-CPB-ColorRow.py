import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3, auto_write=False)

RED = (255, 0, 0)       # This is full red, no green or blue
GREEN = (0, 255, 0)     # This is full green, no red or blue
BLUE = (0, 0, 255)      # This is full blue, no red or green
OFF = (0, 0, 0)         # This turns the LED off completely


while True:                            # while ture is loop to keep running this code on repeat
    # Turn each LED red one by one
    for i in range(10):                # Loop through LED numbers 0 to 9
        pixels[i] = RED                # Set the current LED to red
        pixels.show()                  # Update the board so the color actually lights up
        time.sleep(0.2)                # Wait a little so you can see each LED lighting up

    # Turn each LED green one by one
    for i in range(10):                
        pixels[i] = GREEN              # Set the current LED to green
        pixels.show()                  
        time.sleep(0.2)                

    # Turn each LED blue one by one
    for i in range(10):                
        pixels[i] = BLUE               # Set the current LED to blue
        pixels.show()                  
        time.sleep(0.2)                

    # Turn each LED off one by one
    for i in range(10):                
        pixels[i] = OFF                # Set the current LED to off
        pixels.show()                  
        time.sleep(0.2)                
