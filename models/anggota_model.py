
import mysql.connector


class AnggotaModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="perpustakaan"
        )

    def get_all_anggota(self):
        cursor = self.conn.cursor(dictionary=True)

        try:
            cursor.execute(
                "SELECT id_anggota, nama, alamat FROM anggota"
            )
            return cursor.fetchall()
        finally:
            cursor.close()

    def create_anggota(self, nama, alamat):
        cursor = self.conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO anggota (nama, alamat) VALUES (%s, %s)",
                (nama, alamat)
            )
            self.conn.commit()
            return True
        except mysql.connector.Error as error:
            print("Gagal menambahkan anggota:", error)
            self.conn.rollback()
            return False
        finally:
            cursor.close()

    def update_anggota(self, id_anggota, nama, alamat):
        cursor = self.conn.cursor()

        try:
            cursor.execute(
                """
                UPDATE anggota
                SET nama = %s, alamat = %s
                WHERE id_anggota = %s
                """,
                (nama, alamat, id_anggota)
            )

            self.conn.commit()
            return cursor.rowcount > 0

        except mysql.connector.Error as error:
            print("Gagal memperbarui anggota:", error)
            self.conn.rollback()
            return False
        finally:
            cursor.close()

    def delete_anggota(self, id_anggota):
        cursor = self.conn.cursor()

        try:
            cursor.execute(
                "DELETE FROM anggota WHERE id_anggota = %s",
                (id_anggota,)
            )

            berhasil = cursor.rowcount > 0
            self.conn.commit()
            return berhasil

        except mysql.connector.Error as error:
            print("Gagal menghapus anggota:", error)
            self.conn.rollback()
            return False
        finally:
            cursor.close()

    def close(self):
        self.conn.close()