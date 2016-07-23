from Constants import MP_Constants
from BaseTestCase import BaseTestCase
from pages.WelcomePage import WelcomePage
from pages.AtlantaResultsPage import AtlantaResultsPage
from pages.BayAreaResultsPage import BayAreaResultsPage
from pages.BostonResultsPage import BostonResultsPage
from pages.ChicagoResultsPage import ChicagoResultsPage
from pages.DCResultsPage import DCResultsPage
from pages.DenverResultsPage import DenverResultsPage
from pages.LAResultsPage import LAResultsPage
from pages.NashvilleResultsPage import NashvilleResultsPage
from pages.NYResultsPage import NYResultsPage
from pages.PhiladelphiaResultsPage import PhiladelphiaResultsPage
from pages.PortlandResultsPage import PortlandResultsPage
from pages.SeattleResultsPage import SeattleResultsPage
from pages.BasePage import BasePage
import unittest
import time

class TestResults(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(TestResults, self).setUp()
        self.navigate_to_page(MP_Constants['Base_URL'])

    def test_results_atlanta(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_atlanta_tile()

        atlanta_page = AtlantaResultsPage(self.driver)
        atlanta_page.verify_results()

    def test_results_bayarea(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_bayarea_tile()

        bayarea_page = BayAreaResultsPage(self.driver)
        bayarea_page.verify_results()

    def test_results_boston(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_boston_tile()

        boston_page = BostonResultsPage(self.driver)
        boston_page.verify_results()

    def test_results_chicago(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_chicago_tile()

        chicago_page = ChicagoResultsPage(self.driver)
        chicago_page.verify_results()

    def test_results_DC(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_dc_tile()

        dc_page = DCResultsPage(self.driver)
        dc_page.verify_results()

    def test_results_denver(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_denver_tile()

        denver_page = DenverResultsPage(self.driver)
        denver_page.verify_results()

    def test_results_LA(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_la_tile()

        la_page = LAResultsPage(self.driver)
        la_page.verify_results()

    def test_results_nashville(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_nashville_tile()

        nashville_page = NashvilleResultsPage(self.driver)
        nashville_page.verify_results()

    def test_results_NY(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_ny_tile()

        ny_page = NYResultsPage(self.driver)
        ny_page.verify_results()

    def test_results_philadelphia(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_philadelphia_tile()

        philadelphia_page = PhiladelphiaResultsPage(self.driver)
        philadelphia_page.verify_results()

    def test_results_portland(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_portland_tile()

        portland_page = PortlandResultsPage(self.driver)
        portland_page.verify_results()

    def test_results_seattle(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_seattle_tile()

        seattle_page = SeattleResultsPage(self.driver)
        seattle_page.verify_results()

    def tearDown(self):
        super(TestResults, self).tearDown()

if __name__ == "__main__":
   unittest.main()
