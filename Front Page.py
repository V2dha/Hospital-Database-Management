from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
import NewRegistration as new_r
import ViewRegistration as view_r

#---------------------Main Window--------------------
window1 = Tk()
window1.title('Welcome')
window1.geometry('2000x1000')
window1.config()
path1 = r'1.jpg'
image1 = ImageTk.PhotoImage(Image.open(path1))
image1_label = Label(window1, image=image1, height=2000, width=2000)
image1_label.image = image1
image1_label.place(x=0, y=0)
welcome_label = Label(window1, text='GALAXY HOSPITAL', bd=6, fg='white', bg='black', relief=RAISED, font=('ariel', 50))
welcome_label.place(x=550, y=20)
Label(window1, text='"where every life counts...."', bd=6, bg='sky blue', font=('ariel', 20, 'italic')).place(x=700, y=120)


#--------------BUTTONS-------------------------------
register = Button(window1, text='New Appointment', font=('ariel', 20), command=new_r.Newregist)
register.place(x=800, y=300)

view = Button(window1, text='View Appointment', font=('ariel', 20), command=view_r.Viewregist)
view.place(x=800, y=400)

close = Button(window1, text='Close', font=('ariel', 20), command=window1.destroy)
close.place(x=860, y=500)

window1.mainloop()


######made by Vividha