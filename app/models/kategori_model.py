import mysql.connector
from flask import current_app

class KategoriModel:
    def __init__(self):
        self.config = current_app.config

    def connect(self):
        return mysql.connector.connect(
            host=self.config["MYSQL_HOST"],
            database=self.config["MYSQL_DATABASE"],
            user=self.config["MYSQL_USER"],
            password=self.config["MYSQL_PASSWORD"]
        )

    def insert_kategori(self, nama):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO kategori (id, nama) VALUES (%s, %s)", ('', nama))
        db.commit()
        cursor.close()
        db.close()

    def get_all_kategori(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM kategori")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def delete_kategori(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("DELETE FROM kategori WHERE id = %s", (id,))
        db.commit()
        cursor.close()
        db.close()

    def get_kategori_by_id(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM kategori WHERE id = %s", (id,))
        value = cursor.fetchone()
        cursor.close()
        db.close()
        return value

    def update_kategori(self, id, nama):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("UPDATE kategori SET nama = %s WHERE id = %s", (nama, id))
        db.commit()
        cursor.close()
        db.close()
