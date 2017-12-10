# import sense_hat module
from sense_hat import SenseHat
import time
# Create an instance (object) of the SenseHat() class called 'sense'
sense = SenseHat()

# Fix display orientation if neccessary
sense.set_rotation(180)

continueRunning = True

# Create a function to load an image
def imageLoader():
    # Get the image name and/or path from user (example: santa.png)
    image_path = input("Enter image name/path: ")
    # Load the desired image into the sense hat LED matrix
    sense.load_image(image_path)

# Create a function that asks the user what the application
# should do (load image, exit, etc...)
def userSelection():
    print()
    print("MAD-HAX SenseHat Image Loader")
    print("-----------------------------")
    print("Type -i to load an image or -q to quit.")
    print()
    userInput = input(": ")
    # return the value so that it can be assigned to a variable, used in a
    # conditional, or both
    return userInput


# Load image to sense hat LED matrix (image must be 8 pixels wide by 8 pixels tall)
# Use the load_image() method and supply the file path to the image as an argument

# Create an infinite loop so that the user can change the image repeatedly.
# This loop effectively represts the life of the application. Only if this loop
# is broken will the application exit (or by pressing Ctrl+C to force quit the
# program
while(True):
    userInput = userSelection()
    if(userInput == "-i"):
        # If the user chose to load an image, call the imageLoader function
        # If a user enters a filename that doesn't exist the program will
        # throw an "exception" and exit. In order to make this program more stable
        # we will use a 'try' to run the function and 'catch' and exceptions thrown
        # using a try/catch block. This way we can simply inform the user that
        # the file does not exist and to try again, rather than the program
        # crashing.
        try:
            # Try to execute the imageLoader function
            imageLoader()
        except Exception:
            # This code runs ONLY if the imageLoader function threw an
            # exception (an error) inform the user of the most likely cause
            # of the error:
            print()
            print("Error: File does not exist!")
            print()
    elif(userInput == "-q"):
        # If the user chose to quit, send a goodbye message and break the loop.
        # Remember that this loop represents the runtime of the program.
        # Breaking this loop will result in the completion of the code and
        # thus the application will end/exit.
        print("Exiting application, Goodbye.")
        break
    else:
        # Inform the user that the input was invalid and repeat the loop
        print()
        print("Error: Invalid input!")
        print()
