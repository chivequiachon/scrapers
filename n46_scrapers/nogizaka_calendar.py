from bs4 import BeautifulSoup
from selenium import webdriver
import requests

def scrape():
    driver = webdriver.Firefox()
    driver.get("http://www.nogizaka46.com")
    #r = requests.get("http://www.nogizaka46.com")
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    div_calendar = soup.find('div', class_="today")
    list_elements = div_calendar.find_all("li")

    #schedules = []
    for element in list_elements:
        a = element.find("a")
        href = a.get("href")
        print("{} - {}" % (a.text, href.text))

    #return updates

if __name__ == "__main__":
    scrape()