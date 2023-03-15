import requests
class ImgValidator:
    def has_img(self, soup):
        for img in soup.find_all('img'):
            if 'src' not in img.attrs:
                print(f'Tag <img> without "src" atribute: {img}')
            elif img['src'].startswith('https://'):
                response = requests.get(img['src'])
                if response.status_code == 404:
                    print(f'Image {img["src"]} not found')
            else:
                print(f'Tag <img> with invalid link: {img}')