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
            print("Нельзя оцениввать лектора ниже 0 или выше 10")

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else "Нет завершенных курсов"

        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {avg_grade:.1f}\n" \
               f"Курсы в процессе изучения: {courses_in_progress}\n" \
               f"Завершенные курсы: {finished_courses}"

    def average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return sum(all_grades) / len(all_grades)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()

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

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return sum(all_grades) / len(all_grades)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()

best_student = Student("Роман", "Герасименко", "your_gender")
best_student.courses_in_progress += (["Python", "Git"])
best_student.finished_courses += ['Введение в программирование']

best2_student = Student("Иван", "Иванов", "your_gender")
best2_student.courses_in_progress += (["Python"])

cool_lecturer = Lecturer("Тимур", "Анвартдинов")
cool_lecturer.courses_attached += ["Python"]
cool_lecturer2 = Lecturer("Вася", "Пупкин")
cool_lecturer2.courses_attached += ["Python"]

cool_reviewer = Reviewer("Александр", "Бардин")
cool_reviewer.courses_attached += ["Python"]

cool_reviewer.rate_hw(best_student, "Python", 10)
cool_reviewer.rate_hw(best_student, "Python", 5)
cool_reviewer.rate_hw(best_student, "Python", 3)

cool_reviewer.rate_hw(best_student, "Git", 5)
cool_reviewer.rate_hw(best_student, "Git", 3)
cool_reviewer.rate_hw(best_student, "Git", 1)

cool_reviewer.rate_hw(best2_student, "Python", 1)
cool_reviewer.rate_hw(best2_student, "Python", 5)
cool_reviewer.rate_hw(best2_student, "Python", 3)

best_student.rate_lecturer(cool_lecturer, "Python", 10)
best_student.rate_lecturer(cool_lecturer, "Python", 2)
best_student.rate_lecturer(cool_lecturer, "Python", 7)

# print(best_student.grades)
# print(cool_lecturer.grades)
print("Проверяющий:")
print(cool_reviewer)
print("\nЛектор")
print(cool_lecturer)
print("\nЛектор 2")
print(cool_lecturer2)
print("\nСтудент")
print(best_student)
print("\nСтудент 2")
print(best2_student)
print("\nСравнение студентов:")
print(f"{best_student.name} лучше {best2_student.name}: {best_student > best2_student}")
print(f"{best_student.name} равен {best2_student.name}: {best_student == best2_student}")
print("\nСравнение лекторов:")
print(f"{cool_lecturer.name} лучше {cool_lecturer2.name}: {cool_lecturer > cool_lecturer2}")
print(f"{cool_lecturer.name} равен {cool_lecturer2.name}: {cool_lecturer == cool_lecturer2}")

