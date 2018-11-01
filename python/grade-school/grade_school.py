from functools import reduce

class School(object):

    def __init__(self):
        self.grade_dictionary = {}

    def add_student(self, name, grade):
        self.grade_dictionary[grade] = [name] if grade not in self.grade_dictionary else self.grade_dictionary[grade]+[name]

    def roster(self):
        return reduce(lambda student_list, student: student_list + sorted(student), [value for (key, value) in sorted(self.grade_dictionary.items())], [])

    def grade(self, grade_number):
        return sorted(self.grade_dictionary[grade_number]) if grade_number in self.grade_dictionary else []