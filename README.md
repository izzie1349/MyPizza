# TestAutomation
Simple tests for MyPizza

Dependencies
============
This project uses Selenium in order to control the browser.
There are many testrunners, but in order to keep simplicity, I
opted in keeping unittest.

I encourage to be in a virtualenv for the installations.

* run `pip  install -r requirements.txt`

This will install Selenium.


You also need to overwrite your PYTHONPATH.  In the root directory:
* run `export PYTHONPATH='.'`


Running tests
===================
From the root directory:

* run `python tests/TestResultsPerCity.py`
