import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.smoke
class TestDashboard:
    def test_dashboard_title_displayed(self, logged_in_driver):
        dashboard = DashboardPage(logged_in_driver)
        assert dashboard.is_dashboard_displayed()

    def test_dashboard_title_text(self, logged_in_driver):
        dashboard = DashboardPage(logged_in_driver)
        assert "Dashboard" in dashboard.get_dashboard_title()

    def test_user_menu_visible(self, logged_in_driver):
        dashboard = DashboardPage(logged_in_driver)
        assert dashboard.is_displayed(DashboardPage.USER_DROPDOWN)
