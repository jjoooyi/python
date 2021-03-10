# 파일 입력
score_file = open("score.txt", "w", encoding="utf8") # "w" : 파일 쓰기 용도
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # "a" : append
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # 줄바꿈이 자동으로 일어나지 않기 때문에 이스케이프 문자를 활용
score_file.close()