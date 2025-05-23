class Person:
    def __init__(self,name,surname):
        self._f_name=name
        self._l_name=surname

    def __str__(self):
        return f"{self._f_name} - {self._l_name}"

    def get_name(self):
        return self._f_name
# Person person1=new Person();
# person1=Person()
person1=Person("Adam","Barry")

#print(type(p))
print(person1.get_name())
print(person1._l_name)

print(f"{person1._f_name} {person1._l_name}")

print(person1)