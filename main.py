# Built-in imports
import math
import pprint

# Your code below
GRADE ={}
keys = range(101)
for i in keys:
    GRADE[i] = i
    for i in keys:
        if i >= 70:
            GRADE[i] = "A"
        elif i >= 60 and i < 70:
            GRADE[i] = "B"
        elif i >= 55 and i < 60:
            GRADE[i] = "C"
        elif i >= 50 and i < 55:
            GRADE[i] = "D"
        elif i >= 45 and i < 50:
            GRADE[i] = "E"
        elif i >= 40 and i < 45:
            GRADE[i] = "S"
        elif i < 40:
            GRADE[i] = "U"
    

def read_testscores(filename):
    """
    Parameters
    -----------
        string
            a string of students' results
    Returns
    -------
        dict_list
            a dict list of the students, class, name, overall, grade
        example:
     {"Class: "Class1", 
      "Name : "Student1"
      "Overall" : some int value
      "grade" : "A"}
    """
    
    student_datalist = []
    with open(filename) as f:
        for lines in f.readline():
            line = [line.strip().split(",") for line in f.readlines()]
            if line == []:
                line = None
            else:
  
                for i in range(419):
                    class_ = line[i][0]
                    p1 = int(line[i][2])
                    p2 = int(line[i][3])
                    p3 = int(line[i][4])
                    p4 = int(line[i][5])
                    
                    overall = (p1/30 * 15) + (p2/40 * 30) + (p3/80 * 35) + (p4/30 * 20)
                    overall = math.ceil(overall)
                    grade = GRADE[overall]
                    studentdata = {"class": class_,
                                     "name" : f"Student{i}",
                                     "overall" : overall,
                                     "grade" : f"{grade}"}
                    student_datalist.append(studentdata)
                return student_datalist
                   
student_data = read_testscores("testscores.csv")
pprint.pprint(student_data)


def analyze_grades(students_data):
    """
    Parameters
    ----------
    list of dicts
        a list of dicts of each students data
    Returns
    -------
    dicts
        a dict that returns the number of students getting a specific grade
    """
    for i in range(419):
        class_ = students_data[i]["class"]
        grade = students_data[i]["grade"]
        while class_ == "Class1":
            print(class_)

    
students_data = read_testscores("testscores.csv")
analyze_grades(students_data)