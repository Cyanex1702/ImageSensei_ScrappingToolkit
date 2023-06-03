# ImageSensei - Advanced Image Scraping Toolkit

ImageSensei is a comprehensive and user-friendly image scraping toolkit designed to simplify the process of gathering, organizing, and enhancing image collections. With its powerful features, ImageSensei empowers researchers, developers, and data enthusiasts to efficiently extract and manipulate images from various sources.

## Key Features
1. Image Scraping: Effortlessly scrape images from various online sources by specifying search queries, enabling efficient data collection without manual intervention.

2. Multi-threaded Image Scraping: Accelerate the scraping process by utilizing multi-threading, allowing simultaneous execution of multiple search queries for faster results.

3. Remove Duplicate Images: Eliminate duplicate images from your collection automatically, optimizing storage space and ensuring a clean and clutter-free dataset.

4. Text Detection and Removal: Automatically identify and remove images with text overlays, providing a text-free image collection suitable for visual analysis or machine learning tasks.

5. Image Normalization: Standardize your image dataset by adjusting key attributes such as brightness, contrast, and saturation. This process ensures consistent visual quality and enhances the usability of the images for downstream applications.

6. Uniquely Image Renaming: Easily rename images from multiple directories to ensure unique names, avoiding naming conflicts and improving organization. This feature saves time and effort by automatically handling naming conventions and ensuring each image has a distinct identifier.

## Getting Started
1. Clone the repository:

```bash
git clone https://github.com/Cyanex1702/ImageSensei_ScrappingToolkit.git
```

2. Download the requirements:

```bash
pip install -r requirements.txt
```
## Download and install Tesseract OCR:
### You need to download Tesseract OCR for Removing Text Images.
1.For Windows: Download the Tesseract installer from the official GitHub repository: 
```bash
https://github.com/UB-Mannheim/tesseract/wiki
```
Follow the installation instructions provided.

2. For Linux: Install Tesseract using your package manager. For example, on Ubuntu, run the following command:
```bash
sudo apt-get install tesseract-ocr
```
# Documentation
A collection of code snippets for various image-related tasks including image downloading, moving images, normalizing images, and removing duplicate images. These code snippets are designed to simplify the process of working with image datasets.

### Simple_ImageScrapper.py & Advance_ImageScrapper.py
This code uses the bing_image_downloader library to download images from Bing search engine based on a list of queries.
It allows you to specify the maximum number of images to download per query.
The downloaded images are saved in separate directories based on the query name.
Non-JPEG, JPG, or PNG files are filtered out from the downloaded images.
Duplicates Images are also removed during download.
If you have low computation power use 
```bash
Simple_ImageScrapper.py
```
## Find&Move_Images.py
This code find moves images from a source directory to a destination directory.
You need to specify the paths to the source and destination directories. It will search for all the images even those which are in Subdirectories.

## Compare&Remove_ImagesByUsingNames.py
It retrieves the list of files in both directories and compares them.
Images present in the source directory but not in the destination directory are removed. It does the checking name of the Images and removing the same name Images.
The code prints the list of removed images and provides statistics on the total number of images before and after the process.
Code for Normalizing Images:

## Normalization.py
This code normalizes images in terms of dimensions and number of channels.
You need to specify the input and output directories.
It loops over the files in the input directory, loads each image, and checks its dimensions and channels.
If the image does not match the target dimensions or has an incorrect number of channels, it is resized and converted accordingly.
Normalized images are saved to the output directory, while images that already match the target dimensions and channels are simply copied.


## RemoveDuplicate.py
Code for Removing Duplicate Images:
It uses the imagehash library to calculate the average hash of each image.
The code keeps track of processed images and their hashes to identify duplicates.
Duplicate images are deleted, and the code prints the paths of removed duplicates and the corresponding kept images.

## Randomly_Rename.py
This Code checks all the images in a directory and uniquely renames them.
It generates a random alphanumeric name for each image and renames it accordingly.
The renamed images are saved in the same directory.
Make sure to specify the path to the directory containing the images.

## Remove text.py
This code snippet utilizes Tesseract OCR to detect and remove text from images.
Before using this code, make sure you have Tesseract OCR installed. You can download it from 
```bash
https://github.com/tesseract-ocr/tesseract.
```
Also specify the Directory of it in the code.
## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
Please make sure to follow the code of conduct in all your interactions with the project.

##  License
This project is licensed under the MIT License.
