from tkinter import *
from PIL import Image, ImageTk

def button_click():
    print("Button clicked!")

window = Tk()

window.geometry("420x420")
window.title("First GUI program")

# Attempt to open the image with error handling
try:
    image = Image.open('git.jpg')

except FileNotFoundError:
    print("Image file not found!")
except Exception as e:
    print(f"An error occurred: {e}")

# Resize the image to fit the window if needed
# image = image.resize((width, height), Image.ANTIALIAS)

# Convert the image to a PhotoImage
icon = ImageTk.PhotoImage(Image)

# Set window icon
window.iconphoto(True, icon)

window.config(background="#5cfcff")

# Create a button
button = Button(window, text="Click Me", command=button_click)
button.pack(pady=10)  # Add some padding around the button

window.mainloop()
