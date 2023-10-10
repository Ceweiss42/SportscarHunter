import requests
import os

# Function to download an image from a URL
def download_image(image_url, save_dir):
    try:
        response = requests.get("https://"+image_url)
        if response.status_code == 200:
            # Extract the filename from the URL
            filename = save_dir+"/"+str(len(os.listdir(save_dir)))+".jpg"
            with open(filename, 'wb') as img_file:
                img_file.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to retrieve image from URL: {image_url}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Directory where you want to save the downloaded images
save_directory = '/media/cameron/76E8-CACF/AC Cobra MkII (1963-1965)'

# Create the save directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Read the list of image links from "cleaned.txt"
cleaned_file_path = 'output.txt'

try:
    with open(cleaned_file_path, 'r') as file:
        image_links = file.readlines()
except FileNotFoundError:
    print(f"File not found: {cleaned_file_path}")
    exit()

# Iterate through the image links and download each image
for image_link in image_links:
    image_link = image_link.strip()
    
    if image_link:
        download_image(image_link, save_directory)

print("Finished downloading images.")
