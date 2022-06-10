from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from scraping_team_names_url import getting_teams_data


if __name__ == '__main__':
    options = Options()
    path = "/Users/aviramavivi/chromedriver/chromedriver"
    driver = webdriver.Chrome(executable_path=path)
    url = "https://www.euroleague.net/competition/teams?seasoncode=E2021"
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#onetrust-accept-btn-handler'))).click()
    #^^accepting cookikes^^

    for page_number in [x for x in range(1,12) if x != 2]: # from stackoverflow
        select = Select(driver.find_element_by_class_name("seasons-selector"))
        select.select_by_index(page_number)
        getting_teams_data(driver.current_url,page_number)

    time.sleep(5)
