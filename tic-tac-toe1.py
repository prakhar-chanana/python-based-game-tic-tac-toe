from tkinter import *
from tkinter import messagebox as msb

c = 0
zzz = [2, 2, 2, 2, 2, 2, 2, 2, 2]
xxx = 0
v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0
v6 = 0
v7 = 0
v8 = 0
v9 = 0


def rst():
    global xxx, c, zzz, v1, v2, v3, v4, v5, v6, v7, v8, v9
    l1.configure(text=" ")
    l2.configure(text=" ")
    l3.configure(text=" ")
    l4.configure(text=" ")
    l5.configure(text=" ")
    l6.configure(text=" ")
    l7.configure(text=" ")
    l8.configure(text=" ")
    l9.configure(text=" ")
    xxx = 0
    c = 0
    zzz = [2, 2, 2, 2, 2, 2, 2, 2, 2]
    zz.set('')
    zz1.set('')
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0
    v5 = 0
    v6 = 0
    v7 = 0
    v8 = 0
    v9 = 0


def wht():
    dd = zzz.count(2)
    if dd == 0:
        ff = msb.askyesno('', 'Restart?')
        if ff == YES:
            rst()
        else:
            quit()


def reset(event):
    global xxx, c, zzz, v1, v2, v3, v4, v5, v6, v7, v8, v9
    l1.configure(text=" ")
    l2.configure(text=" ")
    l3.configure(text=" ")
    l4.configure(text=" ")
    l5.configure(text=" ")
    l6.configure(text=" ")
    l7.configure(text=" ")
    l8.configure(text=" ")
    l9.configure(text=" ")
    xxx = 0
    c = 0
    zzz = [2, 2, 2, 2, 2, 2, 2, 2, 2]
    zz.set('')
    zz1.set('')
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0
    v5 = 0
    v6 = 0
    v7 = 0
    v8 = 0
    v9 = 0


def start(event):
    global xxx
    if zz.get() == "" and zz1.get() == "":
        msb.showwarning("WARNING", 'Please Enter Name of Players !!')
    elif zz.get() == "" and zz1.get() != "":
        msb.showwarning("WARNING", 'Please Enter Name of Player 1')
    elif zz.get() != "" and zz1.get() == "":
        msb.showwarning("WARNING", 'Please Enter Name of Player 2')
    else:
        if xxx == 0:
            l1.bind('<Button-1>', clq1)
            l2.bind('<Button-1>', clq2)
            l3.bind('<Button-1>', clq3)
            l4.bind('<Button-1>', clq4)
            l5.bind('<Button-1>', clq5)
            l6.bind('<Button-1>', clq6)
            l7.bind('<Button-1>', clq7)
            l8.bind('<Button-1>', clq8)
            l9.bind('<Button-1>', clq9)
            xxx = 1


def clq1(event):
    global c, zzz, v1
    if v1 == 0:
        v1 = 1
        if c % 2 == 0:
            event.widget.configure(text='X')
            c += 1
            zzz[0] = 1
        elif c % 2 == 1:
            event.widget.configure(text='O')
            c += 1
            zzz[0] = 0
        check()
        checko()
        wht()


def clq2(event):
    global c, zzz, v2
    if v2 == 0:
        v2 = 1
        if c % 2 == 0:
            event.widget.configure(text='X')
            c += 1
            zzz[1] = 1
        elif c % 2 == 1:
            event.widget.configure(text='O')
            c += 1
            zzz[1] = 0
        check()
        checko()
        wht()


def clq3(event):
    global c, zzz, v3
    if v3 == 0:
        v3 = 1
        if c % 2 == 0:
            event.widget.configure(text='X')
            c += 1
            zzz[2] = 1
        elif c % 2 == 1:
            event.widget.configure(text='O')
            c += 1
            zzz[2] = 0
        check()
        checko()
        wht()


def clq4(event):
    global c, zzz, v4
    if v4 == 0:
        v4 = 1
        if c % 2 == 0:
            event.widget.configure(text='X')
            c += 1
            zzz[3] = 1
        elif c % 2 == 1:
            event.widget.configure(text='O')
            c += 1
            zzz[3] = 0
        check()
        checko()
        wht()


def clq5(event):
    global c, zzz, v5
    if v5 == 0:
        v5 = 1
        if c % 2 == 0:
            event.widget.configure(text='X')
            c += 1
            zzz[4] = 1
        elif c % 2 == 1:
            event.widget.configure(text='O')
            c += 1
            zzz[4] = 0
        check()
        checko()
        wht()


def clq6(event):
    global c, zzz, v6
    if v6 == 0:
        v6 = 1
        if c % 2 == 0:
            event.widget.configure(text='X')
            c += 1
            zzz[5] = 1
        elif c % 2 == 1:
            event.widget.configure(text='O')
            c += 1
            zzz[5] = 0
        check()
        checko()
        wht()


def clq7(event):
    global c, zzz, v7
    if v7 == 0:
        v7 = 1
        if c % 2 == 0:
            event.widget.configure(text='X')
            c += 1
            zzz[6] = 1
        elif c % 2 == 1:
            event.widget.configure(text='O')
            c += 1
            zzz[6] = 0
        check()
        checko()
        wht()


def clq8(event):
    global c, zzz, v8
    if v8 == 0:
        v8 = 1
        if c % 2 == 0:
            event.widget.configure(text='X')
            c += 1
            zzz[7] = 1
        elif c % 2 == 1:
            event.widget.configure(text='O')
            c += 1
            zzz[7] = 0
        check()
        checko()
        wht()


def clq9(event):
    global c, zzz, v9
    if v9 == 0:
        v9 = 1
        if c % 2 == 0:
            event.widget.configure(text='X')
            c += 1
            zzz[8] = 1
        elif c % 2 == 1:
            event.widget.configure(text='O')
            c += 1
            zzz[8] = 0
        check()
        checko()
        wht()


def check():
    if zzz[0] == 1:
        if zzz[1] == 1:
            if zzz[2] == 1:
                msb.showinfo('Winner', 'Winner is {}'.format(zz.get()))
                rst()
        if zzz[3] == 1:
            if zzz[6] == 1:
                msb.showinfo('Winner', 'Winner is {}'.format(zz.get()))
                rst()
        if zzz[4] == 1:
            if zzz[8] == 1:
                msb.showinfo('Winner', 'Winner is {}'.format(zz.get()))
                rst()
    if zzz[1] == 1:
        if zzz[4] == 1:
            if zzz[7] == 1:
                msb.showinfo('Winner', 'Winner is {}'.format(zz.get()))
                rst()
    if zzz[2] == 1:
        if zzz[4] == 1:
            if zzz[6] == 1:
                msb.showinfo('Winner', 'Winner is {}'.format(zz.get()))
                rst()
        if zzz[5] == 1:
            if zzz[8] == 1:
                msb.showinfo('Winner', 'Winner is {}'.format(zz.get()))
                rst()
    if zzz[3] == 1:
        if zzz[4] == 1:
            if zzz[5] == 1:
                msb.showinfo('Winner', 'Winner is {}'.format(zz.get()))
                rst()
    if zzz[6] == 1:
        if zzz[7] == 1:
            if zzz[8] == 1:
                msb.showinfo('Winner', 'Winner is {}'.format(zz.get()))
                rst()


def checko():
    if zzz[0] == 0:
        if zzz[1] == 0:
            if zzz[2] == 0:
                msb.showinfo('Winner', 'Winner is {}'.format(zz1.get()))
                rst()
        if zzz[3] == 0:
            if zzz[6] == 0:
                msb.showinfo('Winner', 'Winner is {}'.format(zz1.get()))
                rst()
        if zzz[4] == 0:
            if zzz[8] == 0:
                msb.showinfo('Winner', 'Winner is {}'.format(zz1.get()))
                rst()
    if zzz[1] == 0:
        if zzz[4] == 0:
            if zzz[7] == 0:
                msb.showinfo('Winner', 'Winner is {}'.format(zz1.get()))
                rst()
    if zzz[2] == 0:
        if zzz[4] == 0:
            if zzz[6] == 0:
                msb.showinfo('Winner', 'Winner is {}'.format(zz1.get()))
                rst()
        if zzz[5] == 0:
            if zzz[8] == 0:
                msb.showinfo('Winner', 'Winner is {}'.format(zz1.get()))
                rst()
    if zzz[3] == 0:
        if zzz[4] == 0:
            if zzz[5] == 0:
                msb.showinfo('Winner', 'Winner is {}'.format(zz1.get()))
                rst()
    if zzz[6] == 0:
        if zzz[7] == 0:
            if zzz[8] == 0:
                msb.showinfo('Winner', 'Winner is {}'.format(zz1.get()))
                rst()


so = Tk()
so.geometry('583x790')
so.title('TIC-TAC-TOE')

zz = StringVar()
zz1 = StringVar()
ttt = IntVar()

Label(so, text="TIC-TAC-TOE", justify=CENTER, fg='yellow', bg='black', font=('Arial Black', 30)).pack(fill=X)

f1 = Frame(so)
f1.pack(fill=X)

a1 = Frame(f1, height=150)
a1.pack(side=LEFT, fill=BOTH, expand=YES)
Label(a1, text="Player 1 :", justify=CENTER, font=('arial', 25)).pack(fill=X)
Label(a1, text="Player 2 :", justify=CENTER, font=('arial', 25)).pack(fill=X)
k = Button(a1, text='Reset', font=('arial', 15))
k.pack()
k.bind('<Button-1>', reset)

a2 = Frame(f1, height=150)
a2.pack(side=RIGHT, fill=BOTH, expand=YES)
Entry(a2, textvariable=zz, font=('arial', 20), bd=5).pack(fill=X)
Entry(a2, textvariable=zz1, font=('arial', 20), bd=5).pack(fill=X)
b = Button(a2, text='Start', font=('arial', 15))
b.pack()
b.bind('<Button-1>', start)

f2 = Frame(so, bg='Green')
f2.pack(fill=BOTH, expand=YES)

b1 = Frame(f2, bg='light blue', height=200, width=200)
b1.grid(row=0, column=0, padx=2, pady=2)
l1 = Label(b1, text=" ", font=('Arial Black', 50), fg='Black', bg='Light Blue', width=4, height=2)
l1.pack()
# l1.bind('<Button-1>', clq1)

b2 = Frame(f2, bg='light blue', height=200, width=200)
b2.grid(row=0, column=1, padx=2, pady=2)
l2 = Label(b2, text=" ", font=('Arial Black', 50), fg='Black', bg='Light Blue', width=4, height=2)
l2.pack()
# l2.bind('<Button-1>', clq2)

b3 = Frame(f2, bg='light blue', height=200, width=200)
b3.grid(row=0, column=2, padx=2, pady=2)
l3 = Label(b3, text=" ", font=('Arial Black', 50), fg='Black', bg='Light Blue', width=4, height=2)
l3.pack()
# l3.bind('<Button-1>', clq3)

b4 = Frame(f2, bg='light blue', height=200, width=200)
b4.grid(row=1, column=0, padx=2, pady=2)
l4 = Label(b4, text=" ", font=('Arial Black', 50), fg='Black', bg='Light Blue', width=4, height=2)
l4.pack()
# l4.bind('<Button-1>', clq4)

b5 = Frame(f2, bg='light blue', height=200, width=200)
b5.grid(row=1, column=1, padx=2, pady=2)
l5 = Label(b5, text=" ", font=('Arial Black', 50), fg='Black', bg='Light Blue', width=4, height=2)
l5.pack()
# l5.bind('<Button-1>', clq5)

b6 = Frame(f2, bg='light blue', height=200, width=200)
b6.grid(row=1, column=2, padx=2, pady=2)
l6 = Label(b6, text=" ", font=('Arial Black', 50), fg='Black', bg='Light Blue', width=4, height=2)
l6.pack()
# l6.bind('<Button-1>', clq6)

b7 = Frame(f2, bg='light blue', height=200, width=200)
b7.grid(row=2, column=0, padx=2, pady=2)
l7 = Label(b7, text=" ", font=('Arial Black', 50), fg='Black', bg='Light Blue', width=4, height=2)
l7.pack()
# l7.bind('<Button-1>', clq7)

b8 = Frame(f2, bg='light blue', height=200, width=200)
b8.grid(row=2, column=1, padx=2, pady=2)
l8 = Label(b8, text=" ", font=('Arial Black', 50), fg='Black', bg='Light Blue', width=4, height=2)
l8.pack()
# l8.bind('<Button-1>', clq8)

b9 = Frame(f2, bg='light blue', height=200, width=200)
b9.grid(row=2, column=2, padx=2, pady=2)
l9 = Label(b9, text=" ", font=('Arial Black', 50), fg='Black', bg='Light Blue', width=4, height=2)
l9.pack()
# l9.bind('<Button-1>', clq9)

so.mainloop()
