import pytest
import guvi
from selenium.webdriver.common.by import By

g = guvi.Guvi()
url = "https://www.zenclass.in"
queryTitle = "Guvi Python AT – 1 &2 Automation Project"
queryDescription = "This is a Project Test Code Running for the Python Automation – 1&2 Project Given by mentor Mr. " \
                   "Suman Gangopadhyay. "


# test for zen login
@pytest.mark.first
def test_login():
    g.login(url)
    assert g.driver.current_url == "https://www.zenclass.in/class"


# test for extracting data from lhs of zen class page
@pytest.mark.first
def test_lhsData():
    print(g.getLhsData())


# test to check query creation
@pytest.mark.repeat(1)
def test_createquery():
    g.createQuery(queryTitle, queryDescription)
    assert g.driver.find_element(by=By.XPATH,
                                 value="//*[@id='root']/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/span").text.__contains__(
        queryTitle)
