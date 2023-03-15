class H1Validator:
    def has_h1(self, soup):
        h1 = soup.find_all('h1')
        if len(h1) == 0:
            print('No <h1> on page.')
        elif len(h1) >= 2:
            print('More than 1 <h1> on page.')
        else:
            print(f'Contains {len(h1)} h1.')