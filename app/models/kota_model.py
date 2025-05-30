import mysql.connector
from flask import current_app

class KotaModel:
    def __init__(self):
        self.config = current_app.config

    def connect(self):
        return mysql.connector.connect(
            host=self.config["MYSQL_HOST"],
            database=self.config["MYSQL_DATABASE"],
            user=self.config["MYSQL_USER"],
            password=self.config["MYSQL_PASSWORD"]
        )

    def insert_kota(self, nama):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO kota (id, nama) VALUES (%s, %s)", ('', nama))
        db.commit()
        cursor.close()
        db.close()

    def get_all_kota(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM kota")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def delete_kota(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("DELETE FROM kota WHERE id = %s", (id,))
        db.commit()
        cursor.close()
        db.close()

    def get_kota_by_id(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM kota WHERE id = %s", (id,))
        value = cursor.fetchone()
        cursor.close()
        db.close()
        return value

    def update_kota(self, id, nama):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("UPDATE kota SET nama = %s WHERE id = %s", (nama, id))
        db.commit()
        cursor.close()
        db.close()
