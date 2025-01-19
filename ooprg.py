# class Employee:
#     company = 'Deloitte'

#     def __init__(self, eid, ename, esal, eloc):
#         self.eid = eid
#         self.ename = ename
#         self.esal = esal
#         self.eloc = eloc

#     def display(self):
#         print("Company :",Employee.company)
#         print('The employ id is :', self.eid)
#         print("The employ's name is :", self.ename)
#         print("The employ salary is :", self.esal)
#         print("The employ locaton is :", self.eloc)

#     def taxcalc(self):
#         if self.esal <= 2500:
#             print("The total amount tax you have to pay is :", self.esal*0.00)
#         elif self.esal > 2500 and self.esal <= 5000:
#             print("The total amount you have to pay is :", self.esal*0.05)
#         elif self.esal > 5000 and self.esal <= 7500:
#             print("The total amount of tax ypu have to pay is :", self.esal*0.10)
#         elif self.esal > 7500:
#             print("The total amount of tax you have to pay is :", self.esal*0.20)
#         else:
#             print("Invalid format")

#     def bonuscalc(self):
#         if self.eloc == "Mumbai":
#             print ('Total bonus you will get is',self.esal*0.10)
#         else:
#             print ("The total bonus you will get is",self.esal*0.20)

# e1 = Employee(4854,'Dastagir',45000,'Mumbai')
# e1.display()
# e1.taxcalc()
# e1.bonuscalc()



class Person:
    name = "Dastagir"
    Occupation = "Stressfull coder"
    networth = 2000

    def info(self):
        print(f"{self.name} is a {self.Occupation} and his networth is {self.networth}")

d = Person()
a = Person()
b = Person()
c = Person()

a.name = "Saud"
a.Occupation = "Gym wala"
a.networth = 1500

b.name = "Zeeshan"
b.Occupation = "Depressed Engineer"
b.networth = -2000

c.name = "Shahzeb"
c.Occupation = "Student/Chef"
c.networth = 5000

d.info()
a.info()
b.info()
c.info()