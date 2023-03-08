import requests

class SSLValidator:
    def is_ssl_enabled(self, url):
        try:
            response = requests.get(url)
            return response.url.startswith('https')
        except:
            return False
