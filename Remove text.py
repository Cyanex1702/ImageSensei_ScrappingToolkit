import os
import pytesseract
from PIL import Image
import concurrent.futures

# Set the path to the folder containing images
image_folder = 'PathtoDirectory'

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
image_files = []
for root, dirs, files in os.walk(image_folder):
    for filename in files:
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_files.append(os.path.join(root, filename))
total_images = len(image_files)

# Define a function to process each image
def process_image(image_path):
    # Check if the image contains text
    if contains_text(image_path):
        # If the image contains text, remove it
        os.remove(image_path)
        removed_images.append(image_path)
        print(f"Removed {image_path} as it contains text.")
    else:
        print(f"{image_path} does not contain text.")

# Use threading to process images concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(process_image, image_files)

# Print the list of images that had text and were removed
print("\nImages that had text and were removed:")
for image_path in removed_images:
    print(image_path)
