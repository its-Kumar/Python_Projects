# Import Libraries
from tkinter import *
from pytube import YouTube

# misc
import os
import shutil
import math
import datetime


# ================ App ==================
root = Tk()
root.title("Youtube Downloader")

# =========== Global Area ==============
url = StringVar()
video = None


def download(text):
    global url
    url = text
    print(url)
    global video
    video = YouTube(str(url))
    print(video.streams.all())


label = Label(root, text='Online Video Downloader')
label.pack()

entry = Entry(root, textvariable=url, text='Paste your video link here... ')
entry.pack(side=LEFT)
btnDownload = Button(root, text="Download",
                     command=lambda: download(entry.get()))


# video.streams.all()

#video.streams.filter(file_extension = "mp4").all()

# video.streams.get_by_itag(18).download()

btnDownload.pack()
root.mainloop()
# ============== End ============================
