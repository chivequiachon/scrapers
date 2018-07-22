from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests

def scrape():
    options = Options()
    options.set_headless(headless=True)
    driver = webdriver.Firefox(firefox_options=options, executable_path="./geckodriver")
    driver.get("http://www.nogizaka46.com")
    #r = requests.get("http://www.nogizaka46.com")
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    div_calendar = soup.find('div', class_="today")
    list_elements = div_calendar.find_all("li")

    #schedules = []
    for element in list_elements:
        a = element.find("a")
        href = a.get("href")
        print("{} - {}".format(a.text, href))

    driver.quit()

    #return updates

if __name__ == "__main__":
    scrape()
