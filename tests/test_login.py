import pytest
from pages.login_page import LoginPage
from utils.config import BASE_URL, LOGIN_URL, USERNAME, PASSWORD


@pytest.mark.smoke
class TestLogin:
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open(LOGIN_URL)
        login_page.login(USERNAME, PASSWORD)
        login_page.wait_for_dashboard()
        assert "/dashboard" in login_page.get_current_url()

    def test_invalid_username(self, driver):
        login_page = LoginPage(driver)
        login_page.open(LOGIN_URL)
        login_page.login("InvalidUser", PASSWORD)
        assert "Invalid credentials" in login_page.get_error_message()

    def test_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open(LOGIN_URL)
        login_page.login(USERNAME, "WrongPass123")
        assert "Invalid credentials" in login_page.get_error_message()

    def test_empty_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.open(LOGIN_URL)
        login_page.login("", "")
        assert login_page.is_login_page_displayed()
