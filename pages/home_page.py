from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.create_email_button: Locator = self.page.locator('a[data-command="compose:new"]')
        self.send_email_button: Locator = self.page.locator('button[data-command="compose:send"]:not([class="mobile"])')
        self.recipient_field: Locator = self.page.locator('input[placeholder="Komu…"]')
        self.subject_field: Locator = self.page.locator('input[placeholder="Předmět…"]')
        self.email_body_field: Locator = self.page.locator('div[placeholder="Text e-mailu…"]')
        self.file_upload_button: Locator = self.page.locator('button[title="Přiložit soubory"][tabindex="0"]')
        self.attachment: Locator = self.page.locator('a[class*="preview"][href]')
        self.sent_email_nav: Locator = self.page.locator('a[title="Odeslané"]')
        self.last_sent_email_name: Locator = self.page.locator('(//a[@class="name"])[1]')
        self.last_sent_email_subject: Locator = self.page.locator('(//a[@class="subject"])[1]')
        self.notification: Locator = self.page.locator('wm-notification')
        self.login_widget: Locator = self.page.locator('szn-login-widget[data-dot="login-badge"]')
        self.login_section: Locator = self.page.locator('#login').first
        self.users_button: Locator = self.page.locator('#badge').first
        self.log_out_button: Locator = self.page.locator('[data-dot="logout"]').first

    def send_email(self, recipient, subject, email_body, attachment_path):
        self.create_email_button.click()
        self.recipient_field.fill(recipient)
        self.subject_field.fill(subject)
        self.email_body_field.fill(email_body)
        with self.page.expect_file_chooser() as fc_info:
            self.file_upload_button.click()
            file_chooser = fc_info.value
            file_chooser.set_files(attachment_path)
        expect(self.attachment).to_be_visible()
        self.send_email_button.click()
        expect(self.notification).to_be_visible()

    def check_that_email_was_sent(self, recipient, subject):
        self.sent_email_nav.click()
        expect(self.last_sent_email_name).to_have_text(recipient)
        expect(self.last_sent_email_subject).to_have_text(subject)

    def log_out(self):
        self.users_button.click()
        self.log_out_button.click()
        expect(self.login_section).to_be_visible()
