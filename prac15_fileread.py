# 파일 내용 출력

# 한번에 불러오기
score_file = open("score.txt", "r", encoding="utf8") # "r" : read
print(score_file.read())
score_file.close()

# 한 줄씩 불러오기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# 몇 줄이 들어있는지 모를 때 1
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # 읽어온 내용이 없을 경우
        break
    print(line, end="") # 자동 줄바꿈이 싫을 경우 end 이용
score_file.close()

# 몇 줄이 들어있는지 모를 때 2
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 line을 가지고 와서 list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()