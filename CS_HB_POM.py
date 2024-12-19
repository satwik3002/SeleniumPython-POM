from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Page Object Classes
class BasePage:
    def init(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "/html/body/main/section/div/div/div/form/div[2]/button").click()

class HomePage(BasePage):
    def navigate_to_category(self, category):
        menu = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, category))
        )
        ActionChains(self.driver).move_to_element(menu).click().perform()

class ProductPage(BasePage):
    def add_product_to_basket(self, product_name):
        product = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, product_name))
        )
        product.click()
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[10]/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]/div[3]/div[2]/button[1]").click()

class BasketPage(BasePage):
    def verify_products_in_basket(self, product_names):
        basket_items = self.driver.find_elements(By.CLASS_NAME, "basket-item")
        basket_texts = [item.text for item in basket_items]
        for product in product_names:
            assert product in basket_texts, f"{product} not found in basket."

    def verify_totals(self, expected_subtotal, expected_total):
        subtotal = self.driver.find_element(By.ID, "basket-subtotal").text
        total = self.driver.find_element(By.ID, "basket-total").text
        assert float(subtotal) == expected_subtotal, "Subtotal mismatch."
        assert float(total) == expected_total, "Total mismatch."