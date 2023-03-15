from requests_html import HTMLSession
import json

class PagespeedValidator():
    def get_pagespeed(self, url):
        apiKey = 'AIzaSyC7CeAKw5Z-JZzkP9tY3kP6YsBQgPWk-ZA'
        pagespeedUrl = url.replace(':', '%3A')
        pagespeedUrl = url.replace('/', '%2F')
        mobileUrl = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={pagespeedUrl}&category=performance&locale=pt_BR&strategy=mobile&key={apiKey}'
        desktopUrl = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={pagespeedUrl}&category=performance&locale=pt_BR&strategy=mobile&key={apiKey}'

        session = HTMLSession()

        mobileRequest = session.get(mobileUrl)
        jsonData = json.loads(mobileRequest.text)
        mobileScore = int(float(jsonData['lighthouseResult']['categories']['performance']['score']) * 100)
        print(f'Mobile score - {mobileScore}')

        desktopRequest = session.get(desktopUrl)
        jsonData = json.loads(desktopRequest.text)
        desktopScore = int(float(jsonData['lighthouseResult']['categories']['performance']['score']) * 100)
        print(f'Desktop score - {desktopScore}')