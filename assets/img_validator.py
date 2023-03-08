import requests
from bs4 import BeautifulSoup

class ImgValidator:
    def has_img(self, soup):
        for img in soup.find_all('img'):
            if 'src' not in img.attrs:
                return False
            response = requests.get(img['src'], stream=True)
            if response.status_code != 200:
                return False
        return True
