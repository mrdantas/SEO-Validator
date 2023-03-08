class H1Validator:
    def has_h1(self, soup):
        return soup.h1 is not None
