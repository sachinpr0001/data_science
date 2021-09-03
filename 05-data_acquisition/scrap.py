import bs4
import requests
import os

str = input()
input_str = str
str = str.replace(" ", "&20")
url = "https://www.snapdeal.com/search?keyword={}&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy".format(str)
response = requests.get(url)
soup = bs4.BeautifulSoup(response.content)
picture_element = soup.findAll('picture')
count = 0
try: 
    os.mkdir(input_str)
    for i, picture in enumerate(picture_element):
        count = i
        with open('{}/{}-{}.jpg'.format(input_str, input_str, i), 'wb') as file:
            try:
                img_url = picture.img.attrs['src']
                response = requests.get(img_url)
                file.write(response.content)
            except KeyError:
                img_url = picture.img.attrs['data-src']
                response = requests.get(img_url)
                file.write(response.content)
except FileExistsError:
    print("The search keyword is same to a previously searched keyword. Therefore, deleting old files.")
    for f in os.listdir(input_str):
        os.remove(os.path.join(input_str, f))
        
    for i, picture in enumerate(picture_element):
        count = i
        with open('{}/{}-{}.jpg'.format(input_str, input_str, i), 'wb') as file:
            try:
                img_url = picture.img.attrs['src']
                response = requests.get(img_url)
                file.write(response.content)
            except KeyError:
                img_url = picture.img.attrs['data-src']
                response = requests.get(img_url)
                file.write(response.content)

print(count, "new files are saved in the newly created folder")