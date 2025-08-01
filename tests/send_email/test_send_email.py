import os
from datetime import datetime, timezone

import pytest
from pytest_bdd import given, scenarios, then, when

from support.context import Context
from support.test_config import test_config

scenarios('send_email.feature')


@pytest.fixture
def email_data():
    return {
        "subject": f"Test Email {datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
        "body": "Hi,\n\nThis is a test email.\n\nKind regards,\n\nJaroslav",
        "attachment_path": os.path.abspath("test_data/attachment.txt")
    }


@given("the user is logged into the application")
def user_logs_in(context: Context):
    context.login_page.open(test_config["BaseUrl"])
    context.login_page.login_to_email(test_config["Username"], test_config["Password"])


@when("the user sends an email with an attachment")
def user_sends_email(context: Context, email_data):
    context.home_page.send_email(
        recipient=test_config["RecipientEmail"],
        subject=email_data["subject"],
        email_body=email_data["body"],
        attachment_path=email_data["attachment_path"]
    )


@then("the email should be sent successfully")
def verify_email_sent(context: Context, email_data):
    context.home_page.check_that_email_was_sent(
        recipient=test_config["RecipientEmail"],
        subject=email_data["subject"]
    )


@then("the recipient should receive the email")
def verify_email_received(context: Context, email_data):
    """
    # Configure your own Gmail account for testing and update the credentials.json file accordingly.

    context.gmail_client.check_email_received(
        expected_sender=test_config["UserEmail"],
        expected_subject=email_data["subject"],
        timeout_seconds=30
    )
    """
    context.home_page.log_out()
