from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

#------------------------------------------------PART 5/9-------------------------------------------------
#-----------------------------------------STUDENT MANAGEMENT SYSTEM---------------------------------------
class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("800x500+350+0")
        self.root.title("Face Recognition Software")
        img= Image.open(r"C:\\Users\\Dhruv Sunil\\Desktop\\NTCC Project 2nd Yr\\Face Recognition System\\New folder\\TRAIN_data.jpg")
        img= img.resize((800,500))
        self.pic= ImageTk.PhotoImage(img)
        label= Label(self.root, image=self.pic)
        label.place(x=0, y=0, height=500, width=800)


        style = ttk.Style()

# Defining custom style for the button
        style.configure('Custom.TButton',width=30, height=50, background='lightblue', foreground='black', font=('Californian FB', 14, 'bold'), padding=10)


# Set an active background color when the button is pressed or hovered over
        style.map('Custom.TButton',
          background=[('active', 'blue'), ('pressed', 'darkblue')],
          foreground=[('active', 'black'), ('pressed', 'black')])
        

        btn1= ttk.Button(label, text="TRAIN DATA", command=self.train_classifier, style="Custom.TButton")
        btn1.place(x=235, y= 230)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            
            img=Image.open(image).convert("L") #Gray Scale Image
            img_np=np.array(img, "uint8")
            id=int(os.path.split(image)[1].split(".")[1])

            faces.append(img_np)
            ids.append(id)
            cv2.imshow("Training", img_np)
            cv2.waitKey(1)==13
        ids=np.array(ids)
    
#====================Train the classifier and save=======================================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("Untitled.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!")



if __name__ == "__main__":
    root=Tk()
    obj= Train(root)
    root.mainloop()