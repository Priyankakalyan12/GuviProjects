from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Guvi:
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)

    # method to login to zen portal
    def login(self, url):
        emailId = "guddu.bk12@gmail.com"
        pwd = "Guvipriyanka12#"
        self.driver.get(url)

        emailBox = self.driver.find_element(by=By.XPATH,
                                            value="//div[@id='root']//div[@class='form-group mt-2']//input["
                                                  "@class='form-control']")
        emailBox.send_keys(emailId)

        pwdBox = self.driver.find_element(by=By.XPATH,
                                          value="//div[@id='root']//div[@class='form-group mt-1']//input["
                                                "@class='form-control']")
        pwdBox.send_keys(pwd)

        loginBtn = self.driver.find_element(by=By.XPATH, value="//button[@type='submit']")
        loginBtn.click()
        time.sleep(2)

    # method to create a query in zen portal
    def createQuery(self, queryTitle, queryDescription):
        queryIcon = self.driver.find_element(by=By.XPATH, value="//*[@id='root']/div[1]/nav/ul/div[6]")
        queryIcon.click()

        createQueryBtn = self.driver.find_element(by=By.XPATH, value="//*[@id='root']/div[2]/div/div[1]/div[1]/button")
        self.driver.execute_script("arguments[0].click();", createQueryBtn)

        cancelBtn = self.driver.find_element(by=By.XPATH,
                                             value="/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section["
                                                   "3]/div[2]/button[1]")
        cancelBtn.click()

        # select category
        select = Select(
            self.driver.find_element(by=By.XPATH, value="//select[@class='formInputs'and @name='category']"))
        select.select_by_index(1)

        # select subcategory
        select = Select(
            self.driver.find_element(by=By.XPATH, value="//select[@class='formInputs'and @name='subcategory']"))
        select.select_by_index(1)

        # select language
        select = Select(
            self.driver.find_element(by=By.XPATH, value="//select[@class='formInputs'and @name='language']"))
        select.select_by_index(1)

        # enter queryTitle
        title = self.driver.find_element(by=By.XPATH,
                                         value="//*[@id='root']/div[2]/div/div[2]/div/div/form/div[5]/div/input")
        title.send_keys(queryTitle)

        # enter queryDescription
        description = self.driver.find_element(by=By.XPATH,
                                               value="//*[@id='root']/div[2]/div/div[2]/div/div/form/div[5]/textarea")
        description.send_keys(queryDescription)

        createBtn = self.driver.find_element(by=By.XPATH,
                                             value="//*[@id='root']/div[2]/div/div[2]/div/div/form/div[13]/div/button")
        createBtn.click()
