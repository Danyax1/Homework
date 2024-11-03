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