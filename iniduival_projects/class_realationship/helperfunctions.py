import csv
import os

# this is the student class, it holds all the info for one student
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    def get_letter(self):
        avg = self.get_average()
        if avg is None:
            return "N/A"
        if avg >= 90:   return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        else:           return "F"

    def display(self):
        avg = self.get_average()
        avg_str = f"{avg:.1f}" if avg is not None else "no grades yet"
        print(f"  name   : {self.name}")
        print(f"  id     : {self.student_id}")
        print(f"  grades : {self.grades or 'none yet'}")
        print(f"  avg    : {avg_str}")
        print(f"  letter : {self.get_letter()}")


# this is the gradebook class, it holds all the students
class GradeBook:
    def __init__(self):
        self.students = {}

    def add_student(self, name, student_id):
        if student_id in self.students:
            print("that id already exists")
            return
        self.students[student_id] = Student(name, student_id)
        print("ok added", name)

    def get_student(self, student_id):
        return self.students.get(student_id)

    def get_class_average(self):
        all_grades = []
        for s in self.students.values():
            all_grades.extend(s.grades)
        if not all_grades:
            return None
        return sum(all_grades) / len(all_grades)

    def save(self):
        with open("gradebook.csv", "w", newline="") as f:
            writer = csv.writer(f)
            for sid, s in self.students.items():
                writer.writerow([sid, s.name] + s.grades)
        print("saved!!")

    def load(self):
        if not os.path.exists("gradebook.csv"):
            print("no save file found")
            return
        with open("gradebook.csv", newline="") as f:
            for row in csv.reader(f):
                sid = row[0]
                if sid not in self.students:
                    s = Student(row[1], sid)
                    s.grades = [float(x) for x in row[2:] if x]
                    self.students[sid] = s
        print("loaded!!")


# this is the menu class, it handles all the user interaction
class Menu:
    def __init__(self, gradebook):
        self.gradebook = gradebook

    def get_choice(self):
        while True:
            choice = input("pick one (1-7): ")
            if choice in ("1", "2", "3", "4", "5", "6", "7"):
                return choice
            print("thats not valid!! pick a number 1 through 7")

    def add_student(self):
        name = input("whats the students name? ")
        sid = input("whats their id? ")
        if not name or not sid:
            print("name and id cant be empty!!")
            return
        self.gradebook.add_student(name, sid)

    def add_grade(self):
        if not self.gradebook.students:
            print("no students yet!! add one first")
            return
        sid = input("enter student id: ")
        student = self.gradebook.get_student(sid)
        if not student:
            print("cant find that student")
            return
        try:
            grade = float(input("enter the grade (0-100): "))
            if not 0 <= grade <= 100:
                print("grade has to be between 0 and 100!!")
                return
            student.add_grade(grade)
            print("grade added!!")
        except ValueError:
            print("thats not a number!!")

    def view_student(self):
        sid = input("enter student id: ")
        student = self.gradebook.get_student(sid)
        if not student:
            print("cant find that student")
            return
        student.display()

    def view_all(self):
        if not self.gradebook.students:
            print("no students yet")
            return
        for sid, s in self.gradebook.students.items():
            print(f"{sid} - {s.name} | grades: {s.grades} | avg: {s.get_average():.1f if s.get_average() else 'N/A'}")

    def class_summary(self):
        if not self.gradebook.students:
            print("no students yet")
            return
        print("\n--- class summary ---")
        for sid, s in self.gradebook.students.items():
            avg = s.get_average()
            avg_str = f"{avg:.1f}" if avg is not None else "no grades"
            print(f"{s.name} grades: {s.grades} avg: {avg_str}letter: {s.get_letter()}")
        class_avg = self.gradebook.get_class_average()
        if class_avg is not None:
            print(f"\nclass average: {class_avg:.1f}")
        else:
            print("\nclass average: no grades yet")

    def run(self):
        print("welcome to the class grade book!!")
        while True:
            print("\nwhat do you want to do?")
            print("1. add new student")
            print("2. add grade to student")
            print("3. view student record")
            print("4. view all students")
            print("5. class summary")
            print("6. load from csv")
            print("7. exit")

            choice = self.get_choice()

            if choice == "1":   self.add_student()
            elif choice == "2": self.add_grade()
            elif choice == "3": self.view_student()
            elif choice == "4": self.view_all()
            elif choice == "5": self.class_summary()
            elif choice == "6": self.gradebook.load()
            elif choice == "7":
                self.gradebook.save()
                print("bye THANK YOU!!")
                break