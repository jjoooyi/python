# pip install beautifulsoup4
# pip install lxml
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")  # lxml파서 이용

print(soup.title)
print(soup.title.get_text())
print(soup.a)  # soup 객체에서 처음 발견되는 a element 출력
print(soup.a.attr)  # a element 의 속성 정보 출력
print(soup.a["href"])  # a element 의 href 속성 '값' 정보를 출력

# class="Nbtn_upload" 인 a element 를 찾아줘
print(soup.find("a", attrs={"class": "Nbtn_upload"}))
# class="Nbtn_upload" 인 어떤 element 를 찾아줘
print(soup.find(attrs={"class": "Nbtn_upload"}))

print(soup.find("li", attrs={"class": "rank01"}))
rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a.get_text())

# 형제 태그 정보 가져오기
print(rank1.next_sibling.next_sibling)
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
rank2 = rank3.previous_sibling.previous_sibling
rank2 = rank1.find_next_sibling("li")
rank3 = rank2.find_next_sibling("li")
rank2 = rank3.find_previous_sibling("li")

rank1.find_next_siblings("li")  # 형제들 한번에 받아오기

# 부모 태그 정보 가져오기
parent = rank1.parent

webtoon = soup.find("a", text="독립일기-74화 이건 되는 꿈이다")
print(webtoon)
