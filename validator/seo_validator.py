class SEOValidator:
    def alt_title(self, soup):
        empty_a = soup.find_all(['a'], {'alt': '', 'title': ''})
        for link in empty_a:
            print(f'Link without Alt/Title: {link}')

        empty_img = soup.find_all(['img'], {'alt': '', 'title': ''})
        for img in empty_img:
            print(f'Image without Alt/Title {img}')
          