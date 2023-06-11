import os
from PIL import Image
import imagehash

def remove_duplicates(directory):
    image_hashes = {}
    duplicate_images = []

    total_images = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                total_images += 1

    current_image = 1
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                image_path = os.path.join(root, filename)
                try:
                    image = Image.open(image_path)
                    image_hash = imagehash.average_hash(image)
                    if image_hash in image_hashes:
                        duplicate_images.append((image_path, image_hashes[image_hash]))
                    else:
                        image_hashes[image_hash] = image_path
                    print(f"Processed image {current_image}/{total_images}: {image_path}")
                    current_image += 1
                except Exception as e:
                    print(f"Error processing {image_path}: {e}")

    for image_path, duplicate_path in duplicate_images:
        os.remove(duplicate_path)
        print(f"Removed duplicate: {duplicate_path}")
        print(f"Kept: {image_path}")

    print("Duplicate removal process completed.")

# Provide the path to your image directory
directory_path = 'PathtoDirectory'  # Specify the path to the directory containing images

remove_duplicates(directory_path)
