class ASCValidator:
    def has_asc_chars(self, text):
        return any(ord(c) > 127 for c in text)