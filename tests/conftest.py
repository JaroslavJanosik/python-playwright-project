import os

import pytest
import pytest_html
from playwright.sync_api import Page

from support.context import Context


@pytest.fixture(autouse=True)
def context(page: Page):
    return Context(page)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    screenshot_dir = os.path.join("reports", "html_report", "screenshots")

    # Check if the test was a failure or a skipped xfail
    is_failed_or_skipped = (report.when in ["call", "setup"]) and (
            (report.failed and not getattr(report, "wasxfail", False)) or
            (report.skipped and getattr(report, "wasxfail", False))
    )

    if is_failed_or_skipped:
        page = item.funcargs.get("page")
        if page:
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")

            try:
                # Capture screenshot
                page.screenshot(path=screenshot_path)

                # Attach screenshot to HTML report
                screenshot_report_path = os.path.join("screenshots", f"{item.name}.png")
                html_tag = (
                    f'<div class="image"><a href="{screenshot_report_path}">'
                    f'<img src="{screenshot_report_path}" alt="screenshot" style="width:300px;height:auto;"></a></div>'
                )
                report.extra = getattr(report, "extra", []) + [pytest_html.extras.html(html_tag)]

            except Exception as e:
                print(f"Failed to capture screenshot for {item.name}: {e}")
