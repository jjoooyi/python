def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang)) # 역슬래시하고 중간에 엔터하면 연결된다요

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업, 반복되는 값이 삽입될 경우 기본값을 지정하여 정의 가능
def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")


def profile(name, age, main_lang):
    print(name, age, main_lang)

# 선언된 순서대로 입력하지 않고 임의의 순서대로 정의해줘도 된다
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=35, name="김태호")

# 가변인자 *변수
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end = " " 문장의 끝에서 줄바꿈 하지 않고 지정한 모양대로 값이 삽입된 후 뒷 내용 출력
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "") # 이런식의 무의미한 값을 넣어줘야 하는게 비효율적!

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print() # 줄바꿈

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")