import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import LOGIN_URL


@pytest.mark.smoke
class TestLogout:
    def test_logout(self, logged_in_driver):
        dashboard = DashboardPage(logged_in_driver)
        dashboard.logout()
        assert "/auth/login" in dashboard.get_current_url()
