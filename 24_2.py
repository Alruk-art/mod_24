import time
def test_1(selenium):
    selenium.get ('https://pytest-selenium.readthedocs.io/en/latest/user_guide.html')
    xpath_conf_file = '(//*[text()="configuration file"])[4]'
    element = selenium.find_element_by_xpath (xpath_conf_file)

    element.click ()
    time.sleep (5)

