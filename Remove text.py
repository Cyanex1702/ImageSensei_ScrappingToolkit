import os
import pytesseract
from PIL import Image

# Set the path to the folder containing images
image_folder = 'PathToDirectory'

# Set the path to the Tesseract executable (change it if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Function to check if an image contains text
def contains_text(image_path):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Convert the image to grayscale for better OCR accuracy
    image = image.convert('L')

    # Use PyTesseract to perform OCR on the image
    text = pytesseract.image_to_string(image)

    # Check if any text was detected
    if text.strip():
        return True
    else:
        return False


# Initialize a list to store the names of images that had text
removed_images = []

# Count the total number of images
total_images = len([filename for filename in os.listdir(image_folder)
                    if filename.endswith(('.jpg', '.jpeg', '.png'))])

# Iterate through the images in the folder
for index, filename in enumerate(os.listdir(image_folder), start=1):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(image_folder, filename)

        # Check if the image contains text
        if contains_text(image_path):
            # If the image contains text, remove it
            os.remove(image_path)
            removed_images.append(filename)
            print(f"Removed {filename} as it contains text. ({index}/{total_images})")
        else:
            print(f"{filename} does not contain text. ({index}/{total_images})")

# Print the list of images that had text and were removed
print("\nImages that had text and were removed:")
for image_name in removed_images:
    print(image_name)
