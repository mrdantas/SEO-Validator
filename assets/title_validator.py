class TitleValidator:
    def has_title(self, soup):
        return soup.title is not None