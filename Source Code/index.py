# Marc Orfila Carreras
# https://github.com/MarcOrfilaCarreras/Mi-Fit-Data-Downloader
import tkinter
from tkinter import IntVar
from tkinter import PhotoImage
from tkinter.ttk import *
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# creating main tkinter window
master = tkinter.Tk()
master.geometry("500x500")
master.resizable(width = 0, height = 0)

master.title("Mi-Fit Data Downloader")

logo = PhotoImage(file = 'config/Logo.png')
master.iconphoto(False, logo)

# receive the mail and password
def getInformation():
    global mail
    global password

    mail = inputMail.get()
    password = inputPassword.get()

    boxValues()

# we put the values of the boxes in another variables to share it with the function startSelenium()    
def boxValues():
    global variableActivitySelenium
    global variablePersonalInformationSelenium
    global variableSleepingSelenium
    global variableHeartRateSelenium
    global variableBodyFatSelenium
    global variableTrainingSelenium

    variablePersonalInformationSelenium = variablePersonalInformation.get()
    variableActivitySelenium = variableActivity.get()
    variableSleepingSelenium = variableSleeping.get()
    variableHeartRateSelenium = variableHeartRate.get()
    variableBodyFatSelenium = variableBodyFat.get()
    variableTrainingSelenium = variableTraining.get()

    startSelenium()

#we change the text in the mail input
def setInputMiFitMail(text):
    inputMiFitMailText.set(text)

inputMiFitMailText = tkinter.StringVar()

#we change the text in the password input
def setInputMiFitPassword(text):
    inputMiFitPasswordText.set(text)

inputMiFitPasswordText = tkinter.StringVar()

#we change the text in the web driver input
def setInputWebDriverDirectory(text):
    inputWebDriverDirectoryText.set(text)

inputWebDriverDirectoryText = tkinter.StringVar()

#we save the configuration
def saveConfiguration():
    #we erase the content
    miFitMail = open("config/mi_fit_mail.txt","r+")
    miFitMail.truncate(0)
    miFitMail.close()

    miFitPassword = open("config/mi_fit_password.txt","r+")
    miFitPassword.truncate(0)
    miFitPassword.close()

    webDriverDirectory = open("config/web_driver_directory.txt","r+")
    webDriverDirectory.truncate(0)
    webDriverDirectory.close()

    #we write the new content
    global miFitMailNew
    miFitMail = open("config/mi_fit_mail.txt","a")
    miFitMailNew = inputMiFitMailText.get()
    miFitMail.write(miFitMailNew)
    miFitMail.close()

    global miFitPasswordNew
    miFitPassword = open("config/mi_fit_password.txt","a")
    miFitPasswordNew = inputMiFitPasswordText.get()
    miFitPassword.write(miFitPasswordNew)
    miFitPassword.close()

    global webDriverDirectoryNew
    webDriverDirectory = open("config/web_driver_directory.txt", "a")
    webDriverDirectoryNew = inputWebDriverDirectoryText.get()
    webDriverDirectory.write(webDriverDirectoryNew)
    webDriverDirectory.close()

#we open the configuration window
def openConfiguration():
    windowConfiguration = tkinter.Toplevel(master)
    windowConfiguration.geometry("500x500")
    windowConfiguration.resizable(width = 0, height = 0)
    windowConfiguration.title("Mi-Fit Data Downloader: Settings")

    logo = PhotoImage(file = 'config/Logo.png')
    windowConfiguration.iconphoto(False, logo)

    #input text for mail
    miFitMail = open("config/mi_fit_mail.txt", "r")
    miFitMailText = miFitMail.read()
    setInputMiFitMail(miFitMailText)
    miFitMail.close()

    #input text for password
    miFitPassword = open("config/mi_fit_password.txt", "r")
    miFitPasswordText = miFitPassword.read()
    setInputMiFitPassword(miFitPasswordText)
    miFitPassword.close()

    #input text for web driver
    webDriverDirectory = open("config/web_driver_directory.txt", "r")
    webDriverDirectoryText = webDriverDirectory.read()
    setInputWebDriverDirectory(webDriverDirectoryText)
    webDriverDirectory.close()

    # we create the widgets
    labelTitleConfiguration = tkinter.Label(windowConfiguration, text = "Mi-Fit Data Downloader: Settings", font = ("Helvetica", 16, "bold"))

    labelConfigurationMail = tkinter.Label(windowConfiguration, text = "Mail:", font = ("Helvetica", 12, "bold"))
    inputConfigurationMail = tkinter.Entry(windowConfiguration, font = ("Helvetica", 12), textvariable  = inputMiFitMailText)

    labelConfigurationPassword = tkinter.Label(windowConfiguration, text = "Password:", font = ("Helvetica", 12, "bold"))
    inputConfigurationPassword = tkinter.Entry(windowConfiguration, font = ("Helvetica", 12), textvariable  = inputMiFitPasswordText)

    labelConfigurationDriver = tkinter.Label(windowConfiguration, text = "Web Driver:", font = ("Helvetica", 12, "bold"))
    inputConfigurationDriver = tkinter.Entry(windowConfiguration, font = ("Helvetica", 12), textvariable  = inputWebDriverDirectoryText)

    buttonConfiguration = tkinter.Button(windowConfiguration, text = "Save", font = ("Helvetica", 12), command = saveConfiguration)

    labelCreator = tkinter.Label(windowConfiguration, text = "Marc Orfila Carreras", font = ("Helvetica", 8, "bold"), fg = "grey")

    labelLink = tkinter.Label(windowConfiguration, text = "https://github.com/MarcOrfilaCarreras/Mi-Fit-Data-Downloader", font = ("Helvetica", 8, "bold"), fg = "grey")


    # widget position
    labelTitleConfiguration.pack(pady = 20)
    labelConfigurationMail.place(x = 88, y = 60)
    inputConfigurationMail.place(x = 88, y = 95, height = 20, width = 310)

    labelConfigurationPassword.place(x = 88, y = 135)
    inputConfigurationPassword.place(x = 88, y = 170, height = 20, width = 310)
    
    labelConfigurationDriver.place(x = 88, y = 205)
    inputConfigurationDriver.place(x = 88, y = 240, height = 20, width = 310)

    labelLink.pack(side = tkinter.BOTTOM)
    labelCreator.pack(side = tkinter.BOTTOM)

    buttonConfiguration.place(x = 190, y = 390, height = 30, width = 120)


#########################################################################################################################
#########################################################################################################################

# We start the web scraping
def startSelenium():
    now = datetime.now()
    day = now.day

    #We open the website
    webDriver = open("config/web_driver_directory.txt", "r")

    driver = webdriver.Chrome(webDriver.read())
    driver.set_window_position(100000, 100000, windowHandle ='current')
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

    #We fill the input with the mail
    mail_mi_account = mail

    select = driver.find_element_by_id("username")
    select.clear()
    select.send_keys(mail_mi_account)

    #We fill the input with the password
    password_mi_account = password

    select = driver.find_element_by_id("pwd")
    select.clear()
    select.send_keys(password_mi_account)

    #We click the button to login into the account
    accept_button = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
    accept_button.click()

    #we decide the data we want

    if variablePersonalInformationSelenium == 1:
        select_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='USER']")))
        select_button.click()

    if variableActivitySelenium == 1:
        select_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='ACTIVITY']")))
        select_button.click()

    if variableSleepingSelenium == 1:
        select_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='SLEEP']")))
        select_button.click()

    if variableHeartRateSelenium == 1:
        select_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='HEARTRATE']")))
        select_button.click()

    if variableBodyFatSelenium == 1:
        select_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='BODY']")))
        select_button.click()

    if variableTrainingSelenium == 1:
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

    #We click the OK button
    select_button = wait.until(EC.element_to_be_clickable((By.ID, 'ok')))
    select_button.click()

    #We introduce our mail
    select = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
    select.clear()
    select.send_keys(mail_mi_account)

    #We save the code in a file
    code_mi_fit = open("config/code_mi_fit.txt","w")
    for elem in driver.find_elements_by_xpath('.//span'):
        code_mi_fit.write(elem.text)
    code_mi_fit.close()

    #We read the code from the file
    code_mi_fit = open("config/code_mi_fit.txt","r")
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

#########################################################################################################################
#########################################################################################################################

#we read the data from the files
#input text for mail
miFitMail = open("config/mi_fit_mail.txt", "r")
miFitMailText = miFitMail.read()
setInputMiFitMail(miFitMailText)
miFitMail.close()

#input text for mail
miFitPassword = open("config/mi_fit_password.txt", "r")
miFitPasswordText = miFitPassword.read()
setInputMiFitPassword(miFitPasswordText)
miFitPassword.close()

#input text for web driver
webDriverDirectory = open("config/web_driver_directory.txt", "r")
webDriverDirectoryText = webDriverDirectory.read()
setInputWebDriverDirectory(webDriverDirectoryText)
webDriverDirectory.close()

# we create the widgets with their variables
labelTitle = tkinter.Label(master, text = "Mi-Fit Data Downloader", font = ("Helvetica", 16, "bold"))
labelOptions = tkinter.Label(master, text = "Options:", font = ("Helvetica", 12, "bold"))

global variablePersonalInformation
variablePersonalInformation = IntVar()
labelPersonalInformation = tkinter.Checkbutton(master, text = "Personal Information", font = ("Helvetica", 12), variable = variablePersonalInformation)
labelPersonalInformation.select()

global variableActivity
variableActivity = IntVar()
labelActivity = tkinter.Checkbutton(master, text = "Activity", font = ("Helvetica", 12), variable = variableActivity)
labelActivity.select()

global variableSleeping
variableSleeping = IntVar()
labelSleeping = tkinter.Checkbutton(master, text = "Sleeping", font = ("Helvetica", 12), variable = variableSleeping)
labelSleeping.select()

global variableHeartRate
variableHeartRate = IntVar()
labelHeartRate = tkinter.Checkbutton(master, text = "Heart Rate", font = ("Helvetica", 12), variable = variableHeartRate)
labelHeartRate.select()

global variableBodyFat
variableBodyFat = IntVar()
labelBodyFat = tkinter.Checkbutton(master, text = "Body Fat", font = ("Helvetica", 12), variable = variableBodyFat)
labelBodyFat.select()

global variableTraining
variableTraining = IntVar()
labelTraining = tkinter.Checkbutton(master, text = "Training", font = ("Helvetica", 12), variable = variableTraining)
labelTraining.select()

labelMail = tkinter.Label(master, text = "Mail:", font = ("Helvetica", 12, "bold"))
inputMail = tkinter.Entry(master, font = ("Helvetica", 12), textvariable  = inputMiFitMailText)

labelPassword = tkinter.Label(master, text = "Password:", font = ("Helvetica", 12, "bold"))
inputPassword = tkinter.Entry(master, font = ("Helvetica", 12), textvariable  = inputMiFitPasswordText)

buttonStart = tkinter.Button(master, text = "Start", font = ("Helvetica", 12, "bold"), command = getInformation)

buttonConfiguration = tkinter.Button(master, text = "Settings", font = ("Helvetica", 12), command = openConfiguration)

labelCreator = tkinter.Label(master, text = "Marc Orfila Carreras", font = ("Helvetica", 8, "bold"), fg = "grey")

labelLink = tkinter.Label(master, text = "https://github.com/MarcOrfilaCarreras/Mi-Fit-Data-Downloader", font = ("Helvetica", 8, "bold"), fg = "grey")

# widget position
labelTitle.pack(pady = 20)
labelOptions.place(x = 88, y = 60)

labelPersonalInformation.place(x = 88, y = 90)
labelActivity.place(x = 88, y = 110)
labelSleeping.place(x = 88, y = 130)
labelHeartRate.place(x = 264, y = 90)
labelBodyFat.place(x = 264, y = 110)
labelTraining.place(x = 264, y = 130)

labelMail.place(x = 88, y = 170)
inputMail.place(x = 88, y = 205, height = 20, width = 310)

labelPassword.place(x = 88, y = 240)
inputPassword.place(x = 88, y = 275, height = 20, width = 310)

buttonStart.place(x = 190, y = 320, height = 30, width = 120)

labelLink.pack(side = tkinter.BOTTOM)
labelCreator.pack(side = tkinter.BOTTOM)

buttonConfiguration.place(x = 190, y = 390, height = 30, width = 120)

master.mainloop()
