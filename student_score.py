class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        #if self.score not in range(101):
        # #raise ValueError

        if self.score >= 0 and self.score < 60:
            return 'C'
        if self.score < 80 and self.score >= 60:
            return 'B'
        if self.score <= 100 and self.score >= 80:
            return 'A'
        if self.score not in range(0, 101):
            raise ValueError


#t = Student('pcc', 100)
#print(t.get_grade())