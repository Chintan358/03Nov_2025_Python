from tkinter import *
import mysql.connector


con = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="3nov_python"
)
cursor = con.cursor()

root = Tk()



root.geometry("500x500")

# btn = Button(root,text="submit").pack(side=LEFT)
# btn1 = Button(root,text="reset").pack(sid=RIGHT)
# btn2 = Button(root,text="submit").pack(side=TOP)
# btn3 = Button(root,text="reset").pack(side=BOTTOM)
# btn4 = Button(root,text="reset").pack()


# l1 = Label(root,text="Username").grid(row=1,column=1)
# l2 = Label(root,text="Email").grid(row=2,column=1)
# e1 = Entry()
# e2 = Entry()
# e1.grid(row=1,column=2)
# e2.grid(row=2,column=3)
# btn = Button(root,text="Submit").grid(row=3,column=2)


def add():
    username = e1.get()
    email = e2.get()
    qry = "insert into user values(%s,%s,%s)"
    val = (0,username,email)
    cursor.execute(qry,val)
    con.commit()
    e1.delete(0,END)
    e2.delete(0,END)

l1 = Label(root,text="Username").place(x=100,y=100)
l2 = Label(root,text="Email").place(x=100,y=150)

e1 = Entry()
e2 = Entry()

e1.place(x=200,y=100)
e2.place(x=200,y=150)

btn = Button(root,text="Submit",width=15,command=add).place(x=200,y=200)


root.mainloop()