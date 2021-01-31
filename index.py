# Marc Orfila Carreras
# https://github.com/MarcOrfilaCarreras/Mi-Fit-Data-Downloader
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#We open the website
driver = webdriver.Chrome("C:/Users/marco/chromedriver.exe")
driver.get("https://mifit.huami.com/t/account_mifit")

wait = WebDriverWait(driver, 10)

#We choose to download the data
export_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'output')))
export_button.click()

#We accept the risks
accept_button = wait.until(EC.element_to_be_clickable((By.ID, 'step1')))
accept_button.click()

#We choose Mi Account
mi_account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'mi-confirm-btn')))
mi_account_button.click()

#We fill the input with the mail in the file username.txt
f = open ('mail_mi_fit.txt','r')
mail_mi_account = f.read()
f.close()

select = driver.find_element_by_id("username")
select.clear()
select.send_keys(mail_mi_account)

#We fill the input with the password in the file password.txt
f = open ('password_mi_fit.txt','r')
password_mi_account = f.read()
f.close()

select = driver.find_element_by_id("pwd")
select.clear()
select.send_keys(password_mi_account)

#We click the button to login into the account
accept_button = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
accept_button.click()

#we want all the data
select_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='USER']")))
select_button.click()

select_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='ACTIVITY']")))
select_button.click()

select_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='SLEEP']")))
select_button.click()

select_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='HEARTRATE']")))
select_button.click()

select_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='BODY']")))
select_button.click()

select_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='SPORT']")))
select_button.click()

#We select the dates to download teh data

select_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "datePick")))
select_button.click()

select_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__day--001')))
select_button.click()

#We clicked the OK button
select_button = wait.until(EC.element_to_be_clickable((By.ID, 'ok')))
select_button.click()