"""
Youtube Downloader
-----------------

Python GUI Application
"""

# Import Libraries
from tkinter import Button, Entry, Label, StringVar, Tk

# pip install pytube3      # install pytube
from pytube import YouTube

# ================ App ==================
ROOT = Tk()
ROOT.geometry("400x350")
ROOT.title("Youtube Downloader")

# =========== Global Area ==============
MYVAR = StringVar()
LINK = StringVar()


def download():
    try:
        MYVAR.set("Downloading....  ")
        ROOT.update()
        YouTube(LINK.get()).streams.first().download()
        print(LINK.get())
        LINK.set("Video Downloaded successfully...")
    except:
        MYVAR.set("Mistake")
        ROOT.update()
        LINK.set("Enter correct LINK!!")


Label(ROOT, text="Welcome to Youtube Downloader", font="Consolas 15 bold").pack()
MYVAR.set("Enter the LINK below")
Entry(ROOT, textvariable=MYVAR, width=40).pack(pady=10)
Entry(ROOT, textvariable=LINK, width=40).pack(pady=10)
Button(ROOT, text="Download Video", command=download).pack()

ROOT.mainloop()
# ============== End ============================
