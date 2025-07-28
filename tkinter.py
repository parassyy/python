import tkinter
import mysql.connector
import tkinter.messagebox

cn=mysql.connector.connect(database="db1",
                           user="root",
                           password="system",
                           host="localhost",
                           port="3306")
c=cn.cursor()
            

window=tkinter.Tk()
window.title("Calculator")
window.geometry("500x400+400+200")
window.config(bg="pink")
l1=tkinter.Label(window,text="Name",font=("Arial",16),fg="blue",bg="pink")
l2=tkinter.Label(window,text="UserName",font=("Arial",16),fg="blue",bg="pink")
l3=tkinter.Label(window,text="Password",font=("Arial",16),fg="blue",bg="pink")

l1.place(x=100,y=100)
l2.place(x=100,y=150)
l3.place(x=100,y=200)

e1=tkinter.Entry(window,width=15,font=('Arial',16),fg='red')
e2=tkinter.Entry(window,width=15,font=('Arial',16),fg='red')
e3=tkinter.Entry(window,width=15,font=('Arial',16),fg='red',show='*')
                 
e1.place(x=250,y=100)
e2.place(x=250,y=150)
e3.place(x=250,y=200)

def register():
    name=e1.get()
    uname=e2.get()
    pwd=e3.get()

    sql="insert into resuser values(%s,%s,%s)"
    try:
        c.execute(sql,params=(name,uname,pwd))
        cn.commit()
        tkinter.messagebox.showinfo(title="info",message="User Regested successfully..")
        e1.delete(0,tkinter.END)
        e2.delete(0,tkinter.END)
        e3.delete(0,tkinter.END)
    except:
        tkinter.messagebox.showerror(title="error",message="Error in Register")

def close():
    window.destroy()

b1=tkinter.Button(window,text="Register",font=("Arial",16),fg="green",width=10,command=register)
b2=tkinter.Button(window,text="Close",font=("Arial",16),fg="green",width=10,command=close)

b1.place(x=100,y=250)
b2.place(x=250,y=250)

l4=tkinter.Label(window,text="User Registration From",font=("Arial",16),fg="red",bg="pink")

l4.place(x=120,y=10)
                    
    
    
