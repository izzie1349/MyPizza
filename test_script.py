#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by  import By
import unittest
import time
# TODO: refactor using Page Object Model

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

    def test_order_variation(self): 
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

        # main menu
        specialty_pizza_dropdown_element = "#category-227 > div.menu-list-header > div.row > div.col-xs-6.col-md-8 > h3"
        driver.find_element(By.CSS_SELECTOR, specialty_pizza_dropdown_element).click()
        time.sleep(1)
            
        napoletano_pizza_large = "//tr[@id='product-1731668']/td[2]/ul/li[2]/span[2]"
        driver.find_element(By.XPATH, napoletano_pizza_large).click()

        time.sleep(2)
        wait = WebDriverWait(driver, 10)

        peperoni = wait.until(EC.element_to_be_clickable((By.ID, "order_item_selection_ids_18197131")))
        peperoni.click()
        add_to_cart_button = 'add_cart_item_button'
        driver.find_element(By.ID, add_to_cart_button).click()
        time.sleep(2)

        first_sub = "span.order-totals-cost"
        self.assertEqual("$17.95", driver.find_element_by_css_selector(first_sub).text)
        time.sleep(5)

        # main menu -- second order 
        driver.find_element_by_xpath("//tr[@id='product-1731670']/td[2]/ul/li[2]/span[2]").click()
        time.sleep(2)
        driver.find_element_by_id("add_cart_item_button").click()
        time.sleep(5)

        second_sub = "span.order-totals-cost"
        self.assertEqual("$35.90", driver.find_element_by_css_selector(second_sub).text)
        time.sleep(5)

        # main menu --third order
        driver.find_element_by_xpath("//tr[@id='product-1731706']/td[2]/ul/li[2]/span[2]").click()
        time.sleep(2)
        driver.find_element_by_id("add_cart_item_button").click()
        time.sleep(5)

        third_sub = "span.order-totals-cost"
        self.assertEqual("$53.85", driver.find_element_by_css_selector(third_sub).text)
        time.sleep(5)

        # main menu -- remove peperoni
        edit_link = "edit-product-modal-link-0"
        driver.find_element_by_id(edit_link).click()
        time.sleep(2)

        # uncheck pep
        pep = "order_item_selection_ids_18197131"
        driver.find_element(By.ID, pep).click()
        time.sleep(2)

        # add cart
        driver.find_element(By.XPATH, "(//button[@id='add_cart_item_button'])[2]").click()
        time.sleep(5)

        last_sub = "span.order-totals-cost"
        self.assertEqual("$51.85", driver.find_element_by_css_selector(third_sub).text)
        time.sleep(5)


    def tearDown(self):
        driver.quit()



if __name__ == "__main__":
   unittest.main()