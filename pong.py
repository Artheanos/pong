import time,os,threading,random,sys
try:
    from tkinter import *
    from tkinter import font
except ImportError:
    print("Please use Python3. If you did, then I don't know what's wrong")
    sys.exit()

os.system('xset r off')

root = Tk()
root.winfo_toplevel().title("Cyka")
root.configure(background='black')

w = 500
h = 700
x = ((root.winfo_screenwidth()-w)/2)
y = ((root.winfo_screenheight()-h)/2)
root.geometry('%dx%d+%d+%d' % (w,h,x,y))

top = Frame(root, height=50, width=w, background="black")
top.pack()
top.pack_propagate(0)

helv = font.Font(family='Helvetica', size=26, weight='bold')
l1 = Label(top, bg="black", fg="white", text="PRESS SPACE", padx=120, font=helv)
l1.pack(side=LEFT,anchor=CENTER)
l2 = Label(top, bg="black", fg="white", text="", padx=120, font=helv)
l2.pack(side=RIGHT,anchor=CENTER)

#bot = Frame(root)
#bot.pack(side=BOTTOM)
cw = w-100
ch = h-100
bd=10

pl=40
c = Canvas(root, background="white", width=cw, height=ch)
c.pack(anchor=CENTER)
line = c.create_line(10,(ch-40)/2,10,(ch+40)/2,fill="red",width=5)
line2 = c.create_line(cw-10,(ch-40)/2,cw-10,(ch+40)/2,fill="blue",width=5)
ball = c.create_oval((cw-bd)/2,(ch-bd)/2,(cw+bd)/2,(ch+bd)/2, fill="black")

a=0;a2=0
b=0;b2=0
fx=0;fy=0
s1=0;s2=0

def key(event):
    global a,b,a2,b2,fx,fy
    ek = event.keysym
    print(repr(ek))
    if ek == "space" and not fx:
        if random.random()<=0.5:
            fx=3
        else:
            fx=-3
        l1['text']=s1
        l2['text']=s2
        move()
    if ek == "s":
        a=1;a2+=1
    if ek == "w":
        a=-1;a2+=1
    if ek == "Down":
        b=1;b2+=1
    if ek == "Up":
        b=-1;b2+=1
    if ek == "r":
        root.mainloop()

def move():
    global fx,fy
    while 1:
        x1=c.coords(ball)[0]
        y1=c.coords(ball)[1]
        x2=c.coords(ball)[2]
        y2=c.coords(ball)[3]

        if x2 >= c.coords(line2)[0] and y1 <= c.coords(line2)[3] and y2 >= c.coords(line2)[1]:
            fx*=-1
            hit(c.coords(line2)[1])
        if x1 <= c.coords(line)[2] and y1 <= c.coords(line)[3] and y2 >= c.coords(line)[1]:
            fx*=-1
            hit(c.coords(line)[1])
        if y2 > ch:
            fy*=-1
        if y1 < 0:
            fy*=-1

        if x2 > cw:
            reset(1)
        if x2 < 0:
            reset(2)

        c.move(line,0,4*a)
        c.move(line2,0,4*b)
        c.move(ball,fx,fy)
        time.sleep(1/60)
        c.update()

def hit(y):
    global fy
    diff = (y+pl/2) - (c.coords(ball)[1]+bd/2)
    fy-=diff/10

def reset(point):
    global ball,fx,fy,s1,s2
    if point==1:
        s1+=1
    if point==2:
        s2+=1
    c.delete(ball)
    ball = c.create_oval((cw-bd)/2,(ch-bd)/2,(cw+bd)/2,(ch+bd)/2, fill="black")
    fx=0 ; fy=0
    l1['text']=s1
    l2['text']=s2

def stop(event):
    global a,b,a2,b2
    ek = event.keysym
    if ek in ["w","s"]:
        a2-=1
        a=a*a2
    if ek in ["Down","Up"]:
        b2-=1
        b=b*b2

'''def stop(event):
    ek = event.keysym
    if ek in [p.down,p.up]:
        stop()
    if ek in [p2.down,p2.up]:
        stop()'''

root.bind("<KeyPress>",key)
root.bind("<KeyRelease>",stop)

#butt = Button(top, text="Dupa")
#label = Label(bot, text="Trolololo")

root.mainloop()

os.system('xset r on')