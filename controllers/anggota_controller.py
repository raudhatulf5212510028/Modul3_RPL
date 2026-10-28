import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        self.id_terpilih = None

        # Binding tombol
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )
        self.view.btn_update.configure(
            command=self.perbarui_data
        )
        self.view.btn_delete.configure(
            command=self.hapus_data
        )

        # Binding pilihan baris tabel
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_data
        )

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()

        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    anggota["id_anggota"],
                    anggota["nama"],
                    anggota["alamat"]
                )
            )

    def pilih_data(self, event=None):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            return

        data = self.view.tabel.item(pilihan[0], "values")

        self.id_terpilih = int(data[0])

        self.view.entry_nama.delete(0, "end")
        self.view.entry_nama.insert(0, data[1])

        self.view.entry_alamat.delete(0, "end")
        self.view.entry_alamat.insert(0, data[2])

    def simpan_data(self):
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo(
                "Sukses", "Data anggota berhasil disimpan!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error", "Data anggota gagal disimpan."
            )

    def perbarui_data(self):
        if self.id_terpilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data anggota dari tabel terlebih dahulu!"
            )
            return

        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        berhasil = self.model.update_anggota(
            self.id_terpilih, nama, alamat
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses", "Data anggota berhasil diperbarui!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data gagal diperbarui atau tidak ada perubahan."
            )

    def hapus_data(self):
        if self.id_terpilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data anggota yang ingin dihapus!"
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Yakin ingin menghapus data anggota ini?"
        )

        if not konfirmasi:
            return

        berhasil = self.model.delete_anggota(
            self.id_terpilih
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses", "Data anggota berhasil dihapus!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal dihapus."
            )

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, "end")
        self.view.entry_alamat.delete(0, "end")
        self.id_terpilih = None

        for item in self.view.tabel.selection():
            self.view.tabel.selection_remove(item)

    def run(self):
        try:
            self.view.mainloop()
        finally:
            self.model.close()


if __name__ == "__main__":
    app = AnggotaController()
    app.run()