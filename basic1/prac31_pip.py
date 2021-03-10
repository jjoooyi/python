# pip list
# pip show beautifulsoup4 # 패키지명
# pip install --upgrade beautifulsoup4
# pip uninstall beautifulsoup4
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())