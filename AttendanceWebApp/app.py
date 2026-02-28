from flask import Flask, render_template, request
from db_config import get_connection

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Mark Attendance route
@app.route('/mark-attendance', methods=['GET', 'POST'])
def mark_attendance():
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        subject_id = request.form['subject']
        attendance_date = request.form['date']
        present_ids = request.form.getlist('present')

        cursor.execute("SELECT student_id FROM Students")
        student_ids = cursor.fetchall()

        for (sid,) in student_ids:
            status = 'Present' if str(sid) in present_ids else 'Absent'
            cursor.execute("""
                INSERT INTO Attendance (student_id, subject_id, attendance_date, status)
                VALUES (%s, %s, %s, %s)
            """, (sid, subject_id, attendance_date, status))

        conn.commit()
        conn.close()
        return "✅ Attendance Marked Successfully!"

    cursor.execute("SELECT subject_id, name FROM Subjects")
    subjects = cursor.fetchall()

    cursor.execute("SELECT student_id, name FROM Students ORDER BY student_id")
    students = cursor.fetchall()

    conn.close()
    return render_template('mark_attendance.html', subjects=subjects, students=students)

# View Attendance route
@app.route('/view-attendance', methods=['GET', 'POST'])
def view_attendance():
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        date = request.form['date']
        subject_id = request.form['subject']

        cursor.execute("SELECT name FROM Subjects WHERE subject_id = %s", (subject_id,))
        subject_name = cursor.fetchone()[0]

        cursor.execute("""
            SELECT s.student_id, s.name, a.status
            FROM Attendance a
            JOIN Students s ON a.student_id = s.student_id
            WHERE a.attendance_date = %s AND a.subject_id = %s
            ORDER BY s.student_id
        """, (date, subject_id))
        records = cursor.fetchall()

        conn.close()
        return render_template('view_attendance_result.html', records=records, date=date, subject=subject_name)

    cursor.execute("SELECT subject_id, name FROM Subjects")
    subjects = cursor.fetchall()

    conn.close()
    return render_template('view_attendance.html', subjects=subjects)

# Attendance Summary route
@app.route('/attendance-summary', methods=['GET', 'POST'])
def attendance_summary():
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        date = request.form['date']
        subject_id = request.form['subject']

        cursor.execute("SELECT name FROM Subjects WHERE subject_id = %s", (subject_id,))
        subject_name = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*) FROM Attendance
            WHERE attendance_date = %s AND subject_id = %s
        """, (date, subject_id))
        total = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*) FROM Attendance
            WHERE attendance_date = %s AND subject_id = %s AND status = 'Present'
        """, (date, subject_id))
        present = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*) FROM Attendance
            WHERE attendance_date = %s AND subject_id = %s AND status = 'Absent'
        """, (date, subject_id))
        absent = cursor.fetchone()[0]

        conn.close()
        return render_template('attendance_summary_result.html', date=date, subject=subject_name, total=total, present=present, absent=absent)

    cursor.execute("SELECT subject_id, name FROM Subjects")
    subjects = cursor.fetchall()
    conn.close()
    return render_template('attendance_summary.html', subjects=subjects)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
