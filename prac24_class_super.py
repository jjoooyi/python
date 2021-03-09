class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() # 다중 상속의 경우, super() 를 사용하면 먼저 작성한 생성자만 초기화됨 -> 각각 초기화 해줘야함
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()