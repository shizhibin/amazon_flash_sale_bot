from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
# all variables
username = '8217628886'
password = '*$implyGood1'
login_url = 'https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_BottomSectionFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1'
item_url = 'https://www.amazon.in/dp/B07PKXJN7J/ref=cm_sw_r_wa_apa_i_VMxdFbDKQYYQY'
address_no = 0  # specifies address number in your amazon
address_xpath = '//*[@id="address-book-entry-0"]/div[2]/span/a'

# Navigate to url
wait = WebDriverWait(driver, 10)
driver.get(login_url)
driver.find_element_by_xpath(
    '//*[@id="ap_email"]').send_keys(username + Keys.RETURN)
driver.find_element_by_xpath(
    '//*[@id="ap_password"]').send_keys(password + Keys.RETURN)
driver.get(item_url)

while not driver.find_elements_by_xpath('//*[@id="buy-now-button"]'):
    driver.refresh()

driver.find_element_by_xpath(
    '//*[@id="buy-now-button"]').click()
delivery_to_this = wait.until(
    presence_of_element_located((By.XPATH, address_xpath)))
delivery_to_this.click()

print(driver.find_element_by_id('pp-VZs2zS-174').is_selected())
# driver.find_element_by_xpath('//*[@id="pp-rI5NFq-184"]/span/input').click()


# driver.quit()
#address-book-entry-0 > div.ship-to-this-address.a-button.a-button-primary.a-button-span12.a-spacing-medium > span > a
#address-book-entry-1 > div.ship-to-this-address.a-button.a-button-primary.a-button-span12.a-spacing-medium > span > a
