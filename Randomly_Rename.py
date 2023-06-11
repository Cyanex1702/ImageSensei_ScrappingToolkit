import os
import glob
import random
import string
import shutil

def rename_images(directory):
    count = 0  # Counter for renamed files
    # Iterate over all files and subdirectories within the main directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            # Check if the file is an image (modify the extensions as needed)
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Generate a unique random name for the file
                new_filename = generate_random_name() + os.path.splitext(filename)[1]
                new_file_path = os.path.join(root, new_filename)
                # Rename the file
                shutil.move(file_path, new_file_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
                count += 1  # Increment the counter
    print(f"Total files renamed: {count}")

def generate_random_name(length=8):
    # Generate a random name using lowercase letters and digits
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

# Specify the main directory path
main_directory = 'PathtoDirectory'

# Call the function to rename the image files
rename_images(main_directory)
