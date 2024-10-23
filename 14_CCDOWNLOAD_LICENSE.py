import os
import requests
import uuid
import time

API_KEY = ''
CSE_ID = ''
num_results =

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

def download_image(url, save_path):
    response = requests.get(url, stream=True)
    print(f"Downloading {url} - Status Code: {response.status_code}")
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return True
    return False

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
