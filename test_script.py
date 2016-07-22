#!/usr/bin/python
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

    def test_results_atlanta(self):
        # wait for element
        atlanta_tile_element = 'div.city-tile-atlanta'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, atlanta_tile_element)))

        # click to go to Atlanta results page
        driver.find_element(By.CSS_SELECTOR, atlanta_tile_element).click()
        time.sleep(2)

        # zipcodes in atlanta: 300xx - 303xx
        l = ['300', '301', '302', '303']

        for num in range(2, 27):
            element = "//div[@id='search-results-container']/div[%d]/div/div[2]/span/span[3]" % num
            for z in l:
                if "GA, {}".format(z) in driver.find_element_by_xpath(element).text:
                    print "yes: ", driver.find_element_by_xpath(element).text
                    break
            else:
                city_zipcode = driver.find_element_by_xpath(element).text
                print "element xpath: ", element
                print "this is the guy im comparing GA, {}".format(z)
                self.fail("Failed: {}".format(city_zipcode))  

    def test_results_bayarea(self):
        # wait for element
        bayarea_tile_element = 'div.city-tile-bay-area'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, bayarea_tile_element)))

        # click to go to Atlanta results page
        driver.find_element(By.CSS_SELECTOR, bayarea_tile_element).click()
        time.sleep(2)

        l = ['Oakland', 'Alameda', 'Berkeley', 'Albany', 'El Cerrito', 'San Francisco', 'Orinda']
        for num in range(2, 48):
            # time.sleep(1)
            element = "//div[@id='search-results-container']/div[%d]/div/div[2]/span/span[3]" % num

            for c in l:
                if c in driver.find_element_by_xpath(element).text:
                    print "yes: ", driver.find_element_by_xpath(element).text
                    break
            else:
                city = driver.find_element_by_xpath(element).text
                print "element xpath: ", element
                print "this is the guy im comparing".format(c)
                self.fail("Failed: {}".format(city))


    def test_results_boston(self):

        boston_tile_element = 'div.city-tile-boston'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, boston_tile_element)))

        # click to go to Atlanta results page
        driver.find_element(By.CSS_SELECTOR, boston_tile_element).click()
        time.sleep(2)

        l = ['Boston', 'Cambridge', 'Roxbury', 'Somerville', 'El Cerrito', 'San Francisco']
        for num in range(2, 47):
            # time.sleep(1)
            element = "//div[@id='search-results-container']/div[%d]/div/div[2]/span/span[3]" % num

            for c in l:
                if c in driver.find_element_by_xpath(element).text:
                    print "yes: ", driver.find_element_by_xpath(element).text
                    break
            else:
                city = driver.find_element_by_xpath(element).text
                print "element xpath: ", element
                print "this is the guy im comparing".format(c)
                self.fail("Failed: {}".format(city))

    def test_results_chicago(self):
        chicago_tile_element = 'div.city-tile-chicago'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, chicago_tile_element)))

        # click to go to Atlanta results page
        driver.find_element(By.CSS_SELECTOR, chicago_tile_element).click()
        time.sleep(2)

        l = ['Chicago']
        for num in range(2, 48):
            # time.sleep(1)
            element = "//div[@id='search-results-container']/div[%d]/div/div[2]/span/span[3]" % num

            for c in l:
                if c in driver.find_element_by_xpath(element).text:
                    print "yes: ", driver.find_element_by_xpath(element).text
                    break
            else:
                city = driver.find_element_by_xpath(element).text
                print "element xpath: ", element
                print "this is the guy im comparing".format(c)
                self.fail("Failed: {}".format(city))

    def test_results_DC(self):
        DC_tile_element = 'div.city-tile-d-c'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, DC_tile_element)))

        # click to go to Atlanta results page
        driver.find_element(By.CSS_SELECTOR, DC_tile_element).click()
        time.sleep(2)

        l = ['Washington DC', 'Arlington VA']
        for num in range(2, 48):
            # time.sleep(1)
            element = "//div[@id='search-results-container']/div[%d]/div/div[2]/span/span[3]" % num

            for c in l:
                if c in driver.find_element_by_xpath(element).text:
                    print "yes: ", driver.find_element_by_xpath(element).text
                    break
            else:
                city = driver.find_element_by_xpath(element).text
                print "element xpath: ", element
                print "this is the guy im comparing".format(c)
                self.fail("Failed: {}".format(city))

    def test_results_denver(self):
        denver_tile_element = 'div.city-tile-denver'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, denver_tile_element)))

        # click to go to Atlanta results page
        driver.find_element(By.CSS_SELECTOR, denver_tile_element).click()
        time.sleep(2)

        l = ['Denver CO', 'Lakewood CO', 'Englewood CO', 'Westminster CO', 'Westminister CO', 'Aurora CO', 'Commerce City CO', 'Thornton CO']
        for num in range(2, 37):
            # time.sleep(1)
            element = "//div[@id='search-results-container']/div[%d]/div/div[2]/span/span[3]" % num

            for c in l:
                if c in driver.find_element_by_xpath(element).text:
                    print "yes: ", driver.find_element_by_xpath(element).text
                    break
            else:
                city = driver.find_element_by_xpath(element).text
                print "element xpath: ", element
                print "this is the guy im comparing".format(c)
                self.fail("Failed: {}".format(city))


    def test_results_LA(self):
        LA_tile_element = 'div.city-tile-los-angeles'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, LA_tile_element)))

        # click to go to Atlanta results page
        driver.find_element(By.CSS_SELECTOR, LA_tile_element).click()
        time.sleep(2)

        l = ['Los Angeles CA', 'Monterey Park CA', 'Glendale CA']
        for num in range(2, 50):
            # time.sleep(1)
            element = "//div[@id='search-results-container']/div[%d]/div/div[2]/span/span[3]" % num

            for c in l:
                if c in driver.find_element_by_xpath(element).text:
                    print "yes: ", driver.find_element_by_xpath(element).text
                    break
            else:
                city = driver.find_element_by_xpath(element).text
                print "element xpath: ", element
                print "this is the guy im comparing".format(c)
                self.fail("Failed: {}".format(city))

    def test_results_nashville(self):
        nashville_tile_element = 'div.city-tile-nashville'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, nashville_tile_element)))

        # click to go to Atlanta results page
        driver.find_element(By.CSS_SELECTOR, nashville_tile_element).click()
        time.sleep(2)

        l = ['Nashville TN', 'Madison TN', 'Brentwood TN']
        for num in range(2, 43):
            # time.sleep(1)
            element = "//div[@id='search-results-container']/div[%d]/div/div[2]/span/span[3]" % num
            for c in l:
                if c in driver.find_element_by_xpath(element).text:
                    print "yes: ", driver.find_element_by_xpath(element).text
                    break
            else:
                city = driver.find_element_by_xpath(element).text
                print "element xpath: ", element
                print "this is the guy im comparing".format(c)
                self.fail("Failed: {}".format(city))

    def test_results_NY(self):
        NY_tile_element = 'div.city-tile-new-york'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, NY_tile_element)))

        # click to go to Atlanta results page
        driver.find_element(By.CSS_SELECTOR, NY_tile_element).click()
        time.sleep(2)

        l = ['New York NY', 'Brooklyn NY',]
        for num in range(2, 49):
            # time.sleep(1)
            element = "//div[@id='search-results-container']/div[%d]/div/div[2]/span/span[3]" % num
            for c in l:
                if c in driver.find_element_by_xpath(element).text:
                    print "yes: ", driver.find_element_by_xpath(element).text
                    break
            else:
                city = driver.find_element_by_xpath(element).text
                print "element xpath: ", element
                print "this is the guy im comparing".format(c)
                self.fail("Failed: {}".format(city))

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
