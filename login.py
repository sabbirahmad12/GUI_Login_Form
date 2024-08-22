from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Login')
root.geometry('925x500+250+150')
root.config(bg='#fff')

# Function
def sign_in():
    username_= username.get()
    password_= password.get()

    if username_ == 'sabbir' and password_ == '1234':
        screen = Toplevel(root) 
        screen.title('App')
        screen.geometry("925x500+250+150")
        screen.config(bg='#fff')

        Label(screen, text= "Hello Everyone!", bg= '#fff', font=('Calibri(Body)',50,'bold')).pack(expand=True)

    elif username_ != 'sabbir' and password_ != '1234':
        messagebox.showerror("Invalid", "Invalid username and password")

    elif username_ != 'sabbir':
        messagebox.showerror("Invalid", "Invalid username")

    elif password_ != '1234':
        messagebox.showerror("Invalid", "Invalid password")


# Image Section

img = ImageTk.PhotoImage(Image.open('login.png'))

Label(root, image=img , bg='white').place(x= 50, y= 50)

# Login Frame
frame = Frame(root, width=350, height=350, bg= 'white')
frame.place(x=500, y= 70)

heading = Label(frame, text= 'Sign in', fg= '#57a1f8', bg= 'white', font= ('Microsoft YaHei UI Light', 25,'bold'))
heading.place(x=125, y = 5)

# username
def on_enter(e):
    username.delete(0, 'end')

def on_leave(e):
    name = username.get()
    if name == '':
        username.insert(0, 'Username')

username = Entry(frame, width= 30,fg = 'black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
username.place(x=55, y=80)
username.insert(0,'Username')
username.bind('<FocusIn>', on_enter)
username.bind('<FocusOut>', on_leave)

Frame(frame,width=250,height=2,bg='black').place(x=50,y=107)

# Password
def on_enter(e):
    password.delete(0, 'end')

def on_leave(e):
    pass_ = password.get()
    if pass_ == '':
        password.insert(0, 'Password')

password = Entry(frame, width= 30,fg = 'black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
password.place(x=55, y=150)
password.insert(0,'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame,width=250,height=2,bg='black').place(x=50,y=177)

# Button Section
btn = Button(frame, width=35, pady=7, text='Sign in', bg= '#57a1f8', fg= 'white',border=0, command= sign_in)
btn.place(x=50, y=204)

# Bottom Section 
label = Label(frame, text="Don't have an account?", fg='black', bg= 'white', font=('Microsoft YaHei UI Light',9))
label.place(x=75, y=260)

sign_up_btn = Button(frame, width=6, text= 'Sign up', border = 0, bg = 'white', cursor='hand2', fg= '#57a1f8')
sign_up_btn.place(x=215, y=260)

root.mainloop()
