import requests
img_url_array=[]

filename = './imageNetCup.txt'
pos = []
Efield = []
with open(filename, encoding='utf-8') as file_to_read:
  while True:
    img_url = file_to_read.readline().strip() # 获取每一行的图片地址
    if img_url != None and img_url not in img_url_array:
        img_url_array.append(img_url)
        print("download {}".format(img_url))
        filename = img_url.split('/')[-1]
        data = requests.get(img_url).content
        f = open('./netimages/' + filename, 'wb')
        f.write(data)
        f.close()
    if not img_url:
      break
