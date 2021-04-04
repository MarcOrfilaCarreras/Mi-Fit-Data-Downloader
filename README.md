
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

In this repository, the code is configured to work with **Google Chrome**. Although it can be **changed**.

It will be necessary to download the **drivers** for your web browser. To do this, you can follow the instructions in the Selenium **[installation manual](https://selenium-python.readthedocs.io/installation.html#drivers)**.

## ⚙️ Settings
In the main window, you can select the **data** you want to download. Also, it is necessary to enter the **email** and **password** in their corresponding fields.

![enter image description here](https://raw.githubusercontent.com/MarcOrfilaCarreras/Mi-Fit-Data-Downloader/main/_repository/Mi-Fit%20Data%20Downloader_Main.PNG)

You will have to follow these steps every time you want to download the data. Unless, you configure it by default in **Settings**, where you will also have to configure the path of the **Web Driver**.

![enter image description here](https://raw.githubusercontent.com/MarcOrfilaCarreras/Mi-Fit-Data-Downloader/main/_repository/Mi-Fit%20Data%20Downloader_Settings.PNG)

This will **save** the data forever. Example:

![enter image description here](https://raw.githubusercontent.com/MarcOrfilaCarreras/Mi-Fit-Data-Downloader/main/_repository/Mi-Fit%20Data%20Downloader_Example.gif)