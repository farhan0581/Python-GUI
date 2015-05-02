from Tkinter import *
import socket
import sys
import bz2
import binascii
import tkMessageBox
# from s1 import startserver

info=''
path='nopath'
def getinfo(var):
    # global info
    # info=v.get()
    # info=info+'\n'
    T.insert(END, var)

# def startserver1():
#     startserver(T)


def startserver():
    # host=v.get()
    global path
    host='127.0.0.1'
    port=8000
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(5)
    tkMessageBox.showinfo('server','server statred!!!')
    # smsg=Label(tframe,text=msg)
    # smsg.pack()
    # getinfo("haha")
    while True:
        #T.insert(END, "waiting for connection")
        print >> sys.stderr,'waiting for connection'
        tkMessageBox.showinfo('server','waiting for connection!!!')
        
        connection , client =  s.accept()
        try:
            # T.insert(END, "connection from")
            print >>sys.stderr, 'connection from', client
            tkMessageBox.showinfo('server','connected to client!!!')
            data    =   connection.recv(1024)
            if data[0]=='/':
                path='file received successfully with path::->' + data
                tlabel.delete(1.0,END)
                tlabel.insert(END,path)
            
            data=data+'\n'
            T.insert(END,data)

            # bz2file=open('Mera Naam Yousuf hai Episode 6_2 .mp4','wb')
            # while True:
            #     data    =   connection.recv(1024)
            #     #print data
            #     if not data:
            #         bz2file.close()
            #         break
            #     bz2file.write(data)
                
        finally:
            connection.close()


    



root = Tk().geometry("500x500")
v=StringVar()
tframe=Frame(root)
tframe.pack(side=TOP,pady=10)
la=Label(tframe,text="Enter HOST!!")
la.pack()
gethost=Entry(tframe,textvariable=v)
gethost.pack()
serverbtn=Button(tframe,text="Start Server..",fg="red",command=startserver)
serverbtn.pack(pady=10)
frame=Frame(root)
frame.pack()
label=Label(frame,text="The sender have send this....")
label.pack(side=TOP,pady=20)
S = Scrollbar(frame)
T = Text(frame, height=10, width=50)
S.pack(side=RIGHT,fill=Y)
T.pack(side=LEFT)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
bframe=Frame(root)
bframe.pack(side=BOTTOM)
tlabel=Text(bframe,height=1,width=80)
tlabel.pack()

mainloop()

