import mysql.connector
from flask import current_app

class PenjualModel:
    def __init__(self):
        self.config = current_app.config

    def connect(self):
        return mysql.connector.connect(
            host=self.config["MYSQL_HOST"],
            database=self.config["MYSQL_DATABASE"],
            user=self.config["MYSQL_USER"],
            password=self.config["MYSQL_PASSWORD"]
        )

    def insert_penjual(self, nama):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO penjual (id, nama) VALUES (%s, %s)", ('', nama))
        db.commit()
        cursor.close()
        db.close()

    def get_all_penjual(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM penjual")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def delete_penjual(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("DELETE FROM penjual WHERE id = %s", (id,))
        db.commit()
        cursor.close()
        db.close()

    def get_penjual_by_id(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM penjual WHERE id = %s", (id,))
        value = cursor.fetchone()
        cursor.close()
        db.close()
        return value

    def update_penjual(self, id, nama):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("UPDATE penjual SET nama = %s WHERE id = %s", (nama, id))
        db.commit()
        cursor.close()
        db.close()
