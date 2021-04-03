# Mi-Fit Data Downloader

This program is still in **BETA**, which means that it **does not** include all the functionalities yet.


## 📖 Introduction

**Mi-Fit Data Downloader**, is a program designed to automate the download of data from the Mi-Fit account. It works using **web-scraping**, since there is no API available.

## 🏁 Getting Started

To start using the program, it is necessary to meet the following requirements:
- You need to have **Python** installed (Tested with **version 3.9**)
- You need to have **Selenium** installed
- You need to have **Tkinter** installed
- You need to have **Datetime** installed
- You need to have a **Mi-Fit Account**
- You need to have a **Mail Account**

Explain that in this repository, the code is configured to work with **Google Chrome**. Although it can be **changed**.

In addition, it will be necessary to download the **drivers** for your web browser. To do this, you can follow the instructions in the Selenium **[installation manual](https://selenium-python.readthedocs.io/installation.html#drivers)**.

This should be placed in the **following directory**:

> C:/Users/*you-user*/*your-driver*.exe

Or if you prefer, it **can be changed** to another directory by editing the following line of code:

**Line 58**⠀ `driver  =  webdriver.Chrome("C:/Users/you-user/your-driver.exe")`

## ⚙️ Settings
You can choose what data you want to be downloaded.

![](https://raw.githubusercontent.com/MarcOrfilaCarreras/Mi-Fit-Data-Downloader/main/images/Mi-Fit%20Data%20Downloader_Options.PNG)

In order for the program to be able to log into the Mi-Fit account, it is necessary to enter the email and password in their corresponding fields.

![enter image description here](https://raw.githubusercontent.com/MarcOrfilaCarreras/Mi-Fit-Data-Downloader/main/images/Mi-Fit%20Data%20Downloader_Account.PNG)

This will allow the program to log in automatically.