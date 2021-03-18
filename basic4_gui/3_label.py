from tkinter import *

root = Tk()
root.title("Jooyi GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="basic4_gui/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또만나요")
    
    global photo2 # GC가 빈 메모리를 바로 제거하지 못하게 하기 위해서..? 전역변수로 만들지 않으면 쓰레기로 인식하고 photo2를 지울 수 있음
    # => 함수가 끝나도 photo2를 제거하지 않고 존재하게 하기 위해 전역변수로 지정!
    photo2 = PhotoImage(file="basic4_gui/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()