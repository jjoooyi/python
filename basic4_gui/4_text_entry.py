from tkinter import *

root = Tk()
root.title("Jooyi GUI")
root.geometry("640x480") # 가로 * 세로

txt = Text(root, width=30, height=5) # 여러 줄 입력
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) # 한 줄 입력
e.pack()
e.insert(0, "한 줄만 입력해요") # 현재는 값이 비어있기 때문에 0 대신 END로 입력해도 같은 결과

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 처음부터 끝까지 1-첫번째 라인 0-0번째 컬럼 위치
    print(e.get())
    
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()