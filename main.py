from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from gtts import gTTS
from pathlib import Path
import os

root = Tk()
"""
def BROWSE():
    path = '{}'.format(askdirectory(title='Choose Directory', initialdir=r'/home/Downloads', mustexist=True))
    path1.set(path)

"""
def play():
    convert = gTTS(text=entry.get(), lang='en')
    tit = entry1.get()
   # path2 = path1.get()
   # path3 = "/home"
    convert.save(tit + ".wav")
    messagebox.showinfo("SUCCESSFULLY", "saved")


'''
    except:
        
        messagebox.showinfo("alert", "pls cheak filename, browse, message "
                                     "or someother")

'''


def cls():
    entry.delete(0, 'end')
    entry1.delete(0, 'end')
    #entry3.delete(0, 'end')


# title
ibl = Label(text="Text to Audio Convert", font=("Arial Black", 12))
ibl.place(x=160, y=10)
# file-name
ibl2 = Label(text="File Name:", font=("Arial", 12))
ibl2.place(x=5, y=50)
# file-entry
entry1 = Entry(width=15,
               bd=2,
               font=("Arial", 14))
entry1.place(x=110, y=50)
path1 = StringVar()
"""
# browser-entry
entry3 = Entry(textvariable=path1, width=30,
               bd=2,
               font=("Arial", 14))
entry3.place(x=5, y=80)
# browser-btn
btn = Button(text="Browser",
             width="10",
             font="10",
             command=BROWSE)
btn.place(x=350, y=80)
"""
# message
ibl1 = Label(text='Message:', font=("Arial", 12))
ibl1.place(x=5, y=120)
# message-entry
entry = Entry(width=44,
              bd=2,
              font=("Arial", 14))
entry.place(x=5, y=150)
# covert-btn
btn = Button(text="CONVERT",
             width="15",
             pady=10,
             font="bold,15",
             command=play,
             bg="pink")
btn.place(x=160, y=180)
# clear
btn = Button(text="Clear",
             width="10",
             height="1",
             font="10",
             command=cls,
             bg="pink")
btn.place(x=370, y=180)
'''
ibl1 = Label(text='Browser', font=("Arial Black", 12))
ibl1.place(x=20, y=210)
'''

root.title("Text to Audio Convert")
root.geometry("500x250+400+150")
root.resizable(0, 0)
root.mainloop()
