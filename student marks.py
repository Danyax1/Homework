class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def total_marks(self):
        return sum(self.marks.values())

    def percentage(self, max_marks_per_subject):
        total_obtained = self.total_marks()
        max_total = max_marks_per_subject * len(self.marks)
        return (total_obtained / max_total) * 100


if __name__ == '__main__':
    student = Student('Petro')
    student.add_mark('Maths', 100)
    student.add_mark('History', 10)
    print(student.total_marks())
    print(student.percentage(100))