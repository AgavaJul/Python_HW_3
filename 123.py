class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_rate(self): 
        for v in self.grades.values():
            if float(len(v)) != 0:
                return str(float(sum(v)) / float(len(v)))
            else: 
                return "Деление на ноль запрещено!"

    def __str__(self):
        return 'Имя: '+self.name+'\nФамилия: '+self.surname+'\nСредняя оценка за домашние задания: '+self.avg_rate()+'\nКурсы в процессе изучения: '+(", " .join(self.courses_in_progress))+'\nЗавершенные курсы: '+(", ". join(self.finished_courses))+''

    def __lt__(self, other):
            if not isinstance(other, Student):
                print('Такого студента нет!')
                return
            return self.avg_rate() < other.avg_rate()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

student_1 = Student('Tina', 'Gross', 'w')
student_1.courses_in_progress += ['Python']

student_2 = Student('Nik', 'Name', 'm')
student_2.courses_in_progress += ['Git']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_rate_l(self):
            for v in self.grades.values():
                if float(len(v)) != 0:
                    return str(float(sum(v)) / float(len(v)))
                else: 
                    return "Деление на ноль запрещено!"

    def __str__(self):
        return 'Имя: '+self.name+'\nФамилия: '+self.surname+'\nСредняя оценка за лекции: '+str(self.avg_rate_l())+''
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого лектора нет!')
            return
        return self.avg_rate_l() < other.avg_rate_l()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Имя: '+self.name+'\nФамилия: '+self.surname+''

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

mentor_1 = Reviewer('Jack', 'J')
mentor_1.courses_attached += ['Python']

mentor_1.rate_hw(student_1, 'Python', 3)
mentor_1.rate_hw(student_1, 'Python', 10)
mentor_1.rate_hw(student_1, 'Python', 8)

mentor_2 = Reviewer('Penelopa', 'Kik')
mentor_2.courses_attached += ['Git']

mentor_2.rate_hw(student_2, 'Git', 6)
mentor_2.rate_hw(student_2, 'Git', 10)
mentor_2.rate_hw(student_2, 'Git', 7)

cool_lecturer = Lecturer('Some_1', 'Buddy_1')
cool_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

lecturer_1 = Lecturer('Pol', 'Dol')
lecturer_1.courses_attached += ['Git']

best_student.rate_lecturer(lecturer_1, 'Git', 5)
best_student.rate_lecturer(lecturer_1, 'Git', 10)
best_student.rate_lecturer(lecturer_1, 'Git', 10)

lecturer_2 = Lecturer('Bob', 'Bab')
lecturer_2.courses_attached += ['Git']

student_2.rate_lecturer(lecturer_2, 'Git', 5)
student_2.rate_lecturer(lecturer_2, 'Git', 4)
student_2.rate_lecturer(lecturer_2, 'Git', 8)

print(best_student)
print(lecturer_1)
print(cool_lecturer)
print(cool_lecturer < lecturer_1)
print(student_2 < student_1)


student_list = [best_student, student_1, student_2]

def avg_stud_rate(student_list, course):
    for i in range(len(student_list)):
        if course in student_list[i].grades.keys():
            print(f'Средний балл за домашние задания {student_list[i].name} {student_list[i].surname} {round(float(student_list[i].avg_rate()), 2)}')


avg_stud_rate(student_list, 'Python')

lecturer_list = [cool_lecturer, lecturer_1, lecturer_2]

def avg_lect_rate(lecturer_list, course):
    for i in range(len(lecturer_list)):
        if course in lecturer_list[i].grades.keys():
            print(f'Средний балл за лекции {lecturer_list[i].name} {lecturer_list[i].surname} {round(float(lecturer_list[i].avg_rate_l()), 2)}')

avg_lect_rate(lecturer_list, 'Python')