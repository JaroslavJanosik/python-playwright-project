from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage
from support.helpers.gmail_client import GmailClient


class Context:
    def __init__(self, page: Page):
        self.gmail_client = GmailClient()
        self.home_page = HomePage(page)
        self.login_page = LoginPage(page)
