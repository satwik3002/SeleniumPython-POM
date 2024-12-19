from selenium import webdriver

from CS_HB_POM import LoginPage, HomePage, ProductPage, BasketPage

def test_case():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://auth.hollandandbarrett.com/u/login")

    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    basket_page = BasketPage(driver)

    # Test Case 1
    login_page.login("satwikkatamaraju@gmail.com", "Y2#ssv@Xp/xP8Wt")
    home_page.navigate_to_category("Vitamins & Supplements")
    product_page.add_product_to_basket("Vitamin C")
    home_page.navigate_to_category("Vegan")
    product_page.add_product_to_basket("Vegan Chocolate")
    basket_page.verify_products_in_basket(["Vitamin C", "Vegan Chocolate"])

    # Test Case 2
    home_page.navigate_to_category("Vitamins & Supplements")
    product_page.add_product_to_basket("Vitamin C")
    product_page.add_product_to_basket("Vitamin C")
    home_page.navigate_to_category("Vegan")
    product_page.add_product_to_basket("Vegan Chocolate")
    product_page.add_product_to_basket("Vegan Chocolate")
    product_page.add_product_to_basket("Vegan Chocolate")
    basket_page.verify_products_in_basket([
        "Vitamin C", "Vegan Chocolate", "Vegan Chocolate", "Vegan Chocolate"
    ])
    basket_page.verify_totals(expected_subtotal=100.00, expected_total=110.00)

    driver.quit()


if __name__ == "__main__":
    test_case()
