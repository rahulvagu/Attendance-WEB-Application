# 🧑‍🏫 Online Attendance Management System

A web-based Attendance Management System developed using **Flask** and **MySQL** to efficiently manage and track student attendance.  
The application supports bulk student data handling and provides a simple and user-friendly interface for marking and viewing attendance.

🔗 **GitHub Repository:** https://github.com/rahulvagu/Attendance-WEB-Application

---

## 🚀 Features

- Add and manage 50+ students
- Mark attendance (Present / Absent)
- View attendance by date
- Store attendance records in MySQL
- Update and delete student details
- Flash messages for user actions
- Responsive web interface

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Flask (Python)
- **Database:** MySQL
- **Templating Engine:** Jinja2

---

## 🗄️ Database Design

### Tables Used

#### 1️⃣ students
- student_id (Primary Key)
- name
- roll_number
- department

#### 2️⃣ attendance
- attendance_id (Primary Key)
- student_id (Foreign Key)
- date
- status (Present/Absent)

The relational database structure ensures accurate attendance tracking and fast data retrieval.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/rahulvagu/Attendance-WEB-Application.git
cd Attendance-WEB-Application
