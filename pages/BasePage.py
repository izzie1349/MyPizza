from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from abc import abstractmethod
from Constants import LocatorMode
import time


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    @abstractmethod
    def _verify_page(self):
        """
        This method verifies that we are on the correct page.
        """
        return

    def wait_for_element_visibility(self, waitTime, locatorMode, Locator):
        """
        This method wraps selenium calls 
        """

        element = None

        if locatorMode == LocatorMode.ID:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.visibility_of_element_located((By.ID, Locator)))

        elif locatorMode == LocatorMode.NAME:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.visibility_of_element_located((By.NAME, Locator)))

        elif locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.visibility_of_element_located((By.XPATH, Locator)))

        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locator)))

        elif locatorMode == LocatorMode.LINK_TEXT:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.visibility_of_element_located((By.LINK_TEXT, Locator)))
          
        else:
            raise Exception("element not visible by any locater method!")

        return element


    def wait_until_element_clickable(self, waitTime, locatorMode, Locator):
        """
        This method wraps selenium calls
        """
        element = None

        if locatorMode == LocatorMode.ID:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.element_to_be_clickable((By.ID, Locator)))

        elif locatorMode == LocatorMode.NAME:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.element_to_be_clickable((By.NAME, Locator)))

        elif locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.element_to_be_clickable((By.XPATH, Locator)))

        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locator)))

        elif locatorMode == LocatorMode.LINK_TEXT:
            element = WebDriverWait(self.driver, waitTime).\
            until(EC.visibility_of_element_located((By.LINK_TEXT, Locator)))

        else:
            raise Exception("element not clickable by any locator methof!")

        return element

    def switch_to_window(self, wHandle):
        """
        This method handles popups and new windows that 
        the driver doesnt recognize
        """
        self.driver.switch_to.window(wHandle)

    def find_element(self, locatorMode, Locator):
        """
        This method wraps selenium calls
        """
        element = None

        if locatorMode == LocatorMode.ID:
            element = self.driver.find_element_by_id(Locator)

        elif locatorMode == LocatorMode.NAME:
            element = self.driver.find_element_by_name(Locator)

        elif locatorMode == LocatorMode.XPATH:
            element = self.driver.find_element_by_xpath(Locator)

        elif locatorMode == LocatorMode.CSS_SELECTOR: 
     	    element = self.driver.find_element_by_css_selector(Locator)

        elif locatorMode == LocatorMode.LINK_TEXT: 
            element = self.driver.find_element_by_link_text(Locator)

        else:
            raise Exception("unable to find element by any locator method!")

        return element


    def fill_out_field(self, locatorMode, Locator, text):
        """
        Helps method avoids a lot code duplication when filling out forms
        """
        self.find_element(locatorMode, Locator).clear()
        self.find_element(locatorMode, Locator).send_keys(text)

    def click(self, waitTime, locatorMode, Locator):
        self.wait_until_element_clickable(waitTime, locatorMode, Locator).click()


    def select_from_dropdown(self, locatorMode, Locator, text):
        Select(self.find_element(locatorMode, Locator)).select_by_visible_text(text)

    def press_enter(self, locatorMode, Locator, text):
        element = self.find_element(locatorMode, Locator).clear()
        element.send_keys(text)
        element.send_keys(Keys.RETURN)

    def element_not_present(self, locatorMode, Locator):
        self.find_element(locatorMode, Locator)
        if len(element) > 0:
            raise Exception("element is present")
        else:
            pass


class IncorrectPageException(Exception):
 """
 This exception is raised when we try insatirate wrong page.
 """
