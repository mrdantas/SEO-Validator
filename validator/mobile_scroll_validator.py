class MobileScrollValidator:
    def has_mobile_scroll(self, soup):
        mobile_styles = ['width: 320px', 'width: 360px', 'width: 375px', 'width: 414px', 'width: 768px']
        for tag in soup.findAll():
            if 'style' in tag.attrs and any(style in tag['style'] for style in mobile_styles):
                return True
        return False