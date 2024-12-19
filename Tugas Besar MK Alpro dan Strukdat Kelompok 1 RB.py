import tkinter as tk
from tkinter import messagebox
import random

# Kelas untuk Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")

    def size(self):
        return len(self.items)

# Kelas untuk Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Dequeue from empty queue")

    def size(self):
        return len(self.items)

# Variabel umum untuk menyimpan data pengguna dan pertanyaan 
users = {}
current_user = None
questions = []
history_stack = Stack()  # Stack untuk menyimpan riwayat jawaban
question_queue = Queue()  # Queue untuk menyimpan pertanyaan

# Fungsi registrasi pengguna baru 
def daftar_pengguna():
    def simpan_user():
        username = username_entry.get()
        password = password_entry.get()
        
        if username and password:
            if username in users:
                messagebox.showerror("Registrasi Error", "Username sudah terdaftar!")
            else:
                users[username] = password
                messagebox.showinfo("Registrasi", "Registrasi berhasil! Silakan login.")
                register_window.destroy()
        else:
            messagebox.showerror("Registrasi Error", "Username dan password tidak boleh kosong!")

    register_window = tk.Toplevel(root)
    register_window.title("Registrasi")
    register_window.configure(bg='#FBF6E9')

    tk.Label(register_window, text="Username:", bg='#FBF6E9', fg="#118B50").grid(row=0, column=0, pady=5)
    username_entry = tk.Entry(register_window)
    username_entry.grid(row=0, column=1, pady=5)

    tk.Label(register_window, text="Password:", bg='#FBF6E9', fg="#118B50").grid(row=1, column=0, pady=5)
    password_entry = tk.Entry(register_window, show="*")
    password_entry.grid(row=1, column=1, pady=5)

    save_button = tk.Button(register_window, text="Registrasi", command=simpan_user, bg="#5DB996", fg="#FFFFFF")
    save_button.grid(row=2, columnspan=2, pady=10)

# Fungsi login 
def login():
    global current_user

    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username] == password:
        current_user = username
        messagebox.showinfo("Login", "Login sukses!")
        menu_utama()
    else:
        messagebox.showerror("Login Error", "Username atau password salah!")

# Fungsi untuk menu utama 
def menu_utama():
    for widget in root.winfo_children():
        widget.destroy()

    greeting_label = tk.Label(root, text=f"Halo {current_user}!", font=("Arial", 14), bg='#FBF6E9', fg="#118B50")
    greeting_label.pack(pady=10)

    tambah_pertanyaan_button = tk.Button(root, text="Tambah Soal", command=tambah_pertanyaan, bg="#FBF6E9", fg="#118B50")
    tambah_pertanyaan_button.pack(pady=5)

    edit_pertanyaan_button = tk.Button(root, text="Edit Soal", command=edit_pertanyaan, bg="#FBF6E9", fg="#118B50")
    edit_pertanyaan_button.pack(pady=5)

    hapus_pertanyaan_button = tk.Button(root, text="Hapus Soal", command=hapus_pertanyaan, bg="#FBF6E9", fg="#118B50")
    hapus_pertanyaan_button.pack(pady=5)

    mulai_kuis_button = tk.Button(root, text="Mulai Kuis", command=mulai_kuis, bg="#FBF6E9", fg="#118B50")
    mulai_kuis_button.pack(pady=5)

    exit_button = tk.Button(root, text="Keluar", command=root.quit, bg="#FBF6E9", fg="#118B50")
    exit_button.pack(pady=5)

# Fungsi menambahkan pertanyaan 
def tambah_pertanyaan():
    def simpan_pertanyaan():
        question = question_entry.get()
        answer = answer_entry.get()
        options = options_entry.get().split(',')
        if question and answer and options:
            questions.append((question, answer, [opt.strip() for opt in options]))
            messagebox.showinfo("Tambah Soal", "Soal berhasil ditambahkan!")
            add_window.destroy()
        else:
            messagebox.showerror("Error", "Pertanyaan, jawaban, dan pilihan tidak boleh kosong!")

    add_window = tk.Toplevel(root)
    add_window.title("Tambah Soal")
    add_window.configure(bg='#FBF6E9')

    tk.Label(add_window, text="Pertanyaan:", bg='#FBF6E9', fg="#118B50").grid(row=0, column=0, pady=5)
    question_entry = tk.Entry(add_window, width=50)
    question_entry.grid(row=0, column=1, pady=5)

    tk.Label(add_window, text="Jawaban:", bg='#FBF6E9', fg="#118B50").grid(row=1, column=0, pady=5)
    answer_entry = tk.Entry(add_window)
    answer_entry.grid(row=1, column=1, pady=5)

    tk.Label(add_window, text="Pilihan (pisahkan dengan koma):", bg='#FBF6E9', fg="#118B50").grid(row=2, column=0, pady=5)
    options_entry = tk.Entry(add_window)
    options_entry.grid(row=2, column=1, pady=5)

    save_button = tk.Button(add_window, text="Simpan", command=simpan_pertanyaan, bg="#5DB996", fg="#FFFFFF")
    save_button.grid(row=3, columnspan=2, pady=10)

# Fungsi untuk edit pertanyaan 
def edit_pertanyaan():
    def simpan_edit():
        try:
            index = int(index_entry.get()) - 1
            if 0 <= index < len(questions):
                new_question = question_entry.get()
                new_answer = answer_entry.get()
                new_options = options_entry.get().split(',')
                if new_question and new_answer and new_options:
                    questions[index] = (new_question, new_answer, [opt.strip() for opt in new_options])
                    messagebox.showinfo("Edit Soal", "Soal berhasil diubah!")
                    edit_window.destroy()
                else:
                    messagebox.showerror("Error", "Pertanyaan, jawaban, dan pilihan tidak boleh kosong!")
            else:
                messagebox.showerror("Error", "Nomor soal tidak valid!")
        except ValueError:
            messagebox.showerror("Error", "Masukkan nomor soal yang valid!")

    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Soal")
    edit_window.configure(bg='#FBF6E9')

    tk.Label(edit_window, text="Nomor Soal:", bg='#FBF6E9', fg="#118B50").grid(row=0, column=0, pady=5)
    index_entry = tk.Entry(edit_window)
    index_entry.grid(row=0, column=1, pady=5)

    tk.Label(edit_window, text="Pertanyaan Baru:", bg='#FBF6E9', fg="#118B50").grid(row= 1, column=0, pady=5)
    question_entry = tk.Entry(edit_window, width=50)
    question_entry.grid(row=1, column=1, pady=5)

    tk.Label(edit_window, text="Jawaban Baru:", bg='#FBF6E9', fg="#118B50").grid(row=2, column=0, pady=5)
    answer_entry = tk.Entry(edit_window)
    answer_entry.grid(row=2, column=1, pady=5)

    tk.Label(edit_window, text="Pilihan Baru (pisahkan dengan koma):", bg='#FBF6E9', fg="#118B50").grid(row=3, column=0, pady=5)
    options_entry = tk.Entry(edit_window)
    options_entry.grid(row=3, column=1, pady=5)

    save_button = tk.Button(edit_window, text="Simpan", command=simpan_edit, bg="#5DB996", fg="#FFFFFF")
    save_button.grid(row=4, columnspan=2, pady=10)

# Fungsi untuk menghapus pertanyaan 
def hapus_pertanyaan():
    def menghapus():
        try:
            index = int(index_entry.get()) - 1
            if 0 <= index < len(questions):
                del questions[index]
                messagebox.showinfo("Hapus Soal", "Soal berhasil dihapus!")
                delete_window.destroy()
            else:
                messagebox.showerror("Error", "Nomor soal tidak valid!")
        except ValueError:
            messagebox.showerror("Error", "Masukkan nomor soal yang valid!")

    delete_window = tk.Toplevel(root)
    delete_window.title("Hapus Soal")
    delete_window.configure(bg='#FBF6E9')

    tk.Label(delete_window, text="Nomor Soal:", bg='#FBF6E9', fg="#118B50").grid(row=0, column=0, pady=5)
    index_entry = tk.Entry(delete_window)
    index_entry.grid(row=0, column=1, pady=5)

    delete_button = tk.Button(delete_window, text="Hapus", command=menghapus, bg="#5DB996", fg="#FFFFFF")
    delete_button.grid(row=1, columnspan=2, pady=10)

# Fungsi untuk memulai kuiz
def mulai_kuis():
    if not questions:
        messagebox.showerror("Kuis", "Belum ada soal yang tersedia!")
        return

    def pertanyaan_selanjutnya():
        nonlocal question_index
        if question_index < len(questions):
            question_label.config(text=questions[question_index][0])
            options = questions[question_index][2]
            random.shuffle(options)  # Mengacak pilihan jawaban
            for i, option in enumerate(options):
                option_buttons[i].config(text=option, command=lambda opt=option: cek_jawaban(opt))
        else:
            messagebox.showinfo("Kuis", f"Kuis selesai! Skor Anda: {score}/{len(questions)}")
            quiz_window.destroy()

    def cek_jawaban(selected_answer):
        nonlocal question_index, score
        if selected_answer == questions[question_index][1]:
            score += 1
            messagebox.showinfo("Kuis", "Jawaban Benar!")
        else:
            messagebox.showerror("Kuis", "Salah!")
        question_index += 1
        pertanyaan_selanjutnya()

    quiz_window = tk.Toplevel(root)
    quiz_window.title("Kuis")
    quiz_window.configure(bg='#FBF6E9')

    question_index = 0
    score = 0

    question_label = tk.Label(quiz_window, text="", font=("Arial", 16), bg='#FBF6E9', fg="#118B50")
    question_label.pack(pady=10)

    option_buttons = []
    for _ in range(4):  # Membuat 4 tombol untuk pilihan jawaban
        button = tk.Button(quiz_window, text="", bg="#5DB996", fg="#FFFFFF")
        button.pack(pady=5)
        option_buttons.append(button)

    pertanyaan_selanjutnya()

# Ubah bagian tampilan awal untuk login
root = tk.Tk()
root.title("Aplikasi Kuis")
root.configure(bg='#FBF6E9')  # Ubah latar belakang menjadi Cream

login_frame = tk.Frame(root, bg='#FBF6E9')  # Ubah latar belakang menjadi Cream
login_frame.pack(pady=20)

# Tambahkan judul di tengah
title_label = tk.Label(login_frame, text="LOGIN", font=("Arial", 16), bg='#FBF6E9', fg="#118B50")  # Ubah fg menjadi Dark Green
title_label.grid(row=0 , columnspan=2, pady=10)  # Menempatkan judul di atas

tk.Label(login_frame, text="Username:", bg='#FBF6E9', fg="#118B50").grid(row=1, column=0, pady=5)  # Ubah fg menjadi Dark Green
username_entry = tk.Entry(login_frame)
username_entry.grid(row=1, column=1, pady=5)

tk.Label(login_frame, text="Password:", bg='#FBF6E9', fg="#118B50").grid(row=2, column=0, pady=5)  # Ubah fg menjadi Dark Green
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=2, column=1, pady=5)

login_button = tk.Button(login_frame, text="Login", command=login, bg="#5DB996", fg="#FFFFFF")  # Ubah bg menjadi Teal
login_button.grid(row=3, column=0, pady=10)

register_button = tk.Button(login_frame, text="Sign Up", command=daftar_pengguna, bg="#5DB996", fg="#FFFFFF")  # Ubah bg menjadi Teal
register_button.grid(row=3, column=1, pady=10)

root.mainloop()