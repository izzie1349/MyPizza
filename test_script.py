#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by  import By
import unittest
import time


class TestResults(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("https://www.mypizza.com/")

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

        l = ['Denver CO', 'Lakewood CO', 'Englewood CO', 'Westminster CO', 'Westminister', 'Aurora CO', 'Commerce City CO', 'Thornton CO']
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

    def test_results_philadelphia(self):
        philadelphia_tile_element = 'div.city-tile-philadelphia'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, philadelphia_tile_element)))

        # click to go to Atlanta results page
        driver.find_element(By.CSS_SELECTOR, philadelphia_tile_element).click()
        time.sleep(2)

        l = ['Philadelphia PA']
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


    def test_results_portland(self):
        portland_tile_element = 'div.city-tile-portland'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, portland_tile_element)))

        # click to go to Atlanta results page
        driver.find_element(By.CSS_SELECTOR, portland_tile_element).click()
        time.sleep(2)

        l = ['Beaverton OR', 'Lake Oswego OR', 'Happy Valley', 'Portland OR']
        for num in range(2, 21):
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

    def test_results_seattle(self):
        seattle_tile_element = 'div.city-tile-seattle'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, seattle_tile_element)))

        # click to go to Atlanta results page
        driver.find_element(By.CSS_SELECTOR, seattle_tile_element).click()
        time.sleep(2)

        l = ['Seattle WA', 'Bellevue WA', 'Kirkland WA', 'Burien WA']
        for num in range(2, 45):
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

class TestOrder(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("https://www.mypizza.com/")

    def test_minimum_amount(self):
        # user should not be able to enter "checkout page" if subtotal less than minimum amount

        # click NY tile
        NY_tile_element = 'div.city-tile-new-york'
        see_tile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, NY_tile_element)))


        driver.find_element(By.CSS_SELECTOR, NY_tile_element).click()
        time.sleep(2)

        # NY results page - click tre sorelle
        element = "//div[@id='search-results-container']/div[2]/div/div[2]/h4" 
        driver.find_element_by_xpath(element).click()
        time.sleep(2)


        # tre sorelle restaurant -- click enter you location
        location_link = driver.find_element(By.LINK_TEXT, 'Enter your address')
        location_link.click()
        time.sleep(2)

        # adress popup--weird duplicate
        address_field = driver.find_element_by_name('address')
        address_field.clear()
        address_field.send_keys("63 reade street, new york, ny, united states")
        time.sleep(2)

        delivery_button = driver.find_element_by_css_selector('#delivery')
        delivery_button.click()
        time.sleep(2)

        # choose an order with less than $18 (min)
        specialty_pizza_dropdown_element = "#category-227 > div.menu-list-header > div.row > div.col-xs-6.col-md-8 > h3"
        driver.find_element(By.CSS_SELECTOR, specialty_pizza_dropdown_element).click()
        time.sleep(1)
            
        napoletano_pizza_large = "//tr[@id='product-1731668']/td[2]/ul/li[2]/span[2]"
        driver.find_element(By.XPATH, napoletano_pizza_large).click()
        # # raw_input('bla')
        time.sleep(5)


        add_to_cart_button = 'add_cart_item_button'
        driver.find_element(By.ID, add_to_cart_button).click()
        time.sleep(2)

        checkout_link = 'CHECK OUT'
        driver.find_element(By.LINK_TEXT, checkout_link).click()
        time.sleep(3)

        self.assertEqual(u"Error\nYour order doesn't meet the $18.00 delivery subtotal minimum.", driver.find_element_by_css_selector("div.error").text)






    def tearDown(self):
        driver.quit()



if __name__ == "__main__":
   unittest.main()
