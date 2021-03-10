# pickle: 가지고 있는 데이터를 pickle을 이용하여 파일로 저장하고 
# 그 파일에 있는 내용을 load 하여 변수에 저장하여 사용할 수있도록 해주는 라이브러리

import pickle # 모듈 임포트
profile_file = open("profile.pickle", "wb") # wb : write 바이너리타입..?
profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file(profile_file)에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb") # rb : read, binary
profile = pickle.load(profile_file) # file(profile_file) 에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()