
import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController


class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()

        self.view.btn_login.configure(command=self.login)

    def login(self):
        username = self.view.entry_username.get()
        password = self.view.entry_password.get()

        if not username or not password:
            messagebox.showwarning(
                "Peringatan",
                "Username dan password harus diisi!"
            )
            return

        user = self.model.autentikasi(username, password)

        if user:
            messagebox.showinfo(
                "Login Berhasil",
                f"Selamat datang, {user['username']}!"
            )

            role = user['role'].lower()
            self.view.destroy()

            app = BukuController(user_role=role)
            app.run()

        else:
            messagebox.showerror(
                "Login Gagal",
                "Username atau password salah!"
            )

    def run(self):
        self.view.mainloop()
