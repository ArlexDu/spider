from selenium import webdriver
import time
import requests

# print(requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS)
url="http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E9%A9%AC%E5%85%8B%E6%9D%AF"

xpath='//li[contains(@class,"imgitem")]/div/a/img'

driver = webdriver.Chrome(executable_path=r"./webDriver/chromedriver")

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
# driver.maximize_window()

header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

img_url_array=[]

driver.get(url)

pos=0
m=0

for i in range(10):
    pos+=i*500
    js="document.documentElement.scrollTop=%d" % pos
    driver.execute_script(js)
    time.sleep(1)

    for element in driver.find_elements_by_xpath(xpath):
        img_url = element.get_attribute('data-imgurl')
        if img_url != None and img_url not in img_url_array:
            img_url_array.append(img_url)
            m+=1
            type = img_url.split('.')[-1]
            print("download {}".format(img_url))
            filename=str(m)+'.'+type
            data=requests.get(img_url,headers=header).content
            f=open('./baiduimages/'+filename,'wb')
            f.write(data)
            f.close()
driver.close()
