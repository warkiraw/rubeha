from dataclasses import dataclass
from typing import List
import unittest


@dataclass
class Task:
    name: str
    opis: str
    date: int
    deadline: int
    vawnost:str

class TaskManager:
    def __init__(self):
        self.bloknot = []
    def add_task(self):
        name = input("Придумайте название задачи: ")
        opis = input("Введите описание задачи: ")
        date = input("Дата задачи: ")
        deadline = input("Дедлайн: ")
        vawnost = input("Важна ли задача?:(да или нет)")
        self.task = Task(name=name,opis=opis,date=date,deadline=deadline,vawnost=vawnost)
        self.bloknot.append(self.task)
        with open("rubeha.txt",'a') as f:
            f.write(f"Название задачи:\n{self.task.name}\nОписание:\n{self.task.opis}\nДата задачи:\n{self.task.date}\nДедлайн:\n{self.task.deadline}\nВажность:\n{self.task.vawnost}")
            print("Задача добавлена")
    def del_task(self):
        dele = input("Введите название задачи,которую хотите удалить: ")
        if dele == self.task.name:
            with open("rubeha.txt",'w') as f:
                f.write("")
                print("Задача удалена")
        else:
            print("Задача не найдена")
    def change_task(self):
        z = input("Введите какой пункт задачи,которую хотите изменить:(название,описание,дата,дедлайн,важность) ")
        if z=="название" or z=="Название":
            self.task.name = input("Введите новое название задачи: ")
            with open("rubeha.txt",'w') as f:
                f.write(f"Название задачи:\n{self.task.name}\nОписание:\n{self.task.opis}\nДата задачи:\n{self.task.date}\nДедлайн:\n{self.task.deadline}\nВажность:\n{self.task.vawnost}")
                print("Задача изменена")
        if z=="описание" or z=="Описание":
            self.task.opis = input("Введите новое описание задачи: ")
            with open("rubeha.txt",'w') as f:
                f.write(f"Название задачи:\n{self.task.name}\nОписание:\n{self.task.opis}\nДата задачи:\n{self.task.date}\nДедлайн:\n{self.task.deadline}\nВажность:\n{self.task.vawnost}")
                print("Описание изменено")
        if z=="дата" or z=="Дата":
            self.task.date = input("Введите новую дату задачи: ")
            with open("rubeha.txt",'w') as f:
                f.write(f"Название задачи:\n{self.task.name}\nОписание:\n{self.task.opis}\nДата задачи:\n{self.task.date}\nДедлайн:\n{self.task.deadline}\nВажность:\n{self.task.vawnost}")
                print("Дата изменена")
        if z=="дедлайн" or z=="Дедлайн":
            self.task.deadline = input("Введите новый дедлайн задачи: ")
            with open("rubeha.txt",'w') as f:
                f.write(f"Название задачи:\n{self.task.name}\nОписание:\n{self.task.opis}\nДата задачи:\n{self.task.date}\nДедлайн:\n{self.task.deadline}\nВажность:\n{self.task.vawnost}")
                print("Дедлайн изменен")
        if z=="важность" or z=="Важность":
            self.task.vawnost = input("Введите новую важность задачи: ")
            with open("rubeha.txt",'w') as f:
                f.write(f"Название задачи:\n{self.task.name}\nОписание:\n{self.task.opis}\nДата задачи:\n{self.task.date}\nДедлайн:\n{self.task.deadline}\nВажность:\n{self.task.vawnost}")
                print("Важность изменена")
        else:
            print("Задача не найдена")
    def time_task(self):
        x = int(self.task.deadline) - int(self.task.date)
        print(f"Время задачи: {x} минут")
    def show_task(self):
        for i in self.bloknot:
            print("--------------------------------------------------------------------------------------------")
            print(f"Название задачи:\n{i.name}\nОписание:\n{i.opis}\nДата задачи:\n{i.date}\nДедлайн:\n{i.deadline}\nВажность:\n{i.vawnost}")
    def vawnie_task(self):
        for i in self.bloknot:
            x = int(i.deadline) - int(i.date)
            print(x)

        
                
    
            

a = TaskManager()
a.add_task()
a.add_task()
a.add_task()
a.del_task()
a.change_task()
a.time_task()
a.vawnie_task()

