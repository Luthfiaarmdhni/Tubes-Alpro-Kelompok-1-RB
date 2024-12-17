import tkinter as tk
from tkinter import messagebox
import random

# Variabel untuk menyimpan data pengguna dan pertanyaan
data_pengguna = {}
pengguna_aktif = None
pertanyaan_list = []

# Fungsi untuk mendaftar pengguna baru
def daftar_pengguna():
    def simpan_user():
        username = username_entry.get()
        password = password_entry.get()
        
        if username and password:
            if username in data_pengguna:
                messagebox.showerror("Error Registrasi", "Username sudah terdaftar!")
            else:
                data_pengguna[username] = password
                messagebox.showinfo("Registrasi", "Registrasi berhasil! Silakan login.")
                jendela_registrasi.destroy()
        else:
            messagebox.showerror("Error Registrasi", "Username dan password tidak boleh kosong!")

    jendela_registrasi = tk.Toplevel(root)
    jendela_registrasi.title("Registrasi Pengguna Baru")
    jendela_registrasi.configure(bg='#FBF6E9')

    tk.Label(jendela_registrasi, text="Registrasi Pengguna Baru", font=("Arial", 16), bg='#FBF6E9', fg="#118B50").pack(pady=10)

    tk.Label(jendela_registrasi, text="Username:", bg='#FBF6E9', fg="#118B50").grid(row=0, column=0, pady=5)
    username_entry = tk.Entry(jendela_registrasi)
    username_entry.grid(row=0, column=1, pady=5)

    tk.Label(jendela_registrasi, text="Password:", bg='#FBF6E9', fg="#118B50").grid(row=1, column=0, pady=5)
    password_entry = tk.Entry(jendela_registrasi, show="*")
    password_entry.grid(row=1, column=1, pady=5)

    tombol_simpan = tk.Button(jendela_registrasi, text="Daftar", command=simpan_user, bg="#5DB996", fg="#FFFFFF")
    tombol_simpan.grid(row=2, columnspan=2, pady=10)

# Fungsi login
def login():
    global pengguna_aktif

    username = username_entry.get()
    password = password_entry.get()

    if username in data_pengguna and data_pengguna[username] == password:
        pengguna_aktif = username
        messagebox.showinfo("Login", "Login berhasil!")
        menu_utama()
    else:
        messagebox.showerror("Error Login", "Username atau password salah!")

# Fungsi untuk menu utama
def menu_utama():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Halo {pengguna_aktif}!", font=("Arial", 14), bg='#FBF6E9', fg="#118B50").pack(pady=10)

    tk.Button(root, text="Tambah Pertanyaan", command=tambah_pertanyaan, bg="#FBF6E9", fg="#118B50").pack(pady=5)
    tk.Button(root, text="Edit Pertanyaan", command=edit_pertanyaan, bg="#FBF6E9", fg="#118B50").pack(pady=5)
    tk.Button(root, text="Hapus Pertanyaan", command=hapus_pertanyaan, bg="#FBF6E9", fg="#118B50").pack(pady=5)
    tk.Button(root, text="Mulai Kuis", command=mulai_kuis, bg="#FBF6E9", fg="#118B50").pack(pady=5)
    tk.Button(root, text="Keluar", command=root.quit, bg="#FBF6E9", fg="#118B50").pack(pady=5)

# Fungsi menambahkan pertanyaan
def tambah_pertanyaan():
    def simpan_pertanyaan():
        pertanyaan = pertanyaan_entry.get()
        jawaban = jawaban_entry.get()
        pilihan = pilihan_entry.get().split(',')
        if pertanyaan and jawaban and pilihan:
            pertanyaan_list.append((pertanyaan, jawaban, [opt.strip() for opt in pilihan]))
            messagebox.showinfo("Tambah Pertanyaan", "Pertanyaan berhasil ditambahkan!")
            jendela_tambah.destroy()
        else:
            messagebox.showerror("Error", "Semua field harus diisi!")

    jendela_tambah = tk.Toplevel(root)
    jendela_tambah.title("Tambah Pertanyaan")
    jendela_tambah.configure(bg='#FBF6E9')

    tk.Label(jendela_tambah , text="Pertanyaan:", bg='#FBF6E9', fg="#118B50").grid(row=0, column=0, pady=5)
    pertanyaan_entry = tk.Entry(jendela_tambah, width=50)
    pertanyaan_entry.grid(row=0, column=1, pady=5)

    tk.Label(jendela_tambah, text="Jawaban:", bg='#FBF6E9', fg="#118B50").grid(row=1, column=0, pady=5)
    jawaban_entry = tk.Entry(jendela_tambah)
    jawaban_entry.grid(row=1, column=1, pady=5)

    tk.Label(jendela_tambah, text="Pilihan (pisahkan dengan koma):", bg='#FBF6E9', fg="#118B50").grid(row=2, column=0, pady=5)
    pilihan_entry = tk.Entry(jendela_tambah)
    pilihan_entry.grid(row=2, column=1, pady=5)

    tombol_simpan = tk.Button(jendela_tambah, text="Simpan", command=simpan_pertanyaan, bg="#5DB996", fg="#FFFFFF")
    tombol_simpan.grid(row=3, columnspan=2, pady=10)

# Fungsi untuk mengedit pertanyaan
def edit_pertanyaan():
    def simpan_edit():
        try:
            index = int(index_entry.get()) - 1
            if 0 <= index < len(pertanyaan_list):
                pertanyaan_baru = pertanyaan_entry.get()
                jawaban_baru = jawaban_entry.get()
                pilihan_baru = pilihan_entry.get().split(',')
                if pertanyaan_baru and jawaban_baru and pilihan_baru:
                    pertanyaan_list[index] = (pertanyaan_baru, jawaban_baru, [opt.strip() for opt in pilihan_baru])
                    messagebox.showinfo("Edit Pertanyaan", "Pertanyaan berhasil diubah!")
                    jendela_edit.destroy()
                else:
                    messagebox.showerror("Error", "Semua field harus diisi!")
            else:
                messagebox.showerror("Error", "Nomor pertanyaan tidak valid!")
        except ValueError:
            messagebox.showerror("Error", "Masukkan nomor pertanyaan yang valid!")

    jendela_edit = tk.Toplevel(root)
    jendela_edit.title("Edit Pertanyaan")
    jendela_edit.configure(bg='#FBF6E9')

    tk.Label(jendela_edit, text="Nomor Pertanyaan:", bg='#FBF6E9', fg="#118B50").grid(row=0, column=0, pady=5)
    index_entry = tk.Entry(jendela_edit)
    index_entry.grid(row=0, column=1, pady=5)

    tk.Label(jendela_edit, text="Pertanyaan Baru:", bg='#FBF6E9', fg="#118B50").grid(row=1, column=0, pady=5)
    pertanyaan_entry = tk.Entry(jendela_edit, width=50)
    pertanyaan_entry.grid(row=1, column=1, pady=5)

    tk.Label(jendela_edit, text="Jawaban Baru:", bg='#FBF6E9', fg="#118B50").grid(row=2, column=0, pady=5)
    jawaban_entry = tk.Entry(jendela_edit)
    jawaban_entry.grid(row=2, column=1, pady=5)

    tk.Label(jendela_edit, text="Pilihan Baru (pisahkan dengan koma):", bg='#FBF6E9', fg="#118B50").grid(row=3, column=0, pady=5)
    pilihan_entry = tk.Entry(jendela_edit)
    pilihan_entry.grid(row=3, column=1, pady=5)

    tombol_simpan = tk.Button(jendela_edit, text="Simpan", command=simpan_edit, bg="#5DB996", fg="#FFFFFF")
    tombol_simpan.grid(row=4, columnspan=2, pady=10)

# Fungsi untuk menghapus pertanyaan
def hapus_pertanyaan():
    def hapus():
        try:
            index = int(index_entry.get()) - 1
            if 0 <= index < len(pertanyaan_list):
                del pertanyaan_list[index]
                messagebox.showinfo("Hapus Pertanyaan", "Pertanyaan berhasil dihapus!")
                jendela_hapus.destroy()
            else:
                messagebox.showerror("Error", "Nomor pertanyaan tidak valid!")
        except ValueError:
            messagebox.showerror("Error", "Masukkan nomor pertanyaan yang valid!")

    jendela_hapus = tk.Toplevel(root)
    jendela_hapus.title("Hapus Pertanyaan")
    jendela_hapus.configure(bg='#FBF6E9')

    tk.Label(jendela_hapus, text="Nomor Pertanyaan:", bg='#FBF6E9', fg="#118B50").grid(row=0, column=0, pady=5)
    index_entry = tk.Entry(jendela_hapus)
    index_entry.grid(row=0, column=1, pady=5)

    tombol_hapus = tk.Button(jendela_hapus, text="Hapus", command=hapus, bg="#5DB996", fg="#FFFFFF")
    tombol_hapus.grid(row=1, columnspan=2, pady=10)

# Fungsi untuk memulai kuiz
def mulai_kuis():
    if not pertanyaan_list:
        messagebox.showerror("Kuis", "Belum ada pertanyaan yang tersedia!")
        return

    def pertanyaan_selanjutnya():
        nonlocal index_pertanyaan
        if index_pertanyaan < len(pertanyaan_list):
            label_pertanyaan.config(text=pertanyaan_list[index_pertanyaan][0])
            pilihan = pertanyaan_list[index_pertanyaan][2]
            random.shuffle(pilihan)  # Mengacak pilihan jawaban
            for i, pilihan_jawaban in enumerate(pilihan):
                tombol_pilihan[i].config(text=pilihan_jawaban, command=lambda opt=pilihan_jawaban: cek_jawaban(opt))
        else:
            messagebox.showinfo("Kuis", f"Kuis selesai! Skor Anda: {skor}/{len(pertanyaan_list)}")
            jendela_kuis.destroy()

    def cek_jawaban(jawaban_terpilih):
        nonlocal index_pertanyaan, skor
        if jawaban_terpilih == pertanyaan_list[index_pertanyaan][1]:
            skor += 1
            messagebox.showinfo("Kuis", "Jawaban Benar!")
        else:
            messagebox.showerror("Kuis", "Jawaban Salah!")
        index_pertanyaan += 1
        pertanyaan_selanjutnya()

    jendela_kuis = tk.Toplevel(root)
    jendela_kuis.title("Kuis")
    jendela_kuis.configure(bg='#FBF6E9')

    index_pertanyaan = 0
    skor = 0

    label_pertanyaan = tk.Label(jendela_kuis, text="", font=("Arial", 16), bg='#FBF6E9', fg="#118B50")
    label_pertanyaan.pack(pady=10)

    tombol_pilihan = []
    for _ in range(4):  # Membuat 4 tombol untuk pilihan jawaban
        tombol = tk.Button(jendela_kuis, text="", bg="#5DB996", fg="#FFFFFF")
        tombol.pack(pady=5)
        tombol_pilihan.append(tombol)

    pertanyaan_selanjutnya()

# Ubah bagian tampilan awal untuk login
root = tk.Tk()
root.title("Aplikasi Kuis")
root.configure(bg='#FBF6E9')  # Ubah latar belakang menjadi Cream

frame_login = tk.Frame(root, bg='#FBF6E9')  # Ubah latar belakang menjadi Cream
frame_login.pack(pady=20)

# Tambahkan judul di tengah
tk.Label(frame_login, text="LOGIN", font=("Arial", 16), bg='#FBF6E9', fg="#118B50").grid(row=0, columnspan=2, pady=10)  # Menempatkan judul di atas

tk.Label(frame_login, text="Username:", bg='#FBF6E9', fg="#118B50").grid(row=1, column=0, pady=5)  # Ubah fg menjadi Dark Green
username_entry = tk.Entry(frame_login)
username_entry.grid(row=1, column=1, pady=5)

tk.Label(frame_login, text="Password:", bg='#FBF6E9', fg="#118B50").grid(row=2, column=0, pady=5)  # Ubah fg menjadi Dark Green
password_entry = tk.Entry(frame_login, show="*")
password_entry.grid(row=2, column=1, pady=5)

tombol_login = tk.Button(frame_login, text="Login", command=login, bg="#5DB996", fg="#FFFFFF")  # Ubah bg menjadi Teal
tombol_login.grid(row=3, column=0, pady=10)

tombol_daftar = tk.Button(frame_login, text="Daftar", command=daftar_pengguna, bg="#5DB996", fg="#FFFFFF")  # Ubah bg menjadi Teal
tombol_daftar.grid(row=3, column=1, pady=10)

root.mainloop()