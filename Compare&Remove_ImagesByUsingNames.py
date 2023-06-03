import os

source_directory = 'PathToSource_Directory'  # Specify the source directory
destination_directory = 'PathToDestination_Directory'  # Specify the destination directory

# Get the list of files in the source directory
source_files = os.listdir(source_directory)

# Get the list of files in the destination directory
destination_files = os.listdir(destination_directory)

total_images_before = len(destination_files)
removed_images = []

# Iterate over the files in the destination directory
for file_name in destination_files:
    if file_name not in source_files:
        removed_images.append(file_name)
        file_path = os.path.join(destination_directory, file_name)
        os.remove(file_path)

total_images_after = total_images_before - len(removed_images)

# Print the removed images and statistics
print("Removed images:")
for image_name in removed_images:
    print(image_name)

print("\nTotal images before: ", total_images_before)
print("Total images after: ", total_images_after)
