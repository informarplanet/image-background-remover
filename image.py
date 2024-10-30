#!/bin/python
# Author: DEADARMY
# Date: 30/10/2024
# Version: 2.1
# Description: Image background remover

import os
from PIL import Image
from rembg import remove
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def is_image_file(filename):
    valid_image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif', '.webp', '.avi', "avif"]
    return any(filename.lower().endswith(ext) for ext in valid_image_extensions)

def main():
    # Initialize tkinter and hide the main window
    Tk().withdraw()

    # Open file dialog for the user to select an image
    image_path = askopenfilename(title="Select an Image File", filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif *.webp *.avi *.avif")
    ])

    # Check if the user selected a file and if it's a valid image
    if not image_path or not is_image_file(image_path):
        print("Error: The selected file is not a valid image.")
        return

    try:
        # Load the image
        input_image = Image.open(image_path)

        # Remove the background
        output_image = remove(input_image)

        # Get user input for the new file name
        new_file_name = input("Please enter the name for the new image file (without extension): ")
        new_file_path = f"{new_file_name}.png"

        # Save the new image
        output_image.save(new_file_path)
        print(f"Background removed. The new image is saved as {new_file_path}.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
