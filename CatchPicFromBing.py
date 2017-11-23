from selenium import webdriver
import time
import urllib
from selenium.common.exceptions import NoSuchElementException

url="https://cn.bing.com/images/search?q=%E9%A9%AC%E5%85%8B%E6%9D%AF&FORM=HDRSC2"

xpath_img='//div[contains(@class,"imgpt")]/a/div/img'

xpath_seemore ='//div[contains(@class,"seemore")]/a'

driver = webdriver.Chrome(executable_path=r"./webDriver/chromedriver.exe")

# driver.maximize_window()

img_url_array=[]

driver.get(url)

pos=0
m=0

for i in range(25):
    pos+=i*500
    js="document.documentElement.scrollTop=%d" % pos
    driver.execute_script(js)
    time.sleep(1)

    for element in driver.find_elements_by_xpath(xpath_img):
        img_url = element.get_attribute('src')
        if img_url != None and img_url not in img_url_array:
            img_url_array.append(img_url)
            m+=1
            print("download {}".format(img_url))
            filename=str(m)+'.jpg'
            data=urllib.request.urlopen(img_url).read()
            f=open('./bingimages/'+filename,'wb')
            f.write(data)
            f.close()
    try:
        driver.find_element_by_xpath(xpath_seemore).click()
    except:
        continue
driver.close()
