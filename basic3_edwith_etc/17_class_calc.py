# https://wikidocs.net/28
# self : 호출한 객체 자신
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


# class 클래스 이름(상속할 클래스 이름)
class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = FourCal(5, 6)
b = FourCal(7, 8)
c = MoreFourCal(9, 10)
d = SafeFourCal(4, 0)

a.setdata(4, 2)
b.setdata(3, 7)

print(a.first, id(a.first))  # a의 first 주소값 확인
print(c.pow())
print(d.div())
