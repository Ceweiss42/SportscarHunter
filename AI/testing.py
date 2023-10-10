import requests
from PIL import Image
from io import BytesIO
import keyboard

# Function to display an image from a URL
def display_image_from_url(image_url):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img.show()
        else:
            print(f"Failed to retrieve image from URL: {image_url}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Read the list of image links from a text file
file_path = 'output.txt'

try:
    with open(file_path, 'r') as file:
        image_links = file.readlines()
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Create a file to store cleaned links
cleaned_file = open('cleaned.txt', 'a')

# Iterate through the image links and display/handle each image one by one
current_index = 0
while current_index < len(image_links):
    image_link = image_links[current_index].strip()
    
    if image_link:
        display_image_from_url("https://" + image_link)
    
    # Wait for 'q' or 'p' key press
    key_event = keyboard.read_event(suppress=True)
    
    if key_event.event_type == keyboard.KEY_DOWN:
        if key_event.name == 'q':
            current_index += 1  # Move to the next image
        elif key_event.name == 'p':
            # Save the current image link to "cleaned.txt"
            cleaned_file.write(image_link + '\n')
            current_index += 1  # Move to the next image

cleaned_file.close()
print("Finished viewing and cleaning images.")
