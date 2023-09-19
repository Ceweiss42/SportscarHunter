from icrawler.builtin import GoogleImageCrawler
import os

keyword = "cat"  # Replace with your desired search keyword
max_num = 100  # Replace with the maximum number of images you want to download

# Specify the absolute path to the desktop/testing folder
root_dir = os.path.expanduser("~/Desktop/testing")

# Create the directory if it doesn't exist
if not os.path.exists(root_dir):
    os.makedirs(root_dir)

google_crawler = GoogleImageCrawler(
    parser_threads=2, 
    downloader_threads=4,
    storage={"root_dir": root_dir}
)

google_crawler.crawl(keyword=keyword, max_num=max_num)
