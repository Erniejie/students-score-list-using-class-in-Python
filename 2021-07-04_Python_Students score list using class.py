#students score list using class in Python

# Defining Student class with name &enrollment& Scores

class Student(object):
    def __init__(self,name,roll,scores):
        self.name = name
        self.roll = roll
        self.scores = scores

    def getscores(self):
        return self.scores

    def getroll(self):
        return self.roll

    def __str__(self):
        return self.name + "|" + str(self.getroll()) + "|" + str(self.getscores())

def scores(rec,name,roll,scores):
    rec.append(Student(name,roll,scores))
    return rec

Record = []

x = "y"

while x == "y":
    name = input("Enter the Name of The Student: ")
    height = input("Enter The Roll Number: ")
    roll = input("Scores:")
    Record = scores(Record,name,roll,height)
    x = input("Any More Students? y/n:")

#Printing The List of Students
count = 1
for rec in Record:
    print(count,"|",rec)
    count =count +1

