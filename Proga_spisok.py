import tkinter as tk
import os

# Функция для загрузки задач из файла
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listBox.insert(tk.END, task.strip())

# Функция для сохранения задач в файл
def save_tasks():
    tasks = task_listBox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()  # Сохранение задач при добавлении

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)
        save_tasks()  # Сохранение задач после удаления

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="slate blue")

# Функция для закрытия программы
def on_closing():
    save_tasks()  # Сохраняем задачи перед закрытием
    root.destroy()  # Закрываем окно

# Создаем главное окно
root = tk.Tk()
root.title("Task list")
root.configure(background="cyan")

# Создаем элементы интерфейса
text1 = tk.Label(root, text="Введите вашу задачу:", bg="cyan")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="cyan")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)

text2 = tk.Label(root, text="Список задач:", bg="cyan")
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=50, bg="cyan")
task_listBox.pack(pady=10)

# Загружаем задачи при запуске программы
load_tasks()

# Обработчик закрытия окна
root.protocol("WM_DELETE_WINDOW", on_closing)

# Запускаем главный цикл обработки событий
root.mainloop()
