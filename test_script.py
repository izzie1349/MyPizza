
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by  import By
import unittest
import time

class WaitForElements(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("https://www.mypizza.com/")
    
    def test_wait_for_atlanta_tile(self):
    	# time.sleep(5)

    	atlanta_tile_element = 'div.city-tile-atlanta'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, atlanta_tile_element)))
    
    def test_wait_for_search_field(self):
    	# time.sleep(5)

    	search_field_element = 'project'
        see_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, search_field_element)))

    
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()


