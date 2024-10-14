# You are tasked with creating a mini student management system for a school. The system should store and manage student data (name, age, grades in three subjects, and their student ID). It should have the following functionalities:

# Add a new student: You should be able to add a new student with their name, age, and grades in three subjects. The student ID should be auto-generated.
# Calculate the average grade for each student.
# Display the student information along with their average grade.
# Save student information to a file and load the data back from the file when the system restarts.
# Implement error handling for invalid inputs like non-numeric grades or negative ages.
# Details:

# Use a class Student with attributes for name, age, grades, and student ID.
# The system should allow adding multiple students and store them in a list.
# The student information (including their average grade) should be saved in a file called students.txt. Each time the program runs, it should load the previous data if available.
# Use exception handling to catch errors when reading or writing files and when invalid data (like negative numbers for age or non-numeric grades) is entered.

import random

class FileHandling:
    def write_data(self,fileName,data):
        with open(fileName,"w") as file:
            file.write(data)
            file.close()
    
    def read_file(self,fileName):
        with open(fileName,'r') as file:
            data=file.read()
            file.close()
            return data

class Students:
    def __init__(self):
        # Load existing students from file if available
        self.students=self.toListFormat()
    
    def createStudent(self,name,age,english,science,maths):
        self.studentId=random.randint(1,10000001)
        self.name=name
        self.english=int(english)
        self.science=int(science)
        self.maths=int(maths)
        self.grade={'english':english,'maths':maths,'science':science}
        self.age=age
        self.student={'id':self.studentId,'name':self.name,'grade':self.grade,'age':self.age}
        self.students.append(self.student)
    
    # Convert the self.students list to string format to store in file
    def toStringFormat(self):
        if len(self.students)==0:
            return ""
        return "\n".join(map(str,self.students)) + '\n'
    
    # Convert the string file stored in student.txt to List 
    def toListFormat(self):
        file_handling=FileHandling()
        data=file_handling.read_file("student.txt")
        students_data=[]
        if data is None: 
            return students_data
        for line in data.split("\n"):
            # strip() == trim() in js
            if line.strip():
                # convert string  to dictionary 
                student=eval(line)
                students_data.append(student)
        return students_data
        

    def getAllStudents(self):
        return self.students

    def average(self):
        # return sum(grade for grade in self.grade.values())/len(self.grade)
        return sum(self.grade.values())/len(self.grade)
    
    def display(self):
        print(f"Average grade of student is: {self.average()}")

if __name__=="__main__":
    students=Students()
    file_handling=FileHandling()

    def continue_further():
        continues=input("Do you want to continue further(Y/N) ")
        if continues.lower()=='y' or continues.lower() == 'yes':
            return True
        elif continues.lower()=='n' or continues.lower() == 'no':
            return False
        else:
            continue_further()

    
    while True:
        name=input("Enter name of the student to append to the Database: ")
        age=input("Enter age ")
        english=int(input("Enter marks in English "))
        science=int(input("Enter marks in Science "))
        maths=int(input("Enter marks in Maths "))
        students.createStudent(name,age,english,science,maths)
        students.display()
        if continue_further():
            continue
        else:
            print("All Students ",students.getAllStudents())
            file_handling.write_data("student.txt",students.toStringFormat())
            students.toListFormat()
            break

