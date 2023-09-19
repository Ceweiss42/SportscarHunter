import os
from selenium import webdriver
import requests
import time
import random
from icrawler.builtin import GoogleImageCrawler

def getNames():
    with  open("carsFormatted.txt", "r") as file:
        for line in file.readlines():
            yield line

def formatName(name):
    out =  " ".join(name.split("\t")).strip() + ")"
    index = len(out) - 10
    out = out[:index] + "(" + out[index:]

    index = len(out) - 5
    out = out[:index - 1] + "-" + out[index:]
    return out

def generate():
    with open("AutoDex-AI/carNames.txt", "r") as file:
        min = 0
        max = 70
        for line in file.readlines()[min:max]:
            folder = "/media/cameron/76E8-CACF/" + line.replace("\n", "")
            os.mkdir(folder)
            getImages(folder, "/media/cameron/76E8-CACF/")

def getImages(folder, master):
    query = folder[len(master):]

    print(folder)

    if os.path.exists(folder):
        print("FOUND A FOLDER!", folder)
        root_dir = folder
        google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4, storage={"root_dir": root_dir})

        google_crawler.crawl(keyword=query + " exterior", max_num=100)



    


if __name__ == "__main__":
    
    #compile formatted names into TXT file 'carNames'
    '''with open("carNames.txt", "w+") as f:
        for x in getNames():
            f.write(formatName(x) + "\n")'''
    
    #make folders for each entry in the file
    generate()



