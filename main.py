from validator.ssl_validator import SSLValidator
from validator.asc_validator import ASCValidator
from validator.seo_validator import SEOValidator
from validator.link_validator import linkValidator
from validator.img_validator import ImgValidator
from validator.h1_validator import H1Validator
from validator.mobile_scroll_validator import MobileScrollValidator
from bs4 import BeautifulSoup
import requests

url = 'https://www.producao.mpitemporario.com.br/qaddw.com.br/calibracao'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# ssl_validator = SSLValidator()
# ssl_enabled = ssl_validator.is_ssl_enabled(url)
# print(f"SSL ativado: {ssl_enabled}")


# asc_validator = ASCValidator()
# has_asc = asc_validator.has_asc_chars('Text with special character é')
# print(f"Página com caracteres ASC: {has_asc}")

seo_validator = SEOValidator()
alt_title = seo_validator.alt_title(soup)
# print(f"Título da página encontrado: {alt_title}")

# link_validator = linkValidator()
# has_valid_links = link_validator.has_valid_links(soup)
# print(f"Links válidos: {has_valid_links}")

# img_validator = ImgValidator()
# has_img = img_validator.has_img(soup)
# print(f"Imagens encontradas: {has_img}")

# h1_validator = H1Validator()
# has_h1 = h1_validator.has_h1(soup)
# print(f"Tags H1 encontradas: {has_h1}")

# mobile_scroll_validator = MobileScrollValidator()
# has_mobile_scroll = mobile_scroll_validator.has_mobile_scroll(soup)
# print(f"Scroll lateral no mobile: {has_mobile_scroll}")
