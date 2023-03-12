from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# Set the path of the ChromeDriver executable
driver = webdriver.Chrome(r"C:\Users\JOSHNA\Downloads\driver\chromedriver.exe")
time.sleep(5)

# Navigate to the homepage of the website
driver.get("https://www.thesparksfoundationsingapore.org/")
print("")
print("Checking for test cases")
print("")
time.sleep(5)
################## test case -1 ##############################
print("Test case -1")
if(driver.title):
    print("Title verified successfully:",driver.title)
else:
    print("Title verification failed")
time.sleep(5)
print("")
################## test case -2 ##############################
print("Test case -2")
try:
    element = driver.find_element(By.PARTIAL_LINK_TEXT, 'The Sparks Foundation')
    element.click()
    print("Home page link verified successfully")
except NoSuchElementException:
    print("Home page link verification failed")
time.sleep(5)
print("")
################## test case -3 ##############################
print("Test case -3")
try:
    element = driver.find_element(By.CLASS_NAME, 'navbar')
    print("Navigation bar verified successfully")
except NoSuchElementException:
    print("Navigation bar verification failed")
time.sleep(5)
print("")
################## test case -4 ##############################
print("Test case -4")
for i in range(0, 1800, 200):
    driver.execute_script("window.scrollTo(0, {0});".format(i))
    time.sleep(1)
print("Scrolled down")
print("")
################## test case -5 ##############################
print("Test case -5")
try:
    element = driver.find_element(By.ID,"toTopHover")
    element.click()
    time.sleep(1)
    print("Scrolled up")
except NoSuchElementException:
    print("Scroll up failed")
print("")
################## test case -6 ##############################
print("Test case -6")
try:
    element = driver.find_element(By.LINK_TEXT,('About Us'))
    element.click()
    time.sleep(1)
    element = driver.find_element(By.LINK_TEXT,('News'))
    element.click()
    time.sleep(1)
    print("About Us page visited successfully")
except NoSuchElementException:
    print("About Us page not visited")
print("")
################## test case -7 ##############################
print("Test case -7")
try:
    element = driver.find_element(By.LINK_TEXT,('Policies and Code'))
    element.click()
    time.sleep(1)
    element = driver.find_element(By.LINK_TEXT,('Policies'))
    element.click()
    time.sleep(1)
    print("Policies and Code page visited successfully")
except NoSuchElementException:
    print("Policies and Code page not visited")
print("")
################## test case -8 ##############################
print("Test case -8")
try:
    element = driver.find_element(By.LINK_TEXT,('Programs'))
    element.click()
    time.sleep(1)
    element = driver.find_element(By.LINK_TEXT,('Workshops'))
    element.click()
    time.sleep(1)
    print("Programs page visited successfully")
except NoSuchElementException:
    print(" Programs page not visited")
print("")
################## test case -9 ##############################
print("Test case -9")
try:
    element = driver.find_element(By.LINK_TEXT,('Join Us'))
    element.click()
    time.sleep(1)
    element = driver.find_element(By.LINK_TEXT,('Internship Positions'))
    element.click()
    time.sleep(1)
    print("Join Us page visited successfully")
except NoSuchElementException:
    print("Join Us page not visited")
print("")
################## test case -10 ##############################
print("Test case -10")
try:
    element = driver.find_element(By.LINK_TEXT,('Contact Us'))
    element.click()
    time.sleep(1)
    print("Contact Us page visited successfully")
except NoSuchElementException:
    print("Contact Us page (Internship Positions) not visited")
print("")
################## test case -11 ##############################
print("Test case -11")
try:
    element = driver.find_element(By.LINK_TEXT,('Join Us'))
    element.click()
    time.sleep(1)
    element = driver.find_element(By.LINK_TEXT,('Why Join Us'))
    element.click()
    time.sleep(1) 
    print("Typing name automatically")
    input_element = driver.find_element(by='name', value='Name')
    time.sleep(2)
    input_element.send_keys('Joshna')
    time.sleep(2)
    input_element = driver.find_element(by='name', value='Email')
    input_element.send_keys('chjoshna145@gmail.com')
    time.sleep(2)
    print("Typing Email automatically")
    time.sleep(1)
    print("Selecting Student")
    select=Select(driver.find_element(By.CLASS_NAME, 'form-control'))
    time.sleep(2)
    select.select_by_visible_text('Student')
    time.sleep(1)
    element = driver.find_element(By.CLASS_NAME,('button-w3layouts'))
    element.click()
    print('Form Verified successfully')
except NoSuchElementException:
    print("Form verification failed")
print("")
time.sleep(1)
################## test case -12 ##############################
print("Test case -12")
try:
    element = driver.find_element(By.XPATH, "//*[@id=\"home\"]/div/div[1]/h1/a/img")
    element.click()
    logo=driver.find_element(By.XPATH, "//*[@id=\"home\"]/div/div[1]/h1/a/img")
    if logo.is_displayed():
        print("Logo Verified")
except NoSuchElementException:
    print("Logo verification failed")
print("")
################## test case -13 ##############################
print("Test case -13 ")
try:
    element = driver.find_element(By.LINK_TEXT,('Contact Us'))
    element.click()
    time.sleep(1)
    for i in range(0, 450):
        driver.execute_script("window.scrollTo(0, {0});".format(i))
    add =driver.find_element(By.XPATH,('/html/body/div[2]/div/div/div[2]'))
    time.sleep(1)
    if add.is_displayed():
        print("Address section is displayed successfully")
        print("")
    else:
        print("Address section is not displayed")
        print("")
    ################## test case -14 ##############################
    print("Test case -14")
    loc =driver.find_element(By.XPATH,('/html/body/div[2]/div/div/div[2]/div[1]/i'))
    time.sleep(1)
    if loc.is_displayed():
        print("Location symbol is displayed successfully")
        print("")
    else:
        print("Location symbol is not displayed")
        print("")
    ################## test case -15 ##############################
    print("Test case -15")
    google_map =driver.find_element(By.XPATH,('/html/body/div[3]/iframe'))
    time.sleep(1)
    for i in range(450, 800):
        driver.execute_script("window.scrollTo(0, {0});".format(i))
    if google_map.is_displayed():
        print("Google Map is displayed successfully")
        print("")
    else:
        print("Google Map is not displayed")
        print("")
except NoSuchElementException:
    print("Contact Us page not visited")
    
    
    
    
    
    








    