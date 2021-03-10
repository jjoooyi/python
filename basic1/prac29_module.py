# 모듈 : 필요한 부분들이 부품처럼 잘 만들어진 파일
# 모듈은 내가 그 쓰려는 파일과 같은 경로에 있거나 파이썬 라이브러리가 모여있는 폴더에 들어있을 때 사용 가능
import prac29_theater_module
prac29_theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
prac29_theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
prac29_theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

import prac29_theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from prac29_theater_module import * # 해당 모듈에 있는 멤버들(필드/메소드)을 가져다 사용
price(3)
price_morning(4)
price_soldier(5)

from prac29_theater_module import price, price_morning
price(5)
price_morning(6)
# price_soldier(7)

from prac29_theater_module import price_soldier as price # price_soldier 함수 별명을 price로 지정하여 불러오기
price(5)