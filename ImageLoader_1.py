# import sense_hat module
from sense_hat import SenseHat

# Create an instance (object) of the SenseHat() class called 'sense'
sense = SenseHat()

# Fix display orientation if neccessary
sense.set_rotation(180)

# Load image to sense hat LED matrix (image must be 8 pixels wide by 8 pixels tall)
# Use the load_image() method and supply the file path to the image as an argument
sense.load_image("golden_cross.png")
