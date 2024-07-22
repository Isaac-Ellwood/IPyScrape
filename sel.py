from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import logging

# Set up logging to troubleshoot if anything goes wrong
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up headless Chrome options
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

# Initialize the WebDriver
logging.info("Initializing WebDriver")
driver = webdriver.Chrome(options=options, executable_path='chrome-win64/chrome.exe')

# Load the Hacker News homepage
logging.info("Loading Hacker News homepage")
driver.get("https://news.ycombinator.com/")

# Get page source and parse it with BeautifulSoup
logging.info("Parsing page source with BeautifulSoup")
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all titles on the page (class - titleline)
logging.info("Finding all story titles on the page")
titles = soup.find_all('span', class_='titleline')

if titles:
    logging.info(f"Found {len(titles)} titles. Printing titles:")
    # Print each title
    for title in titles:
        title_link = title.find('a')
        if title_link:
            print(title_link.text)
else:
    logging.warning("No titles found on the page.")

# Close the driver
logging.info("Closing WebDriver")
driver.quit()