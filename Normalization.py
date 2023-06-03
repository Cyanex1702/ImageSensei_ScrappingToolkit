import os
from PIL import Image

# Define the input and output directories
input_dir = 'PathToSource_Directory'  # Specify the input directory
output_dir = 'PathToDestination_Directory'  # Specify the output directory

# Define the target dimensions and number of channels
target_width, target_height, target_channels = 512, 512, 3

# Variables to track the number of images processed and rejected
num_images_processed = 0
num_images_rejected = 0

# Get the total number of images
image_files = [
    filename
    for filename in os.listdir(input_dir)
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg")
]
total_images = len(image_files)

# Loop over all the files in the input directory
for index, filename in enumerate(image_files):
    print(f"Processing image {index+1}/{total_images}: {filename}")
    num_images_processed += 1

    # Load the image
    image_path = os.path.join(input_dir, filename)
    image = Image.open(image_path)
    width, height = image.size
    channels = len(image.getbands())

    # Normalize the dimensions and number of channels
    if (width, height, channels) != (target_width, target_height, target_channels):
        # Resize the image to the target dimensions
        image = image.resize((target_width, target_height), resample=Image.LANCZOS)

        # Convert the image to RGB format if it has 1 or 4 channels
        if channels == 1 or channels == 4:
            image = image.convert("RGB")

        # Convert the image to 3 channels if it has more than 3 channels
        if channels > 3:
            r, g, b, *_ = image.split()
            image = Image.merge("RGB", (r, g, b))

        # Save the normalized image to the output directory
        output_path = os.path.join(output_dir, filename)

        # Convert the image to 'RGB' mode if it is in 'LA' mode
        if image.mode == 'LA':
            image = image.convert("RGB")

        image.save(output_path)
        # print("Image normalized and saved:", output_path)
    else:
        # Copy the image to the output directory
        output_path = os.path.join(output_dir, filename)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        os.link(image_path, output_path)
        # print("Image copied to output directory:", output_path)

# Print the summary
print("Image processing completed.")
print("Number of images processed:", num_images_processed)
print("Number of images rejected:", num_images_rejected)
