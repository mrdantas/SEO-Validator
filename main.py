from assets.ssl_validator import SSLValidator
from assets.asc_validator import ASCValidator
from assets.title_validator import TitleValidator
from assets.a_validator import AValidator
from assets.img_validator import ImgValidator
from assets.h1_validator import H1Validator
from assets.mobile_scroll_validator import MobileScrollValidator
from bs4 import BeautifulSoup
import requests

url = 'https://www.producao.mpitemporario.com.br/qaddw.com.br/'

ssl_validator = SSLValidator()
ssl_enabled = ssl_validator.is_ssl_enabled(url)
print(f"SSL ativado: {ssl_enabled}")

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

asc_validator = ASCValidator()
has_asc = asc_validator.has_asc_chars('Text with special character é')
print(f"Página com caracteres ASC: {has_asc}")

title_validator = TitleValidator()
has_title = title_validator.has_title(soup)
print(f"Título da página encontrado: {has_title}")

a_validator = AValidator()
has_valid_links = a_validator.has_valid_links(soup)
print(f"Links válidos: {has_valid_links}")

img_validator = ImgValidator()
has_img = img_validator.has_img(soup)
print(f"Imagens encontradas: {has_img}")

h1_validator = H1Validator()
has_h1 = h1_validator.has_h1(soup)
print(f"Tags H1 encontradas: {has_h1}")

mobile_scroll_validator = MobileScrollValidator()
has_mobile_scroll = mobile_scroll_validator.has_mobile_scroll(soup)
print(f"Scroll lateral no mobile: {has_mobile_scroll}")
