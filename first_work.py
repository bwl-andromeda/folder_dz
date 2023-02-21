class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def get_awg_hw(self, grades):
        a = []
        for keys, values in self.grades.items():
            for i in values:
                a.append(i) 
        return sum(a) / len(a)
        
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_awg_hw(self.grades)}\nКурсы в процессе изучения: {", " .join(self.courses_in_progress)}\nЗавершенные курсы: {", " .join(self.finished_courses)}'
        return res

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.get_awg_hw(self.grades) < other.get_awg_hw(self.grades)


        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    
    def get_awg_grade(self, grades):
        a = []
        for keys, values in self.grades.items():
            for i in values:
                a.append(i) 
        return sum(a) / len(a)

        
    def __str__(self):
        res = f'Имя: {self.name}\nФaмилия: {self.surname}\nCрeдняя оценка за лекции: {self.get_awg_grade(self.grades)}'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Reviewer!')
            return
        return self.get_awg_grade(self.grades) < other.get_awg_grade(self.grades)
        

class Reviewer(Mentor):

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        


    
some_reviewer = Reviewer('Заместитель','Командира')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

next_reviewer = Reviewer('Возможно','Зачем-то')
next_reviewer.courses_attached += ['Python']
next_reviewer.courses_attached += ['Git']
next_reviewer.courses_attached += ['Основы ООП']


some_lecturer = Lecturer('Стив','Джобс')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Основы ООП']

next_lecturer = Lecturer('Моё','Высочество')
next_lecturer.courses_attached += ['Python']
next_lecturer.courses_attached += ['Git']



some_student = Student('Иванов','Никита','м')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']
some_student.rate_lecture(next_lecturer, 'Python' , 2)
some_student.rate_lecture(next_lecturer, 'Python' , 3)
some_student.rate_lecture(next_lecturer, 'Git' , 4)
some_student.rate_lecture(next_lecturer, 'Git' , 5)



girl_student = Student('Медведева','Юлия','ж')
girl_student.courses_in_progress += ['Python']
girl_student.courses_in_progress += ['Git']
girl_student.courses_in_progress += ['Основы ООП']
girl_student.finished_courses += ['Введение в программирование']
girl_student.rate_lecture(some_lecturer, 'Python' , 7)
girl_student.rate_lecture(some_lecturer, 'Python' , 8)
girl_student.rate_lecture(some_lecturer, 'Основы ООП' , 9)
girl_student.rate_lecture(some_lecturer, 'Основы ООП' , 6)

some_reviewer.rate_hw(some_student,'Python', 8)
some_reviewer.rate_hw(some_student,'Python', 3)
some_reviewer.rate_hw(some_student,'Python', 9)
some_reviewer.rate_hw(some_student,'Git', 4)
some_reviewer.rate_hw(some_student,'Git', 10)
some_student.get_awg_hw(some_student.grades)

next_reviewer.rate_hw(girl_student,'Git', 4)
next_reviewer.rate_hw(girl_student,'Python', 1)
next_reviewer.rate_hw(girl_student,'Python', 3)
next_reviewer.rate_hw(girl_student,'Python', 9)
next_reviewer.rate_hw(girl_student,'Git', 7)
next_reviewer.rate_hw(girl_student,'Git', 6)
next_reviewer.rate_hw(girl_student,'Основы ООП', 9)
next_reviewer.rate_hw(girl_student,'Основы ООП', 7)
girl_student.get_awg_hw(girl_student.grades)
print(some_reviewer)
print()

print(f'Средняя оценка Юлии больше чем у Никиты : {"ДА" if girl_student > some_student else "НЕТ"}')
print()

print(f'Средняя оценка Стива Джобса больше чем у Моего Высочества : {"ДА" if some_lecturer > next_lecturer else "НЕТ"}')
print()
 

print(some_lecturer)
print()

print(next_lecturer)
print()

print(some_student)
print()

print(girl_student)
print()


lst  = [some_student,girl_student]
#print(lst)
def get_awg(stud, course):
    s = []
    for i in stud:
        for key, value in i.grades.items():
            if key == course:
                for j in value:
                    s.append(j)
    return f'Средняя оценка студентов по предмету {course}: {sum(s)/len(s)}'
    
print(get_awg(lst,'Python'))

lst1  = [some_lecturer,next_lecturer]

print()
#print(lst1)
def get_awg_lec(lecturer, course):
    s = []
    for i in lecturer:
        for key, value in i.grades.items():
            if key == course:
                for j in value:
                    s.append(j)
    return f'Средняя оценка лекторов по предмету {course}: {sum(s)/len(s)}'
    
print(get_awg_lec(lst1,'Git'))