# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = WebDriver()
#driver.implicitly_wait(60)


def is_alert_present(driver):
    try:
        driver.switch_to_alert().text
        return True
    except:
        return False


def print_header(param):
    print('----------------------------')
    print('     {}'.format(param))
    print('----------------------------')
    print('')

def check_for_forsee():
    try:
        wait = WebDriverWait(driver, 3)
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No, thanks")))
        driver.find_element_by_link_text("No, thanks").click()
        print('    Handled Foresee ad')
    except Exception, e:
        print("    Tested for Foresee")


def run_synth_script():
    try:
        success = True

        print("Loading home page")
        driver.get("http://www.gnc.com/home/index.jsp")
        check_for_forsee()

        print("Search for protein")
        driver.find_element_by_id("search-box").click()
        driver.find_element_by_id("search-box").clear()
        driver.find_element_by_id("search-box").send_keys("protein")
        driver.find_element_by_id("searchButton").click()

        print("Select first item and add to cart")
        check_for_forsee()

        driver.find_element_by_xpath("//li[@id='prodSummary-41802466']/div/a/img").click()
        driver.find_element_by_link_text("ADD TO CART ▶").click()

        print('Go To cart and start checkout')
        check_for_forsee()

        driver.find_element_by_link_text("Go to Cart").click()
        driver.find_element_by_css_selector("button.checkout.img").click()
        driver.find_element_by_id("continue").click()

        print('Complete buyer info')
        ActionChains(driver).double_click(driver.find_element_by_id("billingAddress.address.firstName")).perform()
        driver.find_element_by_id("billingAddress.address.firstName").click()
        driver.find_element_by_id("billingAddress.address.firstName").clear()
        driver.find_element_by_id("billingAddress.address.firstName").send_keys("AppD")
        driver.find_element_by_id("billingAddress.address.lastName").click()
        driver.find_element_by_id("billingAddress.address.lastName").clear()
        driver.find_element_by_id("billingAddress.address.lastName").send_keys("Synth")
        driver.find_element_by_id("billingAddress.address.address1").click()
        driver.find_element_by_id("billingAddress.address.address1").clear()
        driver.find_element_by_id("billingAddress.address.address1").send_keys("300 6th Avenue")
        driver.find_element_by_id("billingAddress.address.city").click()
        driver.find_element_by_id("billingAddress.address.city").clear()
        driver.find_element_by_id("billingAddress.address.city").send_keys("Pittsburgh")
        if not driver.find_element_by_xpath("//select[@id='billingAddress.address.state']//option[48]").is_selected():
            driver.find_element_by_xpath("//select[@id='billingAddress.address.state']//option[48]").click()
        driver.find_element_by_id("billingAddress.address.postalCode").click()
        driver.find_element_by_id("billingAddress.address.postalCode").clear()
        driver.find_element_by_id("billingAddress.address.postalCode").send_keys("15222")
        driver.find_element_by_id("billing-phone-areacode").click()
        driver.find_element_by_id("billing-phone-areacode").clear()
        driver.find_element_by_id("billing-phone-areacode").send_keys("123")
        driver.find_element_by_id("billing-phone-exchange").click()
        driver.find_element_by_id("billing-phone-exchange").clear()
        driver.find_element_by_id("billing-phone-exchange").send_keys("123")
        driver.find_element_by_id("billing-phone-number").click()
        driver.find_element_by_id("billing-phone-number").clear()
        driver.find_element_by_id("billing-phone-number").send_keys("1234")
        driver.find_element_by_id("billingAddress.emailAddress").click()
        driver.find_element_by_id("billingAddress.emailAddress").clear()
        driver.find_element_by_id("billingAddress.emailAddress").send_keys("synthtest@appd.com")
        driver.find_element_by_id("billingAddress.emailAddress").click()
        driver.find_element_by_id("billingAddress.emailAddress").clear()
        driver.find_element_by_id("billingAddress.emailAddress").send_keys("synthtest@appdnotemail.com")
        #driver.find_element_by_css_selector("div.continue.sprite").click()
        driver.save_screenshot("last")
        print('Verify page info')

    finally:
        driver.quit()
        if not success:
            raise Exception("Test failed.")


def main():
    print_header("GNC Product Search")
    run_synth_script()

if __name__ == '__main__':
    main()
