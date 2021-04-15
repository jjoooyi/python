# https://wikidocs.net/28

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


class Family:
    # 클래스 변수는 해당 클래스로 만든 모든 객체에 공유됨
    lastname = 'Park'


print(Family.lastname)
