class Person:
    def __init__(self,name,surname):
        self.f_name=name
        self.l_name=surname

    def __str__(self):
        return f"{self.f_name} - {self.l_name}"
# Person person1=new Person();
# person1=Person()
person1=Person("Adam","Barry")

#print(type(p))
print(person1.f_name)
print(person1.l_name)

print(f"{person1.f_name} {person1.l_name}")

print(person1)