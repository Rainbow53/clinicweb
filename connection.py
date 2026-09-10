import pymysql
from pathlib import Path
from datetime import datetime
from tkinter import messagebox

def get_connection():
    try:
        return pymysql.connect(
            host="b5fe4m6kyphoshfoxdes-mysql.services.clever-cloud.com",
            user="ung9vbyccp62wjkl",
            database="b5fe4m6kyphoshfoxdes",
            password="ZKva2LNGVrayFXHJCXZ6",
            port=3306,
            ssl={"ssl": True},
            cursorclass=pymysql.cursors.DictCursor
        )

    except pymysql.MySQLError as err:
        #raise Exception(f"Database connection failed: {err}"
        messagebox.showinfo("Database connection failed..                    ") 

