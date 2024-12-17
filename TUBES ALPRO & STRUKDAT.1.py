print("TUGAS BESAR")
'''
Buatlah sebuah GUI untuk KUIS, item yang harus ada:

1. Sistem login
2. Input/tambah, simpan, edit & delete soal
3. Memunculkan skor diakhir

Item yang dinilai:

1. Penggunaan tipe data
2. Penggunaan Fungsi
3. Error Handling
4. Ketepatan penggunaan fungsi recursive (boleh menggunakan looping)

Yang dikumpulkan:

Flowchart, link kode program (menggunakan github), ppt & rekaman video.'''
import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class Question:
    def __init__(self, question_text, answer_text):
        self.question_text = question_text
        self.answer_text = answer_text

    def to_dict(self):
        return {
            "question": self.question_text,
            "answer": self.answer_text
        }

    @staticmethod
    def from_dict(data):
        return Question(data["question"], data["answer"])

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KUIS")
        self.questions = []
        self.load_questions()
        
        self.login_screen()

    def login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Login").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Button(self.root, text="Login", command=self.main_menu).pack()

    def main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Main Menu").pack()
        tk.Button(self.root, text="Add Question", command=self.add_question).pack()
        tk.Button(self.root, text="Edit Question", command=self.edit_question).pack()
        tk.Button(self.root, text="Delete Question", command=self.delete_question).pack()
        tk.Button(self.root, text="Start Quiz", command=self.start_quiz).pack()
        tk.Button(self.root, text="Exit", command=self.exit_app).pack()

    def add_question(self):
        question_text = simpledialog.askstring("Input", "Enter the question:")
        answer_text = simpledialog.askstring("Input", "Enter the answer:")
        if question_text and answer_text:
            question = Question(question_text, answer_text)
            self.questions.append(question)
            self.save_questions()
            messagebox.showinfo("Info", "Question added successfully!")

    def edit_question(self):
        if not self.questions:
            messagebox.showwarning("Warning", "No questions available to edit.")
            return

        question_list = "\n".join([f"{i+1}. {q.question_text}" for i, q in enumerate(self.questions)])
        index = simpledialog.askinteger("Edit Question", f"Select question number to edit:\n{question_list}")
        if index and 0 < index <= len(self.questions):
            new_question_text = simpledialog.askstring("Input", "Enter the new question:")
            new_answer_text = simpledialog.askstring("Input", "Enter the new answer:")
            if new_question_text and new_answer_text:
                self.questions[index-1] = Question(new_question_text, new_answer_text)
                self.save_questions()
                messagebox.showinfo("Info", "Question edited successfully!")

    def delete_question(self):
        if not self.questions:
            messagebox.showwarning("Warning", "No questions available to delete.")
            return

        question_list = "\n".join([f"{i+1}. {q.question_text}" for i, q in enumerate(self.questions)])
        index = simpledialog.askinteger("Delete Question", f"Select question number to delete:\n{question_list}")
        if index and 0 < index <= len(self.questions):
            del self.questions[index-1]
            self.save_questions()
            messagebox.showinfo("Info", "Question deleted successfully!")

    def start_quiz(self):
        if not self.questions:
            messagebox.showwarning("Warning", "No questions available to start the quiz.")
            return

        score = 0
        for q in self.questions:
            answer = simpledialog.askstring("Quiz", q.question_text)
            if answer and answer.strip().lower() == q.answer_text.strip().lower():
                score += 1
        messagebox.showinfo("Score", f"Your score: {score}/{len(self.questions)}")

    def load_questions(self):
        try:
            with open("questions.json", "r") as f:
                data = json.load(f)
                self.questions = [Question.from_dict(q) for q in data]
        except FileNotFoundError:
            # Jika file tidak ada, kita bisa menambahkan beberapa pertanyaan default
            self.questions = [
                Question("Apa ibu kota Indonesia?", "Jakarta"),
                Question("Siapa presiden pertama Indonesia?", "Soekarno"),
                Question("Apa nama gunung tertinggi di dunia?", "Everest"),
                Question("Siapa penemu lampu pijar?", "Thomas Edison"),
                Question("Apa nama planet terdekat dengan matahari?", "Merkurius")
            ]
            self.save_questions()  # Simpan pertanyaan default ke file

    def save_questions(self):
        with open("questions.json", "w") as f:
            json.dump([q.to_dict() for q in self.questions], f)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def exit_app(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

'''PENJELASAN KODE
1. Import Library
tkinter: Library untuk membuat antarmuka grafis (GUI) di Python.
messagebox: Modul dari tkinter untuk menampilkan kotak pesan.
simpledialog: Modul dari tkinter untuk meminta input sederhana dari pengguna.
json: Library untuk bekerja dengan data dalam format JSON.

2. Kelas Question
__init__: Konstruktor yang menginisialisasi objek Question dengan teks pertanyaan dan jawaban.
to_dict: Mengonversi objek Question menjadi dictionary untuk disimpan dalam format JSON.
from_dict: Metode statis yang mengonversi dictionary kembali menjadi objek Question.

3. Kelas QuizApp
__init__: Konstruktor untuk kelas QuizApp, yang menginisialisasi jendela utama, memuat pertanyaan, dan menampilkan layar login.

4. Metode login_screen : Menampilkan layar login dengan label, entry untuk nama pengguna, dan tombol untuk masuk ke menu utama.

5. Metode main_menu : Menampilkan menu utama dengan opsi untuk menambah, mengedit, menghapus pertanyaan, memulai kuis, dan keluar dari aplikasi.

6. Metode add_question: Meminta pengguna untuk memasukkan pertanyaan dan jawaban, kemudian menambahkannya ke daftar pertanyaan dan menyimpannya ke file JSON.

7. Metode edit_question: Memungkinkan pengguna untuk mengedit pertanyaan yang ada. Jika tidak ada pertanyaan, akan muncul peringatan. Jika ada, pengguna dapat memilih pertanyaan untuk diedit.

8. Metode delete_question: Memungkinkan pengguna untuk menghapus pertanyaan yang ada. Jika tidak ada pertanyaan, akan muncul peringatan. Jika ada, pengguna dapat memilih pertanyaan untuk dihapus.

9. Metode start_quiz: Memulai kuis dengan menampilkan setiap pertanyaan kepada pengguna. Pengguna dapat memberikan jawaban, dan skor dihitung berdasarkan jawaban yang benar.

10. Metode load_questions: Memuat pertanyaan dari file JSON. Jika file tidak ditemukan, beberapa pertanyaan default ditambahkan dan disimpan ke file.

11. Metode save_questions: Menyimpan daftar pertanyaan ke file JSON.

12. Metode clear_screen: Menghapus semua widget dari jendela saat ini untuk membersihkan tampilan sebelum menampilkan layar baru.

13. Metode exit_app: Menampilkan konfirmasi sebelum keluar dari aplikasi.

14. Menjalankan Aplikasi : Memulai aplikasi dengan membuat instance dari QuizApp dan menjalankan loop utama tkinter.

Aplikasi ini adalah kuis sederhana yang memungkinkan pengguna untuk menambah, mengedit, menghapus pertanyaan, dan menjalankan kuis dengan pertanyaan yang telah disimpan.
'''