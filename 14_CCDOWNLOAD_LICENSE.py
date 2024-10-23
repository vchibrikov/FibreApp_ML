import os
import requests
import uuid
import time

# Replace with your own API key and CSE ID
API_KEY = 'AIzaSyAvaBb3MWldv-19-TYQ5qD7GAHf1MEzCPA'
CSE_ID = '01e7088a2ad5b4253'

def search_images(query, num_results=800):
    images = []
    for start in range(1, num_results + 1, 10):
        search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={CSE_ID}&searchType=image&rights=cc_publicdomain&key={API_KEY}&start={start}"
        response = requests.get(search_url)
        print(f"API Response Code: {response.status_code} for start={start}")
        if response.status_code == 200:
            results = response.json()
            items = results.get('items', [])
            images.extend(items)
            if len(items) < 10:  # No more results available
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
    
    # Sports
    "soccer match",
    "basketball game",
    "tennis player",
    "swimming pool",
    "marathon runners",
    "yoga class",
    "golf course",
    "boxing ring",
    "skiing downhill",
    "surfing wave",
    "hockey game",
    "cycling race",
    "cricket match",
    "football stadium",
    "gym workout",
    "weightlifting",
    "fencing match",
    "rugby scrum",
    "volleyball beach",
    "badminton court",
    "karate competition",
    "baseball game",
    "archery target",
    "rock climbing",
    "rowing team",
    "skateboarding",
    "snowboarding",
    "track and field",
    "table tennis",
    "sailing yacht",
    
    # Smart House
    "smart thermostat",
    "voice assistant",
    "smart home security",
    "home automation",
    "smart light bulb",
    "smart door lock",
    "robot vacuum cleaner",
    "wireless speakers",
    "smart refrigerator",
    "smart home hub",
    "smart doorbell",
    "smart TV",
    "home energy monitor",
    "smart blinds",
    "smart plugs",
    "home automation app",
    "smart home devices",
    "security camera",
    "connected appliances",
    "home alarm system",
    "automated lighting",
    "smart home integration",
    "smart kitchen",
    "smart coffee maker",
    "smart smoke detector",
    "smart oven",
    "remote control home",
    "home network system",
    "smart irrigation system",
    "smart home entertainment",
    
    # Healthcare
    "stethoscope and doctor",
    "medical research",
    "hospital bed",
    "digital health records",
    "nurse and patient",
    "X-ray image",
    "blood pressure monitor",
    "telemedicine consultation",
    "surgical instruments",
    "fitness tracker",
    "prescription medication",
    "first aid kit",
    "medical conference",
    "health insurance card",
    "ambulance",
    "personal protective equipment",
    "doctor consultation",
    "healthcare technology",
    "medical laboratory",
    "MRI scan",
    "medical education",
    "health and wellness",
    "rehabilitation therapy",
    "pharmacy counter",
    "clinical trials",
    "mental health support",
    "vaccination site",
    "medical billing",
    "nutritionist consultation",
    "physical therapy",
    
    # Finance and Banking
    "credit card transaction",
    "mobile banking app",
    "ATM machine",
    "stock market trading",
    "financial planning",
    "savings account",
    "online payment",
    "investment portfolio",
    "digital wallet",
    "bank loan approval",
    "cryptocurrency exchange",
    "budgeting app",
    "mortgage application",
    "financial advisor",
    "business loan",
    "accounting software",
    "retirement savings",
    "insurance policy",
    "wealth management",
    "tax return filing",
    "interest rates",
    "financial market",
    "credit score report",
    "debt consolidation",
    "personal finance management",
    "bank statement",
    "contactless payment",
    "financial literacy",
    "banking services",
    "economic analysis",
    
    # Transportation
    "electric car charging",
    "airplane takeoff",
    "bicycle lane",
    "train station",
    "bus stop",
    "highway traffic",
    "city metro",
    "ride-sharing service",
    "car dashboard",
    "shipping container",
    "taxi cab",
    "motorcycle riding",
    "scooter rental",
    "cruise ship",
    "commercial airplane",
    "subway train",
    "parking garage",
    "automated toll booth",
    "public transit map",
    "traffic light",
    "railroad crossing",
    "electric scooter",
    "trucking logistics",
    "airport terminal",
    "cargo ship",
    "passenger airplane",
    "commuter bus",
    "bike-sharing program",
    "taxi driver",
    "city tram"
]

    # Ensure the images directory exists
    image_dir = 'images'
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    
    start_time = time.time()  # Start time of the entire process
    
    for query in queries:
        query_start_time = time.time()  # Start time for this query
        
        images = search_images(query)
        print(f"Found {len(images)} images for query: {query}")

        for image_info in images:
            image_url = image_info['link']
            image_type = image_info.get('mime', 'image/jpeg')  # Default to jpeg if mime type is not available
            image_extension = image_type.split('/')[-1]

            # Generate a random filename
            random_filename = str(uuid.uuid4()) + f'.{image_extension}'
            image_path = os.path.join(image_dir, random_filename)

            print(f"Saving as: {image_path}")
            
            if download_image(image_url, image_path):
                print(f"Downloaded {image_url} to {image_path}")
            else:
                print(f"Failed to download {image_url}")

        query_end_time = time.time()  # End time for this query
        query_duration = query_end_time - query_start_time
        print(f"Time taken for query '{query}': {query_duration:.2f} seconds")
        
        # Estimate remaining time
        queries_left = len(queries) - (queries.index(query) + 1)
        estimated_time_left = queries_left * query_duration
        print(f"Estimated time remaining: {estimated_time_left/60:.2f} minutes\n")

    total_time = time.time() - start_time  # Total time for the script
    print(f"Total time taken: {total_time/60:.2f} minutes")

if __name__ == "__main__":
    main()
