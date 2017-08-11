#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from config import *
def start(intv):
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    #submit_url = 'http://t1.ronganjx.com/Web11/logging/BookingCNStudy.aspx?coachName=9115050490&date=2017-08-23&beginTime=2100&trainType=%u573a%u5185&timeLine=22'
    browser.get(SUBMIT_URL)
    print(browser.get_cookies())
    browser.delete_all_cookies()
    browser.add_cookie(COOKIE1)
    browser.add_cookie(COOKIE2)
    browser.add_cookie(COOKIE3)
    browser.get(SUBMIT_URL)
    print(browser.get_cookies())

    c = 1
    while True:
        print c
        sel = browser.find_element_by_xpath("//select[@id='ctl00_ContentPlaceHolder2_ddlLine']")
        Select(sel).select_by_value(u'杨浦')

        sel = browser.find_element_by_xpath("//select[@id='ctl00_ContentPlaceHolder2_ddlStationAndTime']")
        Select(sel).select_by_value(u'五角场  20:00')
        #browser.find_element_by_id("ctl00_ContentPlaceHolder2_btnSubmit").click()
        browser.get(SUBMIT_URL)

        c = c+1