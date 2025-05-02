from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from Student import Student
from Train import Train
from newface import Face_Recognition

#-------------------------------PART 1/9------------------------------------------------------------------
#-------------------------------FACE RECOGNITION SYSTEM INTERFACE-------------------------------------------------------

class Face_Rec:
    def __init__(self, root):
        self.root=root

        self.root.title("Face Recognition Software")
        self.root.attributes('-fullscreen',True)
        img= Image.open(r"C:\Users\Dhruv Sunil\Desktop\NTCC Project 2nd Yr\Face Recognition System\New folder\pop.jpg")
        img= img.resize((1536,864))
        self.pic= ImageTk.PhotoImage(img)
        label= Label(self.root, image=self.pic)
        label.place(x=0, y=0, height=864, width=1536)

        #button1
        img2=Image.open(r"C:\Users\Dhruv Sunil\Desktop\NTCC Project 2nd Yr\Face Recognition System\New folder\student.jpg")
        self.pic2= ImageTk.PhotoImage(img2)
        bt1=Button(label, image=self.pic2, command=self.student_details)
        bt1.place(x=200, y=200, width=200, height=200)
        label2=Label(label, text="Student Details", bg='black', fg='white', font=('Californian FB', 16))
        label2.place(x=200, y=400, width=200, height=30)

        #button2
        img3=Image.open(r"C:\Users\Dhruv Sunil\Desktop\NTCC Project 2nd Yr\Face Recognition System\New folder\train.jpg")
        img3= img3.resize((200,200))
        self.pic3= ImageTk.PhotoImage(img3)
        bt2=Button(label, image=self.pic3, command=self.training)
        bt2.place(x=500, y=200, width=200, height=200)
        label3=Label(label, text="Train Data", bg='black', fg='white', font=('Californian FB', 16))
        label3.place(x=500, y=400, width=200, height=30)


        #button3
        img4=Image.open(r"C:\Users\Dhruv Sunil\Desktop\NTCC Project 2nd Yr\Face Recognition System\New folder\face.png")
        img4= img4.resize((200,200))
        self.pic4= ImageTk.PhotoImage(img4)
        bt3=Button(label, image=self.pic4, command=self.face)
        bt3.place(x=200, y=500, width=200, height=200)
        label4=Label(label, text="Face Detector", bg='black', fg='white', font=('Californian FB', 16))
        label4.place(x=200, y=700, width=200, height=30)

        #button4
        img5=Image.open(r"C:\Users\Dhruv Sunil\Desktop\NTCC Project 2nd Yr\Face Recognition System\New folder\exit.jpg")
        img5= img5.resize((200,200))
        self.pic5= ImageTk.PhotoImage(img5)
        bt4=Button(label, image=self.pic5)
        bt4.place(x=500, y=500, width=200, height=200)
        label5=Label(label, text="Exit", bg='black', fg='white', font=('Californian FB', 16))
        label5.place(x=500, y=700, width=200, height=30)


#-----------------------------STUDENT MANAGEMENT SYSTEM FUNCTION----------------------------------------------------------------------------
    def student_details(self):
        self.new_window= Toplevel(self.root)
        self.app= Student(self.new_window)

    
    def training(self):
        self.new_window= Toplevel(self.root)
        self.app= Train(self.new_window)
    

    def face(self):
        self.new_window= Toplevel(self.root)
        self.app= Face_Recognition(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj= Face_Rec(root)
    root.mainloop()
#-------------------------------PART 1/9------------------------------------------------------------------
