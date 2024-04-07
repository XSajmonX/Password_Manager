import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

win = tk.Tk()
win.title("Password Manager")
win.minsize(500,200)
win.configure(background="black")

hiden = 'x-x-x-x-x-x'

# reading cryptograms fromn csv file
key = []
crypt1 = []
crypt2 = []
read = open('cryptograms.csv','r')
if read.readable():
    print("to read")
for i in read:
    #print(i.split(',')[0])
    key.append(i.split(",")[0])
    crypt1.append(i.split(",")[1])
    crypt2.append(i.split(",")[2])
print(crypt2)
read.close()
soc = key
login = crypt1
passwords = crypt2

dictionary = dict()
for i in range(len(login)):
    dictionary.update({key[i]:[login[i],passwords[i]]})

# verification system
def log(val,f1,f2):
    secret = "a"        # Password to Enter
    if val == secret:
        f1.forget()
        f2.pack(anchor="center",pady=20)
        win.unbind("<Return>")
    else:
        error_mess = tk.messagebox.showerror(title="ERROR",message="Wrong password! Try again")

# GUI verification system
f1 = ttk.LabelFrame(win, text="Login to system",padding=15)
f1.pack(anchor="center",pady=20)
l1 = ttk.Label(f1,text="Password: ")
l1.grid(row=0,column=0,pady=5,padx=5)
val = tk.StringVar()
e1 = ttk.Entry(f1,show="*",textvariable=val,width=15)
e1.grid(row=0,column=1,pady=5,padx=5)

f2 = ttk.LabelFrame(win,text="Menu",padding=15)
f3 = ttk.LabelFrame(win,text="All passwords",padding=15)

bs = []
y=0
k = []
pas = []
serv = []


# Display all passwords
for i in range(len(login)):
    social = ttk.Label(f3, text=key[i], background="blue", width=25).grid(row=i, column=y, pady=5, padx=5)

    serv.append(ttk.Label(f3, text=hiden, background="green", width=25))
    serv[i].grid(row=i, column=y+1, pady=5, padx=5)

    pas.append(ttk.Label(f3,text=hiden,background="yellow",width=25))
    pas[i].grid(row=i,column=y+2,pady=5,padx=5)

    k.append(i)
    bs.append(ttk.Button(f3, text='show', command= lambda j=i : click(j)))
    bs[i].atr = True
    bs[i].grid(row=i, column=y + 3)


def click(i):

    if(bs[i].atr):
        bs[i].configure(text="hide")
        bs[i].atr = False
        pas[i].configure(text=passwords[i])
        serv[i].configure(text=login[i])

    else:
        bs[i].configure(text="show")
        bs[i].atr = True
        pas[i].configure(text=hiden)
        serv[i].configure(text=hiden)

    bs[i].grid(row=i, column=y + 3)
    pas[i].grid(row=i, column=y + 2)

# Changing Frames
def show(f2,f3):
    f2.pack_forget()
    f3.pack(anchor="center",pady=20)
# Saveing cryptograms to csv file
def save_data():
    write = open('cryptograms.csv','w')
    for i in range(len(soc)):
        write.writelines(soc[i]+","+login[i]+","+passwords[i]+",0"+"\n")
    write.close()
# close program and save data
def exit_program():
    save_data()
    win.destroy()

# Return from Passwords Frame to Menu Frame
def back(f3,f2):
    f3.pack_forget()
    f2.pack(anchor="center",pady=20)

def return_BUTT(f,x,y,f3,f2):
    b5 = ttk.Button(f, text="back", command=lambda: back(f3,f2))
    b5.grid(row=x, column=y+1, pady=5, padx=5)
def add():
    f2.pack_forget()
    f4.pack(anchor="center",pady=20)

# System of adding new Password and Service to databse
def add_p(s,l,p,p1,dictionary):
    if s in dictionary:
        answer = tk.messagebox.askyesno(title="Warning", message="This Service is already exist!")
        if answer == True:
            print(len(p), len(p1))
            if (len(p) and len(p1)) == 0:
                print("error")
            elif p == p1:
                print("ok")

                dictionary.update({s: [l, p]})
                print(dictionary)

                service_entry.delete(0, "end")
                login_entry.delete(0, "end")
                pass_entry.delete(0, "end")
                pass_entry1.delete(0, "end")
            return 0

    print(len(p), len(p1))
    if (len(p) and len(p1)) == 0:
        print("error")
    elif p == p1:
        print("ok")

        dictionary.update({s:[l,p]})
        print(dictionary)

        service_entry.delete(0,"end")
        login_entry.delete(0,"end")
        pass_entry.delete(0,"end")
        pass_entry1.delete(0,"end")

    else:
        print("not ok")

def delete_pass(s,dictionary):
    if s in dictionary:
        answer = messagebox.askyesno(title="Warning", message="Are you sure?")
        if answer == True:
            dictionary.pop(s)

f4 = ttk.LabelFrame(win,text="Add/Change password")
return_BUTT(f4,1,1,f4,f2)

service_label = ttk.Label(f4,text="Service: ")
service_label.grid(row=1,column=0,pady=5,padx=5)
s = tk.StringVar()
service_entry = ttk.Entry(f4,textvariable=s,width=25)
service_entry.grid(row=1,column=1,pady=5,padx=5)

login_label = ttk.Label(f4,text="Login: ")
login_label.grid(row=2,column=0,pady=5,padx=5)
l = tk.StringVar()
login_entry = ttk.Entry(f4,textvariable=l,width=25)
login_entry.grid(row=2,column=1,pady=5,padx=5)

pass_label = ttk.Label(f4,text="Password: ")
pass_label.grid(row=3,column=0,pady=5,padx=5)
p = tk.StringVar()
pass_entry = ttk.Entry(f4,textvariable=p,width=25,show="*")
pass_entry.grid(row=3,column=1,pady=5,padx=5)

pass_label1 = ttk.Label(f4,text="Password again: ")
pass_label1.grid(row=4,column=0,pady=5,padx=5)
p1 = tk.StringVar()
pass_entry1 = ttk.Entry(f4,textvariable=p1,width=25,show="*")
pass_entry1.grid(row=4,column=1,pady=5,padx=5)


add_pass = ttk.Button(f4,text="add/change",command=lambda: add_p(s.get(),l.get(),p.get(),p1.get(),dictionary))
add_pass.grid(row=2,column=2,pady=5,padx=5)
delete = ttk.Button(f4,text="Remove",command=lambda: delete_pass(s.get(),dictionary))
delete.grid(row=3,column=2,pady=5,padx=5)
# Menu Frame and Buttons

b2 = ttk.Button(f2,text="Add/Change",command=add).grid(row=0,column=0,pady=5,padx=5)
b3 = ttk.Button(f2,text="All Passwords",command=lambda: show(f2,f3)).grid(row=0,column=1,pady=5,padx=5)
b4 = ttk.Button(f2,text="Exit",command=exit_program).grid(row=1,column=0,columnspan=2,pady=5,padx=5)
win.protocol("WM_DELETE_WINDOW", save_data())
return_BUTT(f3,0,3,f3,f2)
b1 = ttk.Button(f1,text="Check_it",command=lambda:log(val.get(),f1,f2))
win.bind("<Return>",lambda z: log(val.get(),f1,f2))
b1.grid(row=1,column=1,pady=5)



win.mainloop()

