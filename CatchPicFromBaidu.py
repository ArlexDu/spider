from selenium import webdriver
import time
import urllib
import requests

# print(requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS)
url="http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E9%A9%AC%E5%85%8B%E6%9D%AF"

xpath='//li[contains(@class,"imgitem")]/div/a/img'

driver = webdriver.Chrome(executable_path=r"./webDriver/chromedriver.exe")

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
# driver.maximize_window()

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'Referer':'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E9%A9%AC%E5%85%8B%E6%9D%AF'}

img_url_array=[]

driver.get(url)

pos=0
m=0

for i in range(1):
    pos+=i*500
    js="document.documentElement.scrollTop=%d" % pos
    driver.execute_script(js)
    time.sleep(1)

    for element in driver.find_elements_by_xpath(xpath):
        img_url = element.get_attribute('src')
        if img_url != None and img_url not in img_url_array:
            img_url_array.append(img_url)
            m+=1
            type = img_url.split('.')[-1]
            print("download {}".format(img_url))
            filename=str(m)+'.'+type
            data=requests.get(img_url).text
            # print('data {0}'.format(data))
            # f=open('./baiduimages/'+filename,'wb')
            # f.write(data.encode())
            # f.close()
driver.close()
