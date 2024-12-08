import os

class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.name}"


class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)
        print(f"Görev eklendi: {task_name}")

    def complete_task(self, index):
        try:
            self.tasks[index].mark_as_completed()
            print(f"Görev tamamlandı: {self.tasks[index].name}")
        except IndexError:
            print("Geçersiz görev numarası.")

    def delete_task(self, index):
        try:
            task = self.tasks.pop(index)
            print(f"Görev silindi: {task.name}")
        except IndexError:
            print("Geçersiz görev numarası.")

    def show_tasks(self):
        print("\n--- Yapılacaklar Listesi ---")
        print("Tamamlanmayan Görevler:")
        for i, task in enumerate(self.tasks):
            if not task.completed:
                print(f"{i}. {task}")
        print("\nTamamlanan Görevler:")
        for i, task in enumerate(self.tasks):
            if task.completed:
                print(f"{i}. {task}")

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.name}|{task.completed}\n")
        print("Görevler kaydedildi.")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    name, completed = line.strip().split("|")
                    task = Task(name, completed == "True")
                    self.tasks.append(task)
            print("Görevler yüklendi.")
        else:
            print("Kayıtlı görev dosyası bulunamadı.")


def main():
    manager = TaskManager()

    while True:
        print("\n1. Görev Ekle")
        print("2. Görevi Tamamla")
        print("3. Görev Sil")
        print("4. Görevleri Görüntüle")
        print("5. Çıkış ve Kaydet")
        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("Görev adı: ")
            manager.add_task(name)
        elif choice == "2":
            manager.show_tasks()
            index = int(input("Tamamlanacak görev numarasını seçin: "))
            manager.complete_task(index)
        elif choice == "3":
            manager.show_tasks()
            index = int(input("Silinecek görev numarasını seçin: "))
            manager.delete_task(index)
        elif choice == "4":
            manager.show_tasks()
        elif choice == "5":
            manager.save_tasks()
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()
