# pip install requests
import requests
res = requests.get("https://naver.com")
# res = requests.get("https://nadocoding.tistory.com") # 403 error
# print("응답코드 :", res.status_code) # 200 이면 정상
res.raise_for_status()  # 정상이면 진행, 문제 발생 시 에러 발생 후 동작 중지

# if res.status_code == request.codes.ok: # 200
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("basic5_webscraping/mynaver.html", "w", encoding="utf8") as f:
    f.write(res.text)
