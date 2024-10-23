# CCDOWNLOAD_LICENSE.py
This Python script downloads images from the web based on specified search queries. It utilizes the Google Custom Search API to find and retrieve images, saving them with unique filenames to a local directory. This tool is useful for collecting images for various projects or datasets.

- Visual Studio Code release used: 1.93.1
- Python release used: 3.12.4 (64-bit)
> Warning: There are no guarantees this code will run on your machine.

## Features
Google custom search API integration: searches for images using the Google Custom Search API, filtering for images that are public domain.
Image downloading: downloads found images to a local directory, renaming them with unique UUIDs to avoid conflicts.
Progress tracking: displays progress updates, including the time taken for each query and estimated time remaining.

## Prerequisites
- Python 3.x installed on your machine.
- Install the requests library if not already installed:
```
pip install requests
```
A Google Custom Search API key and Custom Search Engine ID.

## Parameters
API_KEY: your Google Custom Search API key.
CSE_ID: your Google Custom Search Engine ID.
num_results: the number of image results to fetch for each query.

## Description
The script defines functions to search for images based on user-defined queries and download them to a specified directory. Each image is saved with a unique filename generated using UUID to ensure no conflicts. The program provides feedback on the download progress and the time taken for each query.

## Key Functions
### search_images(query, num_results=num_results)
This function sends a request to the Google Custom Search API to search for images matching the provided query. It retrieves up to num_results images, iterating through results if necessary.
```
def search_images(query, num_results = num_results):
    images = []
    for start in range(1, num_results + 1, 10):
        search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={CSE_ID}&searchType=image&rights=cc_publicdomain&key={API_KEY}&start={start}"
        response = requests.get(search_url)
        print(f"API Response Code: {response.status_code} for start={start}")
        if response.status_code == 200:
            results = response.json()
            items = results.get('items', [])
            images.extend(items)
            if len(items) < 10:
                break
        else:
            print(f"Failed to fetch images. Status code: {response.status_code}")
            print(f"Response Content: {response.content.decode()}")
            break
    return images
```

### download_image(url, save_path)
This function downloads an image from the specified URL and saves it to the provided path. It returns True if successful and False otherwise.
```
def download_image(url, save_path):
    response = requests.get(url, stream=True)
    print(f"Downloading {url} - Status Code: {response.status_code}")
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return True
    return False
```

### main()
The main function orchestrates the image searching and downloading process. It defines a list of queries, creates a directory for saving images, and processes each query, reporting on the number of images found and the download progress.
```
def main():
    # List of queries to search for
    queries = [
   "1", "2", "3",
]

    image_dir = 'images'
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    
    start_time = time.time()
    
    for query in queries:
        query_start_time = time.time()
        
        images = search_images(query)
        print(f"Found {len(images)} images for query: {query}")

        for image_info in images:
            image_url = image_info['link']
            image_type = image_info.get('mime', 'image/jpeg')
            image_extension = image_type.split('/')[-1]

            random_filename = str(uuid.uuid4()) + f'.{image_extension}'
            image_path = os.path.join(image_dir, random_filename)

            print(f"Saving as: {image_path}")
            
            if download_image(image_url, image_path):
                print(f"Downloaded {image_url} to {image_path}")
            else:
                print(f"Failed to download {image_url}")

        query_end_time = time.time()
        query_duration = query_end_time - query_start_time
        print(f"Time taken for query '{query}': {query_duration:.2f} seconds")
        
        queries_left = len(queries) - (queries.index(query) + 1)
        estimated_time_left = queries_left * query_duration
        print(f"Estimated time remaining: {estimated_time_left/60:.2f} minutes\n")

    total_time = time.time() - start_time
    print(f"Total time taken: {total_time/60:.2f} minutes")

if __name__ == "__main__":
    main()
```

## Usage
- Set your API_KEY and CSE_ID in the script.
- Specify the number of results to fetch for each query by setting the num_results variable.
- Customize the queries list with your desired search terms.


## License
This project is licensed under the MIT License. See the LICENSE file for more information.
