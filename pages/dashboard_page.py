from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class DashboardPage(BasePage):
    DASHBOARD_TITLE = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6")
    USER_DROPDOWN = (By.CSS_SELECTOR, ".oxd-userdropdown")
    LOGOUT_LINK = (By.XPATH, "//a[contains(@href,'logout')]")
    SIDEBAR_DASHBOARD = (By.CSS_SELECTOR, "a[href='/web/index.php/dashboard']")
    SIDEBAR_ADMIN = (By.CSS_SELECTOR, "a[href='/web/index.php/admin']")
    SIDEBAR_PIM = (By.CSS_SELECTOR, "a[href='/web/index.php/pim']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_displayed(self):
        return self.is_displayed(self.DASHBOARD_TITLE)

    def get_dashboard_title(self):
        return self.get_text(self.DASHBOARD_TITLE)

    def click_user_menu(self):
        self.click(self.USER_DROPDOWN)

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()

    def logout(self):
        self.click_user_menu()
        self.click_logout()

    def is_sidebar_visible(self):
        return self.is_displayed(self.SIDEBAR_DASHBOARD)
