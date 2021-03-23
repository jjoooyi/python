# 자료구조
# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬 가능
num_list = [5, 4, 5, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장(하나의 리스트로 합치기)
num_list.extend(mix_list)
print(num_list)

# split() 이용하여 문자열 -> 리스트 str.split(sep, maxsplit) -> list
abc = 'With three words'
stuff = abc.split()
print(stuff)  # ['With', 'three', 'words']


# line에서 uct.ac.za만 추출하는 방법
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# words는 해당 라인을 빈칸을 구분자로 하여 리스트로 저장
words = line.split()
print(words[1])  # stephen.marquard@uct.ac.za 출력
email = words[1]
address = email.split('@')
print(address)  # ['stephen.marquard', 'uct.ac.za'] 출력
print(address[1])  # uct.ac.za 출력
