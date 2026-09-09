class Student:
    def __init__(self,name):
        self.name = name
        self.grades = []

    def add_grade(self,grade):
        self.grades.append(grade)
        print(f"grade added to {self.name}")
    def get_average(self):
        if not self.grades:
            print("Error")
        else:
            return sum(self.grades)/len(self.grades)
            

        

grades = [
    {'student name' : 'amine', 'grades' : [15,12,18,12,19]},
    {'student name' : 'mohamed', 'grades' : [15,12,18,12,19]},
    {'student name' : 'yassine', 'grades' : [15,12,18,12,19]},
    {'student name' : 'ahmed', 'grades' : [15,12,18,12,19]},

]

for grade in grades:
    for i,j in grade.items():
        print()
