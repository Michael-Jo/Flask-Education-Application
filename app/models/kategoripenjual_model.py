import mysql.connector
from flask import current_app

class KategoripenjualModel:
    def __init__(self):
        self.config = current_app.config

    def connect(self):
        return mysql.connector.connect(
            host=self.config["MYSQL_HOST"],
            database=self.config["MYSQL_DATABASE"],
            user=self.config["MYSQL_USER"],
            password=self.config["MYSQL_PASSWORD"]
        )

    def insert_kategoripenjual(self, nama):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO kategoripenjual (id, nama) VALUES (%s, %s)", ('', nama))
        db.commit()
        cursor.close()
        db.close()

    def get_all_kategoripenjual(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM kategoripenjual")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def delete_kategoripenjual(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("DELETE FROM kategoripenjual WHERE id = %s", (id,))
        db.commit()
        cursor.close()
        db.close()

    def get_kategoripenjual_by_id(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM kategoripenjual WHERE id = %s", (id,))
        value = cursor.fetchone()
        cursor.close()
        db.close()
        return value

    def update_kategoripenjual(self, id, nama):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("UPDATE kategoripenjual SET nama = %s WHERE id = %s", (nama, id))
        db.commit()
        cursor.close()
        db.close()
