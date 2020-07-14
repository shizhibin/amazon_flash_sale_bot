from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)


# enter your amazon username and password here

username = ''  # ex: username='abc@gmail.com' or username='987654321'
password = ''  # ex : password='passwordHere'


login_url = 'https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_BottomSectionFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1'


# item link you want to order
item_url = ''


address_xpath = '//*[@id="address-book-entry-0"]/div[2]/span/a'
# if its your second address in your amazon account use this address xpath='//*[@id="address-book-entry-1"]/div[2]/span/a'
# in simple put (n-1) value in place of //*[@id="address-book-entry-___________________"]/div[2]/span/a where n is address number you want to deliver from your amazon account
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

wait_for_checkout_page = wait.until(
    presence_of_element_located((By.XPATH, '//*[@id="checkoutDisplayPage"]/div/div[2]/div[1]/h1')))
javaScript = '''

window.addEventListener('load', () => {
  document.querySelectorAll('input[type="radio"]')[6].checked = true;
  document.querySelectorAll('form')[0].submit()

});
'''
driver.execute_script(javaScript)
review_order = wait.until(
    presence_of_element_located((By.XPATH, '//*[@id="placeYourOrder"]/span/input')))
review_order.click()

# driver.quit()
