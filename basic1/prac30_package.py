import travel.thailand # 모듈이나 패키지만 바로 임포트 가능
# import travel.thailand.ThailandPackage # 모듈이나 패키지 외의 클래스를 바로 임포트 불가능, from 으로 하면 가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# from random import *
from travel import * # __init__.py 에서 __all__ 에다 불러오는것을 허용할 모듈?을 지정해줘야 *로 불러올 수 있다!
trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to = thailand.ThailandPackage()
trip_to.detail()

# 호출한 패키지/모듈의 위치 출력 -> inspect
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))