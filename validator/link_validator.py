import requests
from bs4 import BeautifulSoup

class linkValidator:
    def has_valid_links(self, soup):
        valid = True
        for link in soup.find_all('a'):
            if 'rel' in link.attrs and 'nofollow' in link['rel'] and 'href' in link.attrs:
                status = requests.head(link['href']).status_code
                if status != 200:
                    valid = False
                    break
            else:
                valid = False
                break
        return valid
