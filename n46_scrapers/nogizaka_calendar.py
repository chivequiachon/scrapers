from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bottle import route, run, template
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

@route('/parse/nogi/sched')
def index():
    return template("<b>hello world</b>!", name=name)

if __name__ == "__main__":
    #scrape()
    run(host='localhost', port=8080)
