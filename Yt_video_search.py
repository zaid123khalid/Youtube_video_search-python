from tkinter import *
from youtubesearchpython import VideosSearch
import tkhtmlview


def search():
    term = ent.get()
    vs = VideosSearch(term, limit=5)
    
    id = vs.result()["result"][0]["id"]
    title = vs.result()["result"][0]["title"]
    link = f"<a href=https://www.youtube.com/watch?v={id}> {title}</a>"

    id1 = vs.result()["result"][1]["id"]
    title1 = vs.result()["result"][1]["title"]
    link1 = f"<a href=https://www.youtube.com/watch?v={id1}> {title1}</a>"

    id2 = vs.result()["result"][2]["id"]
    title2 = vs.result()["result"][2]["title"]
    link2 = f"<a href=https://www.youtube.com/watch?v={id2}> {title2}</a>"

    id3 = vs.result()["result"][3]["id"]
    title3 = vs.result()["result"][3]["title"]
    link3 = f"<a href=https://www.youtube.com/watch?v={id3}> {title3}</a>"

    id4 = vs.result()["result"][4]["id"]
    title4 = vs.result()["result"][4]["title"]
    link4 = f"<a href=https://www.youtube.com/watch?v={id4}> {title4}</a>"

    video = tkhtmlview.HTMLLabel(win, html=link)
    video.grid(row=1, columnspan=2)
    video.fit_height()

    video1 = tkhtmlview.HTMLLabel(win, html=link1)
    video1.grid(row=2, columnspan=2)
    video1.fit_height()

    video2 = tkhtmlview.HTMLLabel(win, html=link2)
    video2.grid(row=3, columnspan=2)
    video2.fit_height()

    video3 = tkhtmlview.HTMLLabel(win, html=link3)
    video3.grid(row=4, columnspan=2)
    video3.fit_height()

    video4 = tkhtmlview.HTMLLabel(win, html=link4)
    video4.grid(row=5, columnspan=2)
    video4.fit_height()


win = Tk()
win.title("Youtube Video Search")
photo = PhotoImage(file="Youtube image.png")
win.iconphoto(False, photo)

lbl = Label(win, text="Seach Term:")
lbl.grid(row=0, column=0)

ent = Entry(win, width=50)
ent.grid(row=0, column=1)

btn = Button(win, text="Search", command=search)
btn.grid(row=0, column=2)

win.mainloop()
