import os
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


#------------------------------------------------PART 2/9-------------------------------------------------
#-----------------------------------------STUDENT MANAGEMENT SYSTEM---------------------------------------
class Student:
    def __init__(self, root):
        self.root=root
        self.root.attributes('-fullscreen',True)
        self.root.title("Face Recognition Software")

        #Variables
        self.var_dep = StringVar()
        self.var_Course = StringVar()
        self.var_Year = StringVar()
        self.var_Sem = StringVar()
        self.var_Prof = StringVar()
        self.var_Sec = StringVar()
        self.var_Name = StringVar()
        self.var_Gender = StringVar()
        self.var_Roll_no = StringVar()
        self.var_Res = StringVar()
        self.var_DOB = StringVar()
        self.var_Add = StringVar()
        self.var_Email = StringVar()
        self.var_Phone = StringVar()


        #BG_IMAGE
        img= Image.open(r"C:\Users\Dhruv Sunil\Desktop\NTCC Project 2nd Yr\Face Recognition System\New folder\std_bg.jpg")
        img= img.resize((1536,864))
        self.pic= ImageTk.PhotoImage(img)
        label= Label(self.root, image=self.pic)
        label.place(x=0, y=0, height=864, width=1536)

        #Main Frame
        main_frame= Frame(label, bg="#E0EFFA")
        main_frame.place(x=90, y=120, width=1360, height=700)

        #Left Frame
        left_frame=LabelFrame(main_frame, bd=5, text="Student Details", relief=RIDGE, font=('Californian FB', 18), bg="#E0EFFA")
        left_frame.place(x=20, y= 20, width=640, height=650)


        left_img=Image.open(r"C:\Users\Dhruv Sunil\Desktop\NTCC Project 2nd Yr\Face Recognition System\New folder\profile.jpeg")
        left_img= left_img.resize((140,170))
        self.pic2= ImageTk.PhotoImage(left_img)
        label2=Label(left_frame, image=self.pic2)
        label2.place(x=10, y=20, width=140, height=170)


        #Course Frame
        Course_frame=LabelFrame(left_frame, bd=1, relief=RAISED, text="Course Info", font=('Californian FB', 14, 'bold'), bg="#E0EFFA")
        Course_frame.place(x=160, y=10, width=460, height=180)

        dep_label= Label(Course_frame, text="Department", font=('Californian FB', 13, 'bold'), bg="#E0EFFA")
        dep_label.grid(row=0, column=0, pady=12)
        dep_combo=ttk.Combobox(Course_frame, textvariable=self.var_dep, width=12, font=('Californian FB', 13), state="readonly")
        dep_combo["values"]=("Select Dept", "Engineering", "Arts", "Law", "Architecture")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=12)

        course_label= Label(Course_frame, text="Course", font=('Californian FB', 13, 'bold'), bg="#E0EFFA")
        course_label.grid(row=0, column=2, pady=12)
        course_combo=ttk.Combobox(Course_frame, textvariable=self.var_Course, width=12, font=('Californian FB', 13), state="readonly")
        course_combo["values"]=("Select Course", "B.Tech(CSE)", "B.Tech(ME)", "B.Tech(AI & ML)", "BACHELOR OF FINE ARTS", "MASTER OF FINE ARTS", "LLB(HONS)", "LLM(Business Law)", "B.Arch.", "B.Plan.", "Master of Urban Design (MUD)")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=5, pady=12)

        year_label= Label(Course_frame, text="Year", font=('Californian FB', 13, 'bold'), bg="#E0EFFA")
        year_label.grid(row=1, column=0, pady=12)
        year_combo=ttk.Combobox(Course_frame, textvariable=self.var_Year, width=12, font=('Californian FB', 13), state="readonly")
        year_combo["values"]=("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=12)

        sem_label= Label(Course_frame, text="Semester", font=('Californian FB', 13, 'bold'), bg="#E0EFFA")
        sem_label.grid(row=1, column=2, pady=12)
        sem_combo=ttk.Combobox(Course_frame, textvariable=self.var_Sem, width=12, font=('Californian FB', 13), state="readonly")
        sem_combo["values"]=("Select Semester", "Sem-1", "Sem-2", "Sem-3", "Sem-4", "Sem-5", "Sem-6", "Sem-7", "Sem-8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=5, pady=12)

        professor_label= Label(Course_frame, text="Professor", font=('Californian FB', 13, 'bold'), bg="#E0EFFA")
        professor_label.grid(row=2, column=0, pady=12)
        professor_combo=ttk.Combobox(Course_frame, textvariable=self.var_Prof, width=12, font=('Californian FB', 13), state="readonly")
        professor_combo["values"]=("Select Professor","Dr. Nancy Gulati", "Dr. Geetika Munjal", "Dr. Sachin Minion")
        professor_combo.current(0)
        professor_combo.grid(row=2, column=1, padx=5, pady=12)

        section_label= Label(Course_frame, text="Section", font=('Californian FB', 13, 'bold'), bg="#E0EFFA")
        section_label.grid(row=2, column=2, pady=12)
        section_combo=ttk.Combobox(Course_frame, textvariable=self.var_Sec, width=12, font=('Californian FB', 13), state="readonly")
        section_combo["values"]=("Select Section","DS-1", "DS-2", "BA-1X", "BA-1Y", "L-1", "Arch-A", "Arch-B")
        section_combo.current(0)
        section_combo.grid(row=2, column=3, padx=5, pady=12)


        #Student Frame
        Student_frame=LabelFrame(left_frame, bd=1, relief=RAISED, text="Student Info", font=('Californian FB', 14, 'bold'), bg="#E0EFFA")
        Student_frame.place(x=10, y=200, width=610, height=400)

        name_label= Label(Student_frame, text="Student Name:", font=('Californian FB', 14, 'bold'), bg="#E0EFFA")
        name_label.grid(row=0, column=0, pady=8, padx=10)
        name_entry= ttk.Entry(Student_frame, textvariable=self.var_Name, width=17, font=('Californian FB', 14))
        name_entry.grid(row=0, column=1)

        id_label= Label(Student_frame, text="Roll No:", font=('Californian FB', 14, 'bold'), bg="#E0EFFA")
        id_label.grid(row=1, column=0, pady=8, padx=10)
        id_entry= ttk.Entry(Student_frame, textvariable=self.var_Roll_no, width=17, font=('Californian FB', 14))
        id_entry.grid(row=1, column=1)

        DOB_label= Label(Student_frame, text="DOB:", font=('Californian FB', 14, 'bold'), bg="#E0EFFA")
        DOB_label.grid(row=2, column=0, pady=8, padx=10)
        DOB_entry= ttk.Entry(Student_frame, textvariable=self.var_DOB, width=17, font=('Californian FB', 14))
        DOB_entry.grid(row=2, column=1)

        Email_label= Label(Student_frame, text="Email:", font=('Californian FB', 14, 'bold'), bg="#E0EFFA")
        Email_label.grid(row=3, column=0, pady=8, padx=10)
        Email_entry= ttk.Entry(Student_frame, textvariable=self.var_Email, width=17, font=('Californian FB', 14))
        Email_entry.grid(row=3, column=1)

        Gender_label= Label(Student_frame, text="Gender:", font=('Californian FB', 14, 'bold'), bg="#E0EFFA")
        Gender_label.grid(row=0, column=2, pady=8, padx=10)
        Gender_entry= ttk.Combobox(Student_frame, textvariable=self.var_Gender, width=15, font=('Californian FB', 14), state="readonly")
        Gender_entry['values']=("Male", "Female", "Other")
        Gender_entry.grid(row=0, column=3)

        Residency_label= Label(Student_frame, text="Residency:", font=('Californian FB', 14, 'bold'), bg="#E0EFFA")
        Residency_label.grid(row=1, column=2, pady=8, padx=10)
        Residency_entry= ttk.Combobox(Student_frame, textvariable=self.var_Res, width=15, font=('Californian FB', 14), state="readonly")
        Residency_entry['values']=("Hostler", "Day Scholar")
        Residency_entry.grid(row=1, column=3)

        Adddress_label= Label(Student_frame, text="Address:", font=('Californian FB', 14, 'bold'), bg="#E0EFFA")
        Adddress_label.grid(row=2, column=2, pady=8, padx=10)
        Adddress_entry= ttk.Entry(Student_frame, textvariable=self.var_Add, width=17, font=('Californian FB', 14))
        Adddress_entry.grid(row=2, column=3)

        Phone_label= Label(Student_frame, text="Phone no:", font=('Californian FB', 14, 'bold'), bg="#E0EFFA")
        Phone_label.grid(row=3, column=2, pady=8, padx=10)
        Phone_entry= ttk.Entry(Student_frame, textvariable=self.var_Phone, width=17, font=('Californian FB', 14))
        Phone_entry.grid(row=3, column=3)

        radbtn_frame= Frame(Student_frame, relief=FLAT, bg="#E0EFFA")
        radbtn_frame.place(x=20, y=200, width=500, height=40)
        #Radio Button
        self.var_radio1=StringVar()
        rad_btn1= ttk.Radiobutton(radbtn_frame, variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        rad_btn1.grid(row=0, column=0, padx=60)

        rad_btn2= ttk.Radiobutton(radbtn_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        rad_btn2.grid(row=0, column=1, padx=60)
                                                                   
        btn_frame= Frame(Student_frame, bd=5, relief=FLAT, bg="#E0EFFA")
        btn_frame.place(x=16, y=240, width=570, height=110)

        style = ttk.Style()

# Defining custom style for the button
        style.configure('Custom.TButton',width=20, height=15, background='lightblue', foreground='black', font=('Californian FB', 12, 'bold'), padding=10)

        style.configure('Custom2.TButton',width=11, height=5, background='lightblue', foreground='black', font=('Californian FB', 12, 'bold'), padding=10)

# Set an active background color when the button is pressed or hovered over
        style.map('Custom.TButton',
          background=[('active', 'blue'), ('pressed', 'darkblue')],
          foreground=[('active', 'black'), ('pressed', 'black')])
        
        style.map('Custom2.TButton',
          background=[('active', 'blue'), ('pressed', 'darkblue')],
          foreground=[('active', 'black'), ('pressed', 'black')])


        save_btn= ttk.Button(btn_frame, text="Save", command=self.add_data, style="Custom.TButton")
        save_btn.grid(row=0, column=0)

        update_btn= ttk.Button(btn_frame, text="Update", command=self.update_data, style="Custom.TButton")
        update_btn.grid(row=0, column=1)

        delete_btn= ttk.Button(btn_frame, text="Delete", command=self.delete_data, style="Custom.TButton")
        delete_btn.grid(row=0, column=2)

        reset_btn= ttk.Button(btn_frame, text="Reset", command=self.reset_data, style="Custom.TButton")
        reset_btn.grid(row=1, column=0)

        photo_btn= ttk.Button(btn_frame, command=self.generate_data , text="Take Photo", style="Custom.TButton")
        photo_btn.grid(row=1, column=1)

        newpic_btn= ttk.Button(btn_frame, text="Update Photo", style="Custom.TButton")
        newpic_btn.grid(row=1, column=2)

        #Right Frame
        right_frame=LabelFrame(main_frame, bd=5, text="Student Search", relief=RIDGE, font=('Californian FB', 18), bg="#E0EFFA")
        right_frame.place(x=690, y= 20, width=640, height=650)

        Search_frame=LabelFrame(right_frame, bd=1, relief=RAISED, text="Search System", font=('Californian FB', 14, 'bold'), bg="#E0EFFA")
        Search_frame.place(x=10, y=10, width=610, height=590)
        
        Search_label= Label(Search_frame, text="Search By: ", font=('Californian FB', 12, 'bold'), bg="#E0EFFA")
        Search_label.grid(row=0, column=0, padx=4, pady=10)

        Search_combo=ttk.Combobox(Search_frame, width=11, font=('Californian FB', 12), state="readonly")
        Search_combo["values"]=("Roll No", "Name")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=4, pady=10)

        Search_entry= ttk.Entry(Search_frame, width=15, font=('Californian FB', 12))
        Search_entry.grid(row=0, column=2, padx=4, pady=10)

        Search_btn= ttk.Button(Search_frame, text="Search", style="Custom2.TButton")
        Search_btn.grid(row=0, column=3, padx=2)

        Show_btn= ttk.Button(Search_frame, text="Show All", style="Custom2.TButton")
        Show_btn.grid(row=0, column=4, padx=2)


        #Table Frame
        Table_frame=Frame(right_frame, bd=1, relief=RAISED, bg="#E0EFFA")
        Table_frame.place(x=10, y=100, width=610, height=500)

        scroll_x=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.student_table= ttk.Treeview(Table_frame, column=("dep", "Course", "Year", "Sem", "Prof", "Sec", "Name", "Gender", "Roll_No", "Res", "DOB", "Add", "Email", "Phone", "PhotoSample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Prof", text="Professor")
        self.student_table.heading("Sec", text="Section")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Roll_No", text="Roll_No")
        self.student_table.heading("Res", text="Residency")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Add", text="Address")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("PhotoSample", text="PhotoSample")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("Prof", width=100)
        self.student_table.column("Sec", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Res", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Add", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("PhotoSample", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


#-------------------------------PART 2/9------------------------------------------------------------------


#-------------------------------PART 3/9------------------------------------------------------------------

#-----------------------FUNCTION DECLARATION---------------------------------------

    def add_data(self):
        if self.var_dep.get()== "Select Dept" or self.var_Name.get()== "" or self.var_Roll_no.get()== "" :
            messagebox.showerror("Error", "All fields must be filled", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_Course.get(),
                                                                                                            self.var_Year.get(),
                                                                                                            self.var_Sem.get(),
                                                                                                            self.var_Prof.get(),
                                                                                                            self.var_Sec.get(),
                                                                                                            self.var_Name.get(),
                                                                                                            self.var_Gender.get(),
                                                                                                            self.var_Roll_no.get(),
                                                                                                            self.var_Res.get(),
                                                                                                            self.var_DOB.get(),
                                                                                                            self.var_Add.get(),
                                                                                                            self.var_Email.get(),
                                                                                                            self.var_Phone.get(),
                                                                                                            self.var_radio1.get()                                                                            
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)
                
#-------------------------------------Fetch Data--------------------------------------      
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

#----------------------------------------Get Cursor-------------------------------------
    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_Course.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Sem.set(data[3]),
        self.var_Prof.set(data[4]),
        self.var_Sec.set(data[5]),
        self.var_Name.set(data[6]),
        self.var_Gender.set(data[7]),
        self.var_Roll_no.set(data[8]),
        self.var_Res.set(data[9]),
        self.var_DOB.set(data[10]),
        self.var_Add.set(data[11]),
        self.var_Email.set(data[12]),
        self.var_Phone.set(data[13]),
        self.var_radio1.set(data[14])
        

#------------------------------------------------Update Function------------------------------------------
    def update_data(self):
        if self.var_dep.get() == "Select Dept" or self.var_Name.get() == "" or self.var_Roll_no.get() == "":
            messagebox.showerror("Error", "All fields must be filled", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update student details", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recognizer")
                    my_cursor = conn.cursor()
                    update_query = "UPDATE student SET dep=%s, Course=%s, Year=%s, Sem=%s, Prof=%s, Section=%s, Name=%s, Gender=%s, Residency=%s, DOB=%s, Address=%s, Email=%s, Phone=%s, PhotoSample=%s WHERE Roll_No=%s"
                    my_cursor.execute(update_query, (
                    self.var_dep.get(),
                    self.var_Course.get(),
                    self.var_Year.get(),
                    self.var_Sem.get(),
                    self.var_Prof.get(),
                    self.var_Sec.get(),
                    self.var_Name.get(),
                    self.var_Gender.get(),
                    self.var_Res.get(),
                    self.var_DOB.get(),
                    self.var_Add.get(),
                    self.var_Email.get(),
                    self.var_Phone.get(),
                    self.var_radio1.get(),
                    self.var_Roll_no.get()
                ))   
                    conn.commit()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)  
                    self.fetch_data()
                    conn.close()
            
                else:
                    return
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}", parent=self.root)


 
#----------------------------------------Delete Function---------------------------

    def delete_data(self):
        if self.var_Roll_no.get()=="" :
            messagebox.showerror("Error", "Student Roll No is required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student deletion", "Do you want to delete this student", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Roll_no=%s"
                    val=(self.var_Roll_no.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
            
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student details successfully deleted", parent=self.root)
            except Exception as es:
                    messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)


#--------------------------Reset Function-----------------------------------

    def reset_data(self):
        self.var_dep.set("Select Dept"),
        self.var_Course.set("Select Course"),
        self.var_Year.set("Select Year"),
        self.var_Sem.set("Select Semester"),
        self.var_Prof.set("Select Professor"),
        self.var_Sec.set("Select section"),
        self.var_Name.set(""),
        self.var_Gender.set(""),
        self.var_Roll_no.set(""),
        self.var_Res.set(""),
        self.var_DOB.set(""),
        self.var_Add.set(""),
        self.var_Email.set(""),
        self.var_Phone.set(""),
        self.var_radio1.set("")


#---------------------------------Dataset Generation-------------------------------------



    def generate_data(self):
        if self.var_dep.get() == "Select Dept" or self.var_Name.get() == "" or self.var_Roll_no.get() == "":
            messagebox.showerror("Error", "All fields must be filled", parent=self.root)
            return
        else:
            try:
            # Connect to the database
                conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT * FROM student")
                my_result = my_cursor.fetchall()
                id=self.var_Roll_no.get()
                
                my_cursor.execute("""UPDATE student SET dep=%s, Course=%s, Year=%s, Sem=%s, Prof=%s, Section=%s, Name=%s, Gender=%s, Residency=%s, DOB=%s, Address=%s, Email=%s, Phone=%s, PhotoSample=%s WHERE Roll_No=%s""", (
                self.var_dep.get(),
                self.var_Course.get(),
                self.var_Year.get(),
                self.var_Sem.get(),
                self.var_Prof.get(),
                self.var_Sec.get(),
                self.var_Name.get(),
                self.var_Gender.get(),
                self.var_Res.get(),
                self.var_DOB.get(),
                self.var_Add.get(),
                self.var_Email.get(),
                self.var_Phone.get(),
                self.var_radio1.get(),
                self.var_Roll_no.get()
            ))
        

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            # Load predefined data
                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    return None
                if not os.path.exists('data'):
                    os.makedirs('data')

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()
                    if ret:
                    
                        cropped_face = face_cropped(my_frame)
                        if cropped_face is not None:
                            img_id += 1
                            face = cv2.resize(cropped_face, (500, 500))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            path = f"C:\\Users\\Dhruv Sunil\\Desktop\\NTCC Project 2nd Yr\\Face Recognition System\\data\\face.{id}.{img_id}.jpg"
                            cv2.imwrite(path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped", face)

                        if cv2.waitKey(1) == 13 or img_id == 200:
                            break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Dataset generated!")
            
            except Exception as es:
                    messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)


#-------------------------------PART 3/9------------------------------------------------------------------


#-------------------------------PART 4/9------------------------------------------------------------------

    





#-------------------------------PART 4/9------------------------------------------------------------------





if __name__ == "__main__":
    root=Tk()
    obj= Student(root)
    root.mainloop()