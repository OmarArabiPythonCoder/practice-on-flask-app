class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade #0 - 100
        # this takes the age name and grade of each student

    def get_grade(self):
        return self.grade

class course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students: # if the students are less than self.max_students then return true else return false
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

st1 = student("Omar", 13, 97)
st2 = student("Ahmed", 12, 76)
st3 = student("AbdAllah", 12, 89)

cs = course("science", 2)
cs.add_student(st1)
cs.add_student(st2) # those two will return true because they are less than self.max_students 
print(cs.add_student(st3)) # this one won't because now self.students it has more 
print(cs.students[0].name) # you can get the index of an element if it is inside a list in this case self.students
print(cs.get_average_grade())