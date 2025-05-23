class Person:
    def __init__(self,name,surname):
        self.__f_name=name
        self.__l_name=surname

    def __str__(self):
        return f"{self.__f_name} - {self.__l_name}"

    def get_name(self):
        return self.__f_name

    def get_last_name(self):
        return self.__l_name
# Person person1=new Person();
# person1=Person()
person1=Person("Adam","Barry")

#print(type(p))
print(person1.get_name())
print(person1.get_last_name())
