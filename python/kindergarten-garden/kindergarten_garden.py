class Garden(object):
    students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
    students_dictionary = {}
    plant_name = {
        'V': 'Violets',
        'R': 'Radishes',
        'C': 'Clover',
        'G': 'Grass'
    }

    def __init__(self, diagram, students=None):
        self.rows = diagram.split('\n')
        if students != None:
            students.sort()
            self.students = students
        for index, student in enumerate(self.students):
            self.students_dictionary[student] =  index

    def plants(self, student_name):
        i = self.students_dictionary[student_name]
        items = [
            self.plant_name[self.rows[0][2*i]],
            self.plant_name[self.rows[0][2*i+1]],
            self.plant_name[self.rows[1][2*i]],
            self.plant_name[self.rows[1][2*i+1]]
        ]

        return items

garden = Garden("VCRRGVRG\nRVGCCGCV", students="Samantha Patricia Xander Roger".split())
print(garden.plants("Patricia"))