class Garden(object):
    students = {}
    plant_name = {
        'V': 'Violets',
        'R': 'Radishes',
        'C': 'Clover',
        'G': 'Grass'
    }

    def __init__(self, diagram, students=[]):
        self.rows = diagram.split('\n')
        if len(students) == 0:
            students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
        for index, student in enumerate(students):
            self.students[student] =  index

    def plants(self, student_name):
        i = self.students[student_name]
        items = []
        items.append(self.plant_name[self.rows[0][2*i]])
        items.append(self.plant_name[self.rows[0][2*i+1]])
        items.append(self.plant_name[self.rows[1][2*i]])
        items.append(self.plant_name[self.rows[1][2*i+1]])
        return items
