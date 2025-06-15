import requests
from bs4 import BeautifulSoup
import os


# web_url = "https://pic.netbian.com/4kmeinv/"


def get_web_url(url):

    resp   = requests.get(url)
    resp.encoding = "gbk"

    html_doc = resp.text

    return html_doc

def parse_and_download(html_doc):
    soup = BeautifulSoup(html_doc, "html.parser")

    imgs = soup.find_all("img")

    for img in imgs:
        if "/uploads/" not in img["src"]:
            continue
        src = img["src"]
        url_img = f"https://pic.netbian.com{src}"
        print(url_img)


        file_name = os.path.basename(url_img)
        with open(f"D:/网页爬取图片/{file_name}", "wb") as f:
            photo_url = requests.get(url_img)
            f.write(photo_url.content)




urls = ["https://pic.netbian.com/4kmeinv/"]+[
    f"https://pic.netbian.com/4kmeinv/index_{i}.html"
    for i in range(2,11)

]
for url in urls:
    print("##正在爬取图片。。。。。。##")
    url = get_web_url(url)
    parse_and_download(url)