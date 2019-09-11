from selenium import webdriver
from time import sleep

class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'gLFyf' # class
        # self.search_bar = 'q' # name
        self.btn_search = 'btnK' # name
        self.btn_lucky = 'btnI' # name
        self.gmail = 'gb_d'

    def navigate(self):
        self.driver.get(self.url)

        # Realiza pesquisa
    def search(self, word):
        # self.driver.find_element_by_class_name(self.search_bar).send_keys(word)
        
        self.driver.find_element_by_xpath('//input[@name="q"]').send_keys(word)
        sleep(2)
        self.driver.find_element_by_name(self.btn_lucky).submit()

    def email(self):
        # Clicar no E-mail
        self.driver.find_element_by_class_name(self.gmail).click()

ff = webdriver.Firefox()
g = Google(ff)
g.navigate()
g.search('Campus Party Natal')
g.email()