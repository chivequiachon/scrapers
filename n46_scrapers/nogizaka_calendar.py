from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests


def scrape_schedules():
    options = Options()
    options.set_headless(headless=True)
    driver = webdriver.Firefox(firefox_options=options, executable_path="./geckodriver")
    driver.get("http://www.nogizaka46.com")
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    div_calendar = soup.find('div', class_="today")
    list_elements = div_calendar.find_all("li")

    schedules = []
    for element in list_elements:
        a = element.find("a")
        url = a.get("href")
        news_type = a.get("class")
        schedules.append({"newsType": news_type[0], "event": a.text, "url": "www.nogizaka46.com" + url})

    driver.quit()

    return schedules


def udpate_gspreadsheet(schedules, gas_url):
    json = {"schedules": schedules}
    r = requests.post(gas_url, json=json)
    return r.status_code

if __name__ == "__main__":
    GAS_URL = "https://script.google.com/macros/s/AKfycby2nDqAOiRvPya6IeeJAaF3twka53O5ktdFMFJ1ILTG9a4o6pk/exec"
    schedules = scrape_schedules()
    status_code = udpate_gspreadsheet(schedules, GAS_URL)
    print("status: {}".format(status_code))