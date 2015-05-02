from Tkinter import *
from tkFileDialog   import askopenfilename
import socket
import tkMessageBox

info=''
name=''
d=''
n=''
flag=0


def client():
    port=8000
    host='127.0.0.1'
    so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s=so

def getinfo():
    global info
    info=v.get()
    info=info+'\n'
    T.insert(END, info)
    startclient()

def callback():
    global name
    global flag
    flag=1
    name= askopenfilename()
    return name

def startclient():
    global n,d,flag,s
    # port=8000
    # count=0
    # # host=z.get()
    # host='127.0.0.1'
    # s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # s.connect((host,port))
    s.connect((host,port))

    d=v.get()
    textfield.delete(0,'end')

    n=name
    msg='client started'
    if n=='' and d=='':
        tkMessageBox.showinfo('client','choose a file or type something!!!')
    if flag==1:
        s.sendall(n)
        flag=0
    if d!='':
        s.sendall(d)    
    

root = Tk().geometry("550x550")
v=StringVar()
z=StringVar()
tframe=Frame(root)
tframe.pack(side=TOP,pady=10)
labelcl=Label(tframe,text="enter the HOST..")
labelcl.pack()
clport=Entry(tframe,textvariable=z)
clport.pack()
serverbtn=Button(tframe,text="Start Client..",fg="red",command=client)
serverbtn.pack(pady=10)
textbtn=Button(tframe,text="Choose text..",fg="white",bg="red",command=callback)
imagebtn=Button(tframe,text="Choose image..",fg="white",bg="green",command=callback)
videobtn=Button(tframe,text="Choose video..",fg="white",bg="black",command=callback)
sendbtn=Button(tframe,text="Send...",fg="black",command=startclient)
textbtn.pack(side=LEFT,padx=5)
videobtn.pack(side=LEFT,padx=5)
imagebtn.pack(side=LEFT,padx=5)
sendbtn.pack(side=RIGHT)
frame=Frame(root)
frame.pack()
label=Label(frame,text="You have entered this....")
label.pack(side=TOP,pady=20)
S = Scrollbar(frame)
T = Text(frame, height=10, width=50)
S.pack(side=RIGHT,fill=Y)
T.pack(side=LEFT)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
# T.insert(END, info)
bframe=Frame(root)
bframe.pack(side=BOTTOM)
tlabel=Label(bframe,text="Enter your text here...")
tlabel.pack()
textfield=Entry(bframe,width=50,textvariable=v,justify=LEFT)
textfield.pack(side=LEFT)
sendbtn=Button(bframe,text="Send",command=getinfo)
sendbtn.pack(side=LEFT)

mainloop()