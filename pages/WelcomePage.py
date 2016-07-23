from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Constants import LocatorMode
from BasePage import BasePage
from AtlantaResultsPage import AtlantaResultsPage
from BayAreaResultsPage import BayAreaResultsPage
from BostonResultsPage import BostonResultsPage
from ChicagoResultsPage import ChicagoResultsPage
from DCResultsPage import DCResultsPage
from DenverResultsPage import DenverResultsPage
from LAResultsPage import LAResultsPage
from NashvilleResultsPage import NashvilleResultsPage
from NYResultsPage import NYResultsPage
from PhiladelphiaResultsPage import PhiladelphiaResultsPage
from PortlandResultsPage import PortlandResultsPage
from SeattleResultsPage import SeattleResultsPage
import time

class WelcomePage(BasePage):

    def __init__(self, driver):
        super(WelcomePage, self).__init__(driver)


    def _verify_page(self):
        """
        This method verifies that we are on the correct page.
        """
        try:
            self.wait_for_element_visibility(10, "cssSelector", "div.city-tile-atlanta")
        except:
            raise IncorrectPageException

    def click_atlanta_tile(self):
        self.click(10, "cssSelector", "div.city-tile-atlanta")

        return AtlantaResultsPage

    def click_bayarea_tile(self):
        self.click(10, "cssSelector", "div.city-tile-bay-area")

        return BayAreaResultsPage


    def click_boston_tile(self):
        self.click(10, "cssSelector", "div.city-tile-boston")

        return BostonResultsPage

    def click_chicago_tile(self):
        self.click(10, "cssSelector", "div.city-tile-chicago")

        return ChicagoResultsPage

    def click_dc_tile(self):
        self.click(10, "cssSelector", "div.city-tile-d-c")

        return DCResultsPage

    def click_denver_tile(self):
        self.click(10, "cssSelector", "div.city-tile-denver")

        return DenverResultsPage

    def click_la_tile(self):
        self.click(10, "cssSelector", "div.city-tile-los-angeles")

        return LAResultsPage

    def click_nashville_tile(self):
        self.click(10, "cssSelector", "div.city-tile-nashville")
        return NashvilleResultsPage


    def click_ny_tile(self):
        self.click(10, "cssSelector", "div.city-tile-new-york")
        return NYResultsPage

    def click_philadelphia_tile(self):
        self.click(10, "cssSelector", "div.city-tile-philadelphia")
        return PhiladelphiaResultsPage

    def click_portland_tile(self):
        self.click(10, "cssSelector", "div.city-tile-portland")
        return PortlandResultsPage

    def click_seattle_tile(self):
        self.click(10, "cssSelector", "div.city-tile-seattle")
        return SeattleResultsPage
