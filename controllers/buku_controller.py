
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView(role=self.user_role)

        # Menampilkan role pada judul jendela
        self.view.title(
            f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}"
        )

        # Binding tombol aksi
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_delete.configure(command=self.hapus_data)
        self.view.btn_logout.configure(command=self.logout)

        # Otorisasi: anggota tidak boleh update dan delete
        if self.user_role == "anggota":
            self.view.btn_update.configure(state="disabled")
            self.view.btn_delete.configure(state="disabled")

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def simpan_data(self):
        # Admin dan anggota boleh menambah buku
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!"
            )

            self.view.entry_judul.delete(0, "end")
            self.view.entry_penulis.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")

            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Gagal menyimpan data."
            )

    def update_data(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Hanya admin yang dapat memperbarui data!"
            )
            return

        messagebox.showinfo(
            "Informasi",
            "Hubungkan fungsi ini dengan metode update pada controller sebelumnya."
        )

    def hapus_data(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Hanya admin yang dapat menghapus data!"
            )
            return

        messagebox.showinfo(
            "Informasi",
            "Hubungkan fungsi ini dengan metode hapus pada controller sebelumnya."
        )

    def logout(self):
        if messagebox.askyesno(
            "Konfirmasi Logout",
            "Apakah Anda yakin ingin keluar dari aplikasi?"
        ):
            self.view.destroy()

            from controllers.auth_controller import AuthController
            auth_app = AuthController()
            auth_app.run()

    def run(self):
        self.view.mainloop()
