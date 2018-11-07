from functools import reduce
from collections import defaultdict
class School(object):

    def __init__(self):
        self.grades = defaultdict(list)

    def add_student(self, name, grade):
        self.grades[grade].append(name)

    def roster(self):
        return reduce(lambda students, student: students + sorted(student), [value for (key, value) in sorted(self.grades.items())], [])

    def grade(self, grade_number):
        return sorted(self.grades[grade_number])