# Next to this python file, are a lot of images, all of them having the resolution of 64x64.
# They all end with _64.png
# This script will scale all of them to 48, 32, 24, and 16 pixels, and add them to the folder.

import os
from PIL import Image

# Define the resolutions to scale to
resolutions = [48, 32, 24, 16]

# Get the path to the directory containing the images
dir_path = os.path.dirname(os.path.realpath(__file__))

# Loop through all the files in the directory
for filename in os.listdir(dir_path):
    # Check if the file is a PNG image with the correct resolution
    if filename.endswith("_64.png"):
        # Open the image
        image_path = os.path.join(dir_path, filename)
        with Image.open(image_path) as im:
            # Loop through the resolutions to scale to
            for res in resolutions:
                # Calculate the new size of the image
                new_size = (res, res)
                # Scale the image
                scaled_im = im.resize(new_size)
                # Save the scaled image with the new filename
                new_filename = filename.replace("_64.png", f"_{res}.png")
                new_image_path = os.path.join(dir_path, new_filename)
                scaled_im.save(new_image_path)