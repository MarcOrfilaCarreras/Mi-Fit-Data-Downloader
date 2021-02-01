# Marc Orfila Carreras
# https://github.com/MarcOrfilaCarreras/Mi-Fit-Data-Downloader
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

now = datetime.now()
day = now.day

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

#We select the dates to download the data

select_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "datePick")))
select_button.click()

if day == 1:
	select_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__day--outside-month')))
	select_button.click()
if day != 1:
	select_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__day--001')))
	select_button.click()

select_button = driver.find_elements_by_xpath('(//*[@class="datePick"])')[-1].click()

select_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__day--today')))
select_button.click()

#We clicked the OK button
select_button = wait.until(EC.element_to_be_clickable((By.ID, 'ok')))
select_button.click()

#We introduce our mail
select = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
select.clear()
select.send_keys(mail_mi_account)

#We save the code in a file
code_mi_fit = open("code_mi_fit.txt","w")
for elem in driver.find_elements_by_xpath('.//span'):
    code_mi_fit.write(elem.text)
code_mi_fit.close()

#We read the code from the file
code_mi_fit = open("code_mi_fit.txt","r")
useless = code_mi_fit.read(6)
code1 = code_mi_fit.read(7)
code2 = code_mi_fit.read(8)
code3 = code_mi_fit.read(9)
code4 = code_mi_fit.read(10)
code_mi_fit.close()

code = code1 + code2 + code3 + code4

#We enter the code
select = wait.until(EC.element_to_be_clickable((By.ID, 'code')))
select.clear()
select.send_keys(code)

#We send the email
send_email_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'sendEmailBtn')))
send_email_button.click()

#We finish the task
time.sleep(1)
driver.close()