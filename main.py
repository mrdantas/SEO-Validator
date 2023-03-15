from validator.ssl_validator import SSLValidator
from validator.asc_validator import ASCValidator
from validator.seo_validator import SEOValidator
from validator.url_validator import URLValidator
from validator.img_validator import ImgValidator
from validator.h1_validator import H1Validator
from validator.h2_validator import H2Validator
from validator.mobile_scroll_validator import MobileScrollValidator
from validator.pagespeed_validator import PagespeedValidator
from bs4 import BeautifulSoup
import requests

url = 'https://www.producao.mpitemporario.com.br/qaddw.com.br/xpto'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print("================ URL Validator ================")  
url_validator = URLValidator()
has_valid_url = url_validator.has_valid_url(url)


# ssl_validator = SSLValidator()
# ssl_enabled = ssl_validator.is_ssl_enabled(url)
# print(f"SSL ativado: {ssl_enabled}")


# asc_validator = ASCValidator()
# has_asc = asc_validator.has_asc_chars('Text with special character é')
# print(f"Página com caracteres ASC: {has_asc}")

 
# print("================ SEO (Alt/Title) Validator ================")  
# seo_validator = SEOValidator()
# alt_title = seo_validator.alt_title(soup)


# print("================ Img Validator ================")
# img_validator = ImgValidator()
# has_img = img_validator.has_img(soup)
 
# print("================ H1 Validator ================")
# h1_validator = H1Validator()
# has_h1 = h1_validator.has_h1(soup)

# print("================ H2 Validator ================")
# h2_validator = H2Validator()
# has_h2 = h2_validator.has_h2(soup)

# print("================ Pagespeed Validator ================")
# value_ps = PagespeedValidator()
# get_pagespeed = value_ps.get_pagespeed(url)

# mobile_scroll_validator = MobileScrollValidator()
# has_mobile_scroll = mobile_scroll_validator.has_mobile_scroll(soup)
# print(f"Scroll lateral no mobile: {has_mobile_scroll}")
