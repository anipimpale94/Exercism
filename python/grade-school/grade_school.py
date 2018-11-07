from functools import reduce
from collections import defaultdict
class School(object):

    def __init__(self):
        self.grade_dictionary = defaultdict(lambda: [])

    def add_student(self, name, grade):
        self.grade_dictionary[grade] = self.grade_dictionary[grade]+[name]

    def roster(self):
        return reduce(lambda student_list, student: student_list + sorted(student), [value for (key, value) in sorted(self.grade_dictionary.items())], [])

    def grade(self, grade_number):
        return sorted(self.grade_dictionary[grade_number])