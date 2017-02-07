# cell 0
# Install the selenium library
# http://selenium-python.readthedocs.io/getting-started.html

# !pip install selenium

# cell 1
# we will need several libraries
# we will use selenium to immitate human web browsing
# the BeautifulSoup library is very useful for parsing HTML
# we will use the csv library objects for writing the results to a csv file

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import csv

# cell 2
# we will define a URL
# and request the URL content using the Chrome browser driver


#url = "https://www.tripadvisor.ca/Hotel_Review-g294260-d7718988-Reviews-Ferra_Hotel_Boracay-Boracay_Aklan_Province_Panay_Island_Visayas.html"
url = "https://www.tripadvisor.ca/Hotel_Review-g294260-d7718988-Reviews-or10-Ferra_Hotel_Boracay-Boracay_Aklan_Province_Panay_Island_Visayas.html#REVIEWS"

geckoPath = 'H:\Download\geckodriver-v0.14.0-win64\geckodriver.exe'
binary = FirefoxBinary()
driver = webdriver.Firefox(firefox_binary=binary,executable_path=geckoPath)
#driver = webdriver.Firefox()
# driver = webdriver.Chrome("H:\Download\chromedriver_win32\chromedriver.exe")
driver.get(url)

# The HTML code for the web page is stored in the html variable
html = driver.page_source
print("yes")

# we will use the soup object to parse HTML
# BeautifulSoup reference
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

soup = BeautifulSoup(html, "lxml")

# we will use find_all method to find all paragraph tags of class partial_entry
# The result of this command is a list
# we use for .. in [] to iterate through the list

print("Hotel")
for hotelName in soup.find_all("div", "heading_name_wrapper"):
    print(hotelName.text)

hotelName = hotelName.text.strip()


listUserName = []
for review in soup.find_all("div", "username mo"):
    listUserName.append(review.text.strip())


list = []
for review in soup.find_all("p", "partial_entry"):
    list.append(review.text.strip())

dictFinal = dict(zip(listUserName, list))


driver.close()


#Write the csv

for k, v in dictFinal.items():
#define your path  and create csv with the same name
    fileName = r"H:\\Download\\work\\"+k+"-"+hotelName+".csv"
    fileName = fileName.replace(" ","")
    #print(v)

    #print(fileName)
    with open(fileName,'w', newline='') as outcsv:
            writer = csv.writer(outcsv, delimiter=',')
            #Write item to outcsv
            writer.writerow([v,])

# cell 3


