import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="VRP@2004",  # 🔁 Replace with your real password
        database="AttendanceDB"
    )
