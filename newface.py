from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, accuracy_score, precision_score, recall_score

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen',True)
        self.root.title("Face Recognition Software")

        img= Image.open(r"C:\\Users\\Dhruv Sunil\\Desktop\\NTCC Project 2nd Yr\\Face Recognition System\\New folder\\TRAIN_data.jpg")
        img= img.resize((1536,864))
        self.pic= ImageTk.PhotoImage(img)
        label= Label(self.root, image=self.pic)
        label.place(x=0, y=0, height=864, width=1536)

        # Button
        Btn_1 = Button(label, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        Btn_1.place(x=600, y=420, width=200, height=40)


    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))
                

                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recognizer")
                    my_cursor = conn.cursor()

                    my_cursor.execute("SELECT Name FROM student WHERE Roll_No = %s", (str(id),))
                    n = my_cursor.fetchone()
                    n = "".join(n) if n else "Unknown"

                    my_cursor.execute("SELECT Roll_No FROM student WHERE Roll_No = %s", (str(id),))
                    r = my_cursor.fetchone()
                    r = "".join(str(r)[1]) if r else "Unknown"

                    my_cursor.execute("SELECT Dep FROM student WHERE Roll_No = %s", (str(id),))
                    d = my_cursor.fetchone()
                    d = "".join(d) if d else "Unknown"

                    if confidence > 77:
                        cv2.putText(img, f"Roll: {r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department: {d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                        end_time = time.time()
                        elapsed_time = end_time - start_time

                        print(f"Time taken: {elapsed_time:.10f} seconds")

       
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                except mysql.connector.Error as err:
                    print(f"Database error: {err}")
                finally:
                    if conn.is_connected():
                        my_cursor.close()
                        conn.close()

                coord = [x, y, w, h]


            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, clf)
            return img


        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Untitled.xml")

        video_cap = cv2.VideoCapture(0)
        start_time = time.time()
        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break
        
        video_cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
