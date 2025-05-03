class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached
                and 1 <= grade <= 10):

            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            print("нельзя оцениввать лектора ниже 0 или выше 10")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


best_student = Student("Roman", "Gerasimenko", "your_gender")
best_student.courses_in_progress += ["Python"]

cool_lecturer = Lecturer("Timur", "Anvartdinov")
cool_lecturer.courses_attached += ["Python"]

cool_reviewer = Reviewer("Some", "Buddy")
cool_reviewer.courses_attached += ["Python"]

cool_reviewer.rate_hw(best_student, "Python", 15)
cool_reviewer.rate_hw(best_student, "Python", 5)
cool_reviewer.rate_hw(best_student, "Python", 3)

best_student.rate_lecturer(cool_lecturer, "Python", 12)
best_student.rate_lecturer(cool_lecturer, "Python", 2)
best_student.rate_lecturer(cool_lecturer, "Python", 7)

# print(best_student.grades)
# print(cool_lecturer.grades)
print(f"Оценки студента {best_student.name} {best_student.surname} по курсу Python: {best_student.grades.get('Python', [])}")
print(f"Оценки лектора {cool_lecturer.name} {cool_lecturer.surname} по курсу Python: {cool_lecturer.grades.get('Python', [])}")