import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Step 1: Get URL from user
    url = input("Please enter the image URL: ")
    
    try:
        # Step 2: Create "Fetched_Images" directory if it doesn’t exist
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Step 3: Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # If HTTP error, raise exception
        
        # Step 4: Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image.jpg"
        
        # Step 5: Save image in binary mode
        filepath = os.path.join("Fetched_Images", filename)
        with open(filepath, "wb") as f:
            f.write(response.content)
        
        # Step 6: Print success message
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
    
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()
