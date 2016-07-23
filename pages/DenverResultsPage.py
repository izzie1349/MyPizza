from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Constants import LocatorMode
from BasePage import BasePage
import time

class DenverResultsPage(BasePage):

    def __init__(self, driver):
        super(DenverResultsPage, self).__init__(driver)

    def _verify_page(self):
        """
        This method verifies that we are on the correct page.
        """
        try:
            self.wait_for_element_visibility(10, "xpath", "//div[@id='search-results-container']/div/div/div[2]/span/span[3]")
        except:
            raise IncorrectPageException

    def verify_results(self):
        l = ['Denver CO', 'Lakewood CO', 'Englewood CO', 'Westminster CO', 'Westminister', 'Aurora CO', 'Commerce City CO', 'Thornton CO']
        for num in range(2, 37):
            element = "//div[@id='search-results-container']/div[%d]/div/div[2]/span/span[3]" % num
            for c in l:
                if c in self.find_element('xpath', element).text:
                    # print "yes: ", self.find_element('xpath', element).text
                    break
            else:
                c = self.find_element('xpath', element).text
                print "element xpath: ", element, c # debugging purposees
                raise Exception('city on site is not in our list of acceptable cities')
