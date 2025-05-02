# FACE-RECOGNITION-SYSTEM

Face Recognition Student Management System
This project is a full-featured Face Recognition-Based Student Management System built using Python, OpenCV, MySQL, and Tkinter. It allows the addition of student details, captures and trains facial data, and performs real-time face recognition for student identification.

Features
🔐 Face Recognition using OpenCV (LBPH)

🧑‍🎓 Student Management Interface

📸 Capture & Train Student Face Images

💾 MySQL Database Integration

🖼️ Graphical User Interface using Tkinter

📊 Accuracy and Evaluation Metrics (Precision, Recall, MSE)

Requirements
Python 3.x

OpenCV (opencv-contrib-python)

Tkinter (usually pre-installed)

PIL (Pillow)

NumPy

Matplotlib

MySQL Server (XAMPP or standalone)

MySQL Connector for Python

Install dependencies using:

bash
Copy
Edit
pip install opencv-contrib-python pillow numpy matplotlib mysql-connector-python
Directory Structure
graphql
Copy
Edit
├── main.py             # Main dashboard interface
├── Student.py          # Handles student registration and database operations
├── Train.py            # Trains the model on captured face data
├── newface.py          # Performs real-time face recognition and matches with database
├── data/               # Folder containing captured face images
├── Untitled.xml        # Trained LBPH face recognizer model
Setup Instructions
Database Setup
Create a MySQL database named face_recognizer and a table named student with appropriate fields matching those used in the scripts (Roll_No, Name, Dep, etc.).

Run the Application
Execute the main.py file:

bash
Copy
Edit
python main.py
Modules Overview:

Student Module: Add/update/delete student records.

Train Module: Train the LBPH classifier with face images.

Face Recognition: Recognize faces using webcam and display details.

Screenshots
(Insert GUI screenshots here showing student form, training, recognition output, etc.)

Credits
Developed by: Kaunain and Team
Part of: NTCC Project – 2nd Year

License
This project is for academic use only. Please contact the author for commercial or redistribution rights.
