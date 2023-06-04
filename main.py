import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

NUM_PAGES = 63
URL_STEAM_DB = "https://steamdb.info/"
DRIVER_PATH = "C:\\Users\\keenly\\PycharmProjects\\Porfolio_project_day92_WEB_SCRAPING"
driver_service = Service(executable_path=DRIVER_PATH)
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=driver_service)


# Brain
try:
	driver.get(URL_STEAM_DB)
	time.sleep(5)
	click_button = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[2]/div[1]/div[1]/table/thead/tr/th[1]/a").click()
	time.sleep(5)
	games_data = []
	for page in range(NUM_PAGES):
		games_link = driver.find_elements(By.CSS_SELECTOR, ".text-left a")
		for link in games_link:
			if link.get_attribute("text").strip() and link.get_attribute("href").strip():
				game_title = link.get_attribute("text").strip()
				games_links = link.get_attribute("href").strip()
				game_data = {'Title': game_title, 'URL': games_links}
				games_data.append(game_data)
				print(game_data)
		driver.find_element(By.LINK_TEXT, "Next").click()

	with open ('games.csv', 'w', newline='', encoding='utf-8') as file:
		fieldnames = ['Title', 'URL']
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		writer.writeheader()
		for game_data in games_data:
			writer.writerow(game_data)
finally:
	print('Данные игр успешно сохранены в файл CSV.')
	driver.quit()