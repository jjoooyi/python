from tkinter import *

root = Tk()
root.title("Jooyi GUI")
root.geometry("640x480") # 가로 * 세로

# 여러줄에 걸쳐 목록 관리하는 위젯
listbox = Listbox(root, selectmode="extended", height=0) # selectmode- extended/single, height - 리스트에서 몇개 까지 화면에 보이게 할것인지 0이면 전체
listbox.insert(0, 'apple')
listbox.insert(1, 'banana')
listbox.insert(2, 'cherry')
listbox.insert(END, 'durian') # END - 리스트의 마지막 위치에 값 추가
listbox.insert(END, 'grape')
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(END) # 맨 뒤 항목 삭제
    # listbox.delete(0) # 맨 앞 항목 삭제
    
    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")
    
    # 항목 확인 (시작 idx, 끝 idx)
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))
    
    # 선택된 항목 확인 curselection() : 선택된 항목의 인덱스 값 반환
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()