# import sense_hat module
from sense_hat import SenseHat
import time
# Create an instance (object) of the SenseHat() class called 'sense'
sense = SenseHat()

# Fix display orientation if neccessary
sense.set_rotation(180)

# Load image to sense hat LED matrix (image must be 8 pixels wide by 8 pixels tall)
# Use the load_image() method and supply the file path to the image as an argument

# Create an infinite loop so that the user can change the image repeatedly.
# Press Ctrl+C to quit the application
while(True):
    # Get the image name and/or path from user (example: santa.png)
    image_path = input("Enter image name/path: ")
    # Load the desired image into the sense hat LED matrix
    sense.load_image(image_path)
