from day2.p02_inheritance.person import Person


class Student(Person):
    def __init__(self,name,age,batch="B40"):
        Person.__init__(self,name,age)
        self.batch=batch

    def __str__(self):
        return f"{Person.__str__(self)} - {self.batch}"



student1=Student("Jawid",30,"B30")
print(student1)

