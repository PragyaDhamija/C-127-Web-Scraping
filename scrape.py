from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(start_url)
time.sleep(10)

def scrape():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
    #for i in range(0, 428):
    for i in range(0,10):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ulTag in soup.find_all("ul", attrs={"class","exoplanet"}):
            liTags = ulTag.find_all("li")
            temp_list = []
             #Enumerate is a function that returns the index along with the element.
            for index,liTag in enumerate(liTags):
                if(index==0):
                    temp_list.append(liTag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(liTag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element("xpath","/html/body/div[2]/div/div[3]/section[2]/div/section[2]/div/div/article/div/div[2]/div[1]/div[2]/div[1]/div/nav/span[2]/a").click()
    with open("scrapeData.csv" , "w") as f:
        c = csv.writer(f)
        c.writerow(headers)
        c.writerows(planet_data)

scrape() 