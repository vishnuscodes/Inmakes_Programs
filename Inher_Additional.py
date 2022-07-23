class Doctor:
    def __init__(self):
        self.doctor = input("Enter doctors name: ")
        self.nurse = input("Enter the name of the nurse: ")
        self.department = input("Enter the department: ")

class Department(Doctor):
    def getdetails(self):
        print("Doctor: "+self.doctor)
        print("Nurse: "+self.nurse)
        print("Department: "+self.department)

class Patient:
    def __init__(self):
        self.name = input("Enter patient's name: ")
        self.age = input("Enter patient's age: ")
        self.disease = input("Enter patient's disease: ")


    def getpatientdetails(self):
        print("Name: " +self.name)
        print("Age: "+self.age)
        print("Disease: "+self.disease)


dept1 = Department()
dept1.getdetails()

patient1 = Patient()
patient1.getpatientdetails()