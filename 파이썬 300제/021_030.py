# 021
letters = 'python'
print(letters[0], letters[2])

# 022
license_plate = "24가 2210"
print(license_plate[-4:])

# 023 시작인덱스:끝인덱스:오프셋
string = "홀짝홀짝홀짝"
print(string[::2])

# 024
string = "PYTHON"
print(string[::-1])

# 025
phone_number = "010-1111-2222"
print(phone_number.replace('-', ' '))

# 026
print(phone_number.replace('-', ''))

# 027
url = "http://sharebook.kr"
print(url[-2:])
print(url.split('.')[1])
print(url.split('.')[-1])

# 028 문자열은 수정할 수 없음
# lang = 'python'
# lang[0] = 'P' # 에러 발생
# print(lang)

# 029
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

# 030
string = 'abcd'
string.replace('b', 'B')
print(string)  # abcd, 문자열은 수정되지 않음
