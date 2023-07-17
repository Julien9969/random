from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options 
import time

options = uc.ChromeOptions() 
# options.headless = True
# Set up the Selenium webdriver
driver = uc.Chrome(
    # service=ChromeService(ChromeDriverManager().install()),
    options=options,
    headless=True
)
  # Adjust this based on your browser and driver location
driver.get('https://www.crunchyroll.com/fr/videos/alphabetical')
driver.maximize_window() 
time.sleep(7)
# Wait for the page to load and display the first series
wait = WebDriverWait(driver, 7)
first_series = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'horizontal-card__images-wrapper--ufKkO')))

h = 2000
previous_Anime = ''
with open('cr links/links.txt', 'w') as f:
    while True:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Find all the anime links on the page
        anime_links = soup.find_all('a', class_='horizontal-card__images-wrapper--ufKkO')
        
        print("= ==== = = = = = == = =")
        if previous_Anime == anime_links[0]['href']:
            print("Fin")
            break
        # Extract and print the URLs
        for link in anime_links:
            anime_url = link['href']
            f.write(f'{anime_url}\n')
            print(anime_url)
        
        # Scroll down to show the next series
        driver.execute_script(f"window.scrollTo(0, {h});")
        h += 2000
        time.sleep(6)
        # Wait for the page to load and display the first series
        wait = WebDriverWait(driver, 5)
        # Wait for the next series to load
        # wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'horizontal-card__images-wrapper--ufKkO')))
