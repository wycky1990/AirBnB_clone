import json 

class perso:
    def__init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return self.__dict__

p1 = person ("Amanuel", 234)
p2 = person ("Alex", 32)

dic_p1 = p1.to_dict()
print(p1.to_dict(), type(dict_p1))
print(json.dumps(dict_p1), type(json.dumps(dict_p1)))
