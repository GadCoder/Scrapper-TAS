from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthHandler:
    def __init__(self):
        self.base_url: str = "https://unmsm.edu.pe"
        self.driver: webdriver = self.create_driver()
        self.user_agent: str = None

    def create_selenium_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--enable-javascript")
        options.add_experimental_option("prefs", {"intl.accept_languages": "en"})
        options.add_argument("--headless")
        options.add_argument("--incognito")
        options.add_argument("--nogpu")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1280,1280")
        options.add_argument("--no-sandbox")
        options.add_argument("--enable-javascript")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        return options

    def create_driver(self):
        options = self.create_selenium_options()
        ua = UserAgent()
        user_agent = ua.random
        self.user_agent = user_agent
        driver = webdriver.Chrome(options=options)
        driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        driver.execute_cdp_cmd(
            "Network.setUserAgentOverride", {"userAgent": user_agent}
        )
        return driver

    def get_auth_token(self, user: str, password: str) -> str:
        current_user = user
        current_password = password
        try:
            main_page = self.access_login_page(
                user=current_user, password=current_password
            )
            soup = BeautifulSoup(main_page, "html.parser")
            token_tag = soup.find("meta", attrs={"name": "_t"})
            token = token_tag["content"]
            if token is not None and token:
                print("Token: ", token)
                return token
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def access_login_page(self, user: str, password: str):
        login_url = "https://tramiteonline.unmsm.edu.pe/sgdfd/mat/login"
        self.driver.get(login_url)
        user_input = self.driver.find_element(By.ID, "usuario")
        password_input = self.driver.find_element(By.NAME, "clave")
        login_btn = self.driver.find_element(By.ID, "btnIniciarSesion")
        user_input.send_keys(user)
        password_input.send_keys(password)
        login_btn.click()
        user_img = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "imgUsuario"))
        )
        html = self.driver.page_source
        return html
