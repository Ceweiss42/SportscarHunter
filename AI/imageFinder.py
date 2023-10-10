import time
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests

# Replace this URL with the website you want to scrape


def bingify(car):
    car.replace(" ", "%20")
    return car

def duckify(car):
    car.replace(" ", "+")
    return car


for car in open("carNames.txt", "r").readlines()[2:6]:

    car = car.strip()
    bingCar = bingify(car)
    googleCar = bingify(car)
    duckCar = duckify(car)




    #AC Cobra MkII (1963-1965)
    urls = ["https://www.bing.com/images/search?tbm=isch&q="+bingCar,
        "https://www.google.com/search?tbm=isch&q="+googleCar,
        "https://duckduckgo.com/?q="+duckCar+"&iax=images&ia=images"]


    # Create a Selenium WebDriver instance
    driver = webdriver.Firefox()  # You need to have ChromeDriver installed

    with open("links.txt", "w+") as file:

        for url in urls:
        # Navigate to the URL
            driver.get(url)

            # Scroll down the page to trigger lazy loading
            scroll_pause_time = 2  # Adjust this value as needed
            scroll_height = driver.execute_script("return document.body.scrollHeight")

            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(scroll_pause_time)
                new_scroll_height = driver.execute_script("return document.body.scrollHeight")
                if new_scroll_height == scroll_height:
                    break
                scroll_height = new_scroll_height

            # Parse the updated HTML content of the page
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            # Find all "img" tags in the updated HTML
            img_tags = soup.find_all('img')

            # Extract and print the "src" attribute from each "img" tag
            
            for img_tag in img_tags:
                src = img_tag.get('src')
                if src:
                    if "external-content" in src:
                        src = src[19:]
                    file.write(src + "\n")

            print(len(img_tags))

    driver.quit()

    os.system("sort links.txt | uniq > output.txt")



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
    save_directory = '/media/cameron/76E8-CACF/'+car

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
