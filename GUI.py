from tkinter import *
import os
import clean
import download

root = Tk()
root.resizable(width=False, height=False)

def whatRange():
    def getRange():
        text = str(tx.get())
        text = text.split()
        try:
            start = int(text[0])
            end = int(text[1])
            if start >= end:
                raise Exception
        except:
            bt = Button(root, width=10, heigh=10, bg='red')
            bt.pack()
            bt.mainloop()
            print("Wrong input")
        else:
            files = [str(i) + '.txt' for i in range(start, end)]
            clean.start_working(files=files)
            frame.destroy()

    frame = Frame(root, bg='gray')
    tx = Entry(frame)
    but = Button(frame, text="Submit", command=getRange)
    tx.grid()
    but.grid()
    frame.pack()
    frame.mainloop()


def update():
    clean.lost_packages()


def CleanAll():
    files = os.listdir('/home/max/PycharmProjects/FULL_DATA' + '/HTML_DATA/')
    clean.start_working(files=files)


def cleanGUI():
    frameo.destroy()
    frame = Frame(root, width=100, heigh=100, bg='gray')
    bt1 = Button(frame, text='Range', command=whatRange)
    bt2 = Button(frame, text='Сlean all', command=CleanAll)
    bt3 = Button(frame, text='Update', command=update)
    bt4 = Button(frame, text="Close", command=root.destroy)
    bt1.grid()
    bt2.grid()
    bt3.grid()
    bt4.grid()
    frame.pack()
    frame.mainloop()


def downloadGUI():
    frameo.destroy()
    frame = Frame(root, width=100, heigh=100, bg='gray')
    bt1 = Button(frame, text='Range', command=whatRangeD)
    bt2 = Button(frame, text='Update', command=download.lost_packages)
    bt3 = Button(frame, text="Close", command=root.destroy)
    bt1.grid()
    bt2.grid()
    bt3.grid()
    frame.pack()
    frame.mainloop()


def whatRangeD():
    frame = Frame(root, bg='gray')
    thr = 40

    def getThreads(event):
        return int(scale.get())

    scale = Scale(frame, orient=HORIZONTAL,
                  length=100, from_=1, to=60, resolution=1)
    btn = Button(frame, text='Submit number of Threads')
    scale.grid()
    btn.grid()
    btn.bind("<Button-1>", getThreads)

    def getRange():
        text = str(tx.get())
        text = text.split()
        try:
            start = int(text[0])
            end = int(text[1])
            if start >= end:
                raise EXCEPTION
        except:
            bt = Button(root, width=10, heigh=10, bg='red')
            bt.pack()
            bt.mainloop()
            print("Wrong input")
        else:
            files = [str(i) for i in range(start, end)]
            download.start_working(files=files,
                                   threads=thr)
            root.destroy()

    tx = Entry(frame)
    but = Button(frame, text="Submit", command=getRange)
    tx.grid()
    but.grid()
    frame.pack()
    frame.mainloop()


frameo = Frame(root, width=100, heigh=100, bg='gray')


def main():
    bt1 = Button(frameo, text="Clear", command=cleanGUI)
    bt2 = Button(frameo, text="Download", command=downloadGUI)
    bt3 = Button(frameo, text='Close', command=root.destroy)
    bt1.grid()
    bt2.grid()
    bt3.grid()
    frameo.pack()
    frameo.mainloop()

main()