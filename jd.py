#!/usr/bin/python3
#coding:utf-8
from selenium import webdriver
#下面填入京东的用户名以及密码
jd_up={"ue":"****","pd":"****"}

chrome=webdriver.Chrome()
chrome.get(url="https://passport.jd.com/new/login.aspx?")
chrome.find_element_by_xpath("//*[@id=\"content\"]/div/div[1]/div/div[2]/a").click()
User=chrome.find_element_by_id("loginname")
User.clear()
User.send_keys(jd_up["ue"])
Passwd=chrome.find_element_by_id("nloginpwd")
Passwd.clear()
Passwd.send_keys(jd_up["pd"])
chrome.find_element_by_id("loginsubmit").click()
while True:
    try:
        chrome.get(url="https://item.jd.com/4099139.html")
        chrome.find_element_by_id("choose-btn-ko").click()
        chrome.find_element_by_id("order-submit").click()
        print("抢购成功并且已下单！！")
        chrome.quit()
    except Exception:
        print("还未开始抢购！！")