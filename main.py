import sqlite3
from datetime import datetime

class ToDoList:
    def __init__(self, db_name='todo.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                created_at TEXT NOT NULL
            );
        '''
        self.conn.execute(query)
        self.conn.commit()

    def masukkan_tugas(self, task):
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO tasks (task, created_at) VALUES (?, ?);"
        self.conn.execute(query, (task, created_at))
        self.conn.commit()

    def lihat_tugas(self):
        query = "SELECT id, task, created_at FROM tasks;"
        cursor = self.conn.execute(query)
        tasks = cursor.fetchall()
        for task in tasks:
            print(f"{task[0]}. {task[1]} (Created at: {task[2]})")

    def start(self):
        while True:
            print("\n==== Daftar Tugas Harian ====\n")
            print("1. Masukkan Tugas")
            print("2. Lihat Tugas")
            print("3. Keluar\n")

            pilihan = input("Masukkan pilihanmu (1/2/3): ")

            if pilihan == '1':
                task = input("Masukkan Tugas : ")
                self.masukkan_tugas(task)
                print("Tugas berhasil dimasukkan !")
            elif pilihan == '2':
                print("\n==== Tugas Anda ====\n")
                self.lihat_tugas()
            elif pilihan == '3':
                print("Keluar dari daftar tugas. Selamat mengerjakan!")
                break
            else:
                print("Invalid . Tolong masukkan 1, 2, or 3.")

if __name__ == "__main__":
    todo_app = ToDoList()
    todo_app.start()
