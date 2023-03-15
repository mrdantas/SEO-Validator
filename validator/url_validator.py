import urllib.request

class URLValidator:
    def has_valid_url(self, url):
        try:
            response = urllib.request.urlopen(url)
            final_url = response.geturl()
            code_status = response.getcode()
            if final_url.endswith('/404'):
                print(f'Error: URL redirect to 404 error page: {url}')
            return code_status == 200
        except urllib.error.HTTPError as e:
            print(f'HTTP Error: {e.code}')
            return False
        # except:
        #     print(f'Invalid URL: {url}')
        #     return False