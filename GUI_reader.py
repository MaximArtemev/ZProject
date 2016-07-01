#!/usr/bin/env python

from tkinter import *
import marking

MARK = '/home/max/PycharmProjects/FULL_DATA/MARKS_DATA/'
CLEAN = '/home/max/PycharmProjects/FULL_DATA/CLEAN_DATA/'

root = Tk()
root.resizable(width=FALSE, height=FALSE)
t = Text(root, font=("Helvetica", "14", 'normal'), width=70, height=40, wrap=WORD, )
frameAns = Frame(root, )
frameAdditional = Frame(root, )

current = 0
a = marking.check()
sor_every = marking.make_an(a[0], a[1], a[2])


def packText(filename):
    with open(CLEAN + str(filename) + '.txt', 'r') as file:
        title = file.readline()
        span = file.read()
    global t
    t = Text(root, font=("times", "14", 'normal'), width=70, height=40, wrap=WORD)
    t.insert('1.0', title)
    t.tag_add('title', '1.0', '1.end')
    t.tag_config('title',
                 font=('times', 14, 'bold'), justify=CENTER)
    t.insert('2.0', span)
    t.tag_add('span', '2.0', 'end')
    t.tag_config('span',
                 font=('sans', 11,), justify=LEFT)
    t.config(state=DISABLED)
    t.grid(row=0, column=0, padx=5, pady=5)


def packAns():
    bYes = Button(frameAns, text='Yes', command=yes, height=10, width=10)
    bYes.grid(row=1, column=1)
    bNo = Button(frameAns, text='No', command=no, height=10, width=10)
    bNo.grid(row=1, column=0)
    frameAns.grid()


def anal():
    global current
    current = sor_every[-1][0]
    setup()
    sor_every.pop()


def yes():
    global current
    anal()
    with open(MARK + str(current) + '.txt', 'w') as answers:
        answers.write('1')


def no():
    global current
    anal()
    with open(MARK + str(current) + '.txt', 'w') as answers:
        answers.write('0')


def setup():
    packText(current)
    packAns()


def main():
    setup()
    root.mainloop()


main()
