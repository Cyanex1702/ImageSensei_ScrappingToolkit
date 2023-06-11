from bing_image_downloader import downloader
from pathlib import Path

query_list = [
 # Type you query here
]

downloaded_files = set()
limit_per_query = 150  # Specify the limit per query

directory = Path('PathToDataSet')  # Specify the directory to save the downloaded images

# Create the directory if it doesn't exist
directory.mkdir(parents=True, exist_ok=True)

for query in query_list:
    output_dir = directory / query
    downloaded_images = len(list(output_dir.glob('*')))

    if downloaded_images >= limit_per_query:
        continue  # Move on to the next query if the limit is already met

    remaining_limit = limit_per_query - downloaded_images
    downloader.download(query, limit=remaining_limit, output_dir=output_dir, adult_filter_off=False,
                        force_replace=False, timeout=60)

    # Filter out non-JPEG, JPG, or PNG files
    [f.unlink() for f in output_dir.glob('*') if f.suffix.lower() not in ('.jpg', '.jpeg', '.png')]

    # Remove duplicates
    downloaded_files |= {downloader.get_image_hash(f.read_bytes()) for f in output_dir.glob('*')}
    [f.unlink() for f in output_dir.glob('*') if downloader.get_image_hash(f.read_bytes()) in downloaded_files]
