import tkinter as tk

class Bua:
    def buga(self):
        newaq = tk.Label(chuangko,text="你好世界",font=("宋体",36),bg="#00FFFF")
        newaq.pack()

ssic=Bua()
chuangko = tk.Tk()
chuangko.title("GUI的“你好世界”")
chuangko.geometry('500x400')
chuangko.resizable(width=False,height=False)
chuangko.configure(bg='#00FFFF')
ssic.buga()

chuangko.mainloop()