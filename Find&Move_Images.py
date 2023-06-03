import os
import shutil
import glob

def move_images_to_directory(source_directory, destination_directory):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Find all image files in the source directory and its subdirectories
    image_files = glob.glob(os.path.join(source_directory, '**/*.jpg'), recursive=True) + \
                  glob.glob(os.path.join(source_directory, '**/*.jpeg'), recursive=True) + \
                  glob.glob(os.path.join(source_directory, '**/*.png'), recursive=True) + \
                  glob.glob(os.path.join(source_directory, '**/*.gif'), recursive=True)

    # Move each image file to the destination directory
    moved_files_count = 0
    for image_file in image_files:
        # Get the relative path of the image file
        relative_path = os.path.relpath(image_file, source_directory)
        # Construct the destination path
        destination_path = os.path.join(destination_directory, os.path.basename(relative_path))
        # Create the destination directory if it doesn't exist
        os.makedirs(destination_directory, exist_ok=True)
        # Move the image file
        shutil.move(image_file, destination_path)
        moved_files_count += 1

    print(f"{moved_files_count} image(s) moved successfully!")

# Example usage
source_directory = 'PathToSource_Directory'  # Specify the source directory
destination_directory = 'PathToDestination_Directory'  # Specify the destination directory

move_images_to_directory(source_directory, destination_directory)
