import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Scrapper:
    def __init__(self):
        self.base_url: str = "https://unmsm.edu.pe"
        self.auth_token: str = None
        self.driver: webdriver = webdriver.Firefox()

    def login(self):
        user, password = self.get_credentials()
        main_page = self.access_login_page(user, password)
        soup = BeautifulSoup(main_page, "html.parser")

    def access_login_page(self, user: str, password: str):
        login_url = "https://tramiteonline.unmsm.edu.pe/sgdfd/mat/login"
        self.driver.get(login_url)
        user_input = self.driver.find_element(By.ID, "usuario")
        password_input = self.driver.find_element(By.NAME, "clave")
        login_btn = self.driver.find_element(By.ID, "btnIniciarSesion")
        user_input.send_keys(user)
        password_input.send_keys(password)
        login_btn.click()
        html = self.driver.page_source
        return html
