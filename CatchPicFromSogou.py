from selenium import webdriver
import time
import urllib

url="http://pic.sogou.com/pics?query=%C2%ED%BF%CB%B1%AD&w=05009900&p=40030500&_asf=pic.sogou.com&_ast=1511437004&sc=index&sut=2332&sst0=1511437003957"

xpath='//div[@id="imgid"]/ul/li/a/img'

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

    for element in driver.find_elements_by_xpath(xpath):
        img_url = element.get_attribute('src')
        if img_url != None and img_url not in img_url_array:
            img_url_array.append(img_url)
            m+=1
            print("download {}".format(img_url))
            filename=str(m)+'.jpg'
            data=urllib.request.urlopen(img_url).read()
            f=open('./sougouimages/'+filename,'wb')
            f.write(data)
            f.close()
driver.close()
