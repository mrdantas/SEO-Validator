class H2Validator():    
    def has_h2(self, soup):
        h2_tags = soup.find_all('h2')
        h2_set = set()
        duplicates_count = 0
        for h2_tag in h2_tags:
            text = h2_tag.text.strip()
            if text in h2_set:
                duplicates_count += 1
                print(f"Duplicated content in <h2> on page: {h2_tag}")
            else:
                h2_set.add(text)
        if duplicates_count == 0:
            print("OK")
