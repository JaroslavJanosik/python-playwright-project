from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username: Locator = self.page.locator('#login-username')
        self.password: Locator = self.page.locator('#login-password')
        self.sign_in_button: Locator = self.page.locator('button[data-arrow-down="#login-username"]')

    def open(self, url: str):
        self.page.goto(url)

    def login_to_email(self, username: str, password: str):
        self.username.fill(username)
        self.sign_in_button.click()
        self.password.fill(password)
        self.sign_in_button.click()
