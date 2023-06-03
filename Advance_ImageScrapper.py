from bing_image_downloader import downloader
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

query_list = [
    # Add your desired queries here
]

# Remove duplicates from the query_list
query_list = list(set(query_list))

limit_per_query = 200  # Specify the limit per query
directory = Path('PathToDataSet')  # Specify the directory where the images will be downloaded

def process_query(query):
    output_dir = directory / query
    downloaded_images = len(list(output_dir.glob('*')))

    if downloaded_images >= limit_per_query:
        return  # Skip if the limit is already met

    remaining_limit = limit_per_query - downloaded_images
    downloader.download(query, limit=remaining_limit, output_dir=output_dir, adult_filter_off=False,
                        force_replace=False, timeout=60)

    # Filter out non-JPEG, JPG, or PNG files
    [f.unlink() for f in output_dir.glob('*') if f.suffix.lower() not in ('.jpg', '.jpeg', '.png')]

# Create a ThreadPoolExecutor with max_workers set to 25
executor = ThreadPoolExecutor(max_workers=25)

# Submit the query processing tasks to the executor
for query in query_list:
    # Submit a task (query) to the executor
    executor.submit(process_query, query)

# Shutdown the executor and wait for all tasks to complete
executor.shutdown(wait=True)
