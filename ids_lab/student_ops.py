class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 85:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "F"

