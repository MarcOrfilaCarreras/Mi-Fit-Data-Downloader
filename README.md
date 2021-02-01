# Mi-Fit Data Downloader

This program is still in **BETA**, which means that it **does not** include all the functionalities yet.


## 📖 Introduction

**Mi-Fit Data Downloader**, is a program designed to automate the download of data from the Mi-Fit account. It works using **web-scraping**, since there is no API available.

## 🏁 Getting Started

To start using the program, it is necessary to meet the following requirements:
- You need to have Python installed (Tested with **version 3.9**)
- You need to have Selenium installed
- You need to have Datetime installed
- You need to have a Mi-Fit Account
- You need to have a Gmail Account

Explain that in this repository, the code is configured to work with **Google Chrome**. Although it can be **changed**.

In addition, it will be necessary to download the necessary **drivers** for your web browser. To do this, you can follow the instructions in the Selenium **[installation manual](https://selenium-python.readthedocs.io/installation.html#drivers)**.

This should be placed in the **following directory**:

> C:/Users/*you-user*/*your-driver*.exe

Or if you prefer, it **can be changed** to another directory by editing the following line of code:

    driver  =  webdriver.Chrome("C:/Users/you-user/your-driver.exe")

## ⚙️ Settings
In order for the program to be able to log into the Mi-Fit account, it is necessary to enter the email and password in their corresponding files.
- The mail in the file **mail_mi_fit.txt**
- The password in the file **password_mi_fit.txt**

This will allow the program to log in automatically.
