from pprint import pprint

class Example():
		def met1(self, value):
				self.variable = value
		@classmethod
		def met2(cls, value):
				cls.variable = value


a = Example()
b = Example()

# a.met2(85)
# print(b.variable)

# result : 85


class Member():
    _ins = list()
    
    def __init__(self, name, height, weight, fat):
        self.name = name
        self.height = height
        self.weight = weight
        self.fat = fat
        
        self.add_instance(self)
        
    @classmethod
    def add_instance(cls, ins):
        cls._ins.append(ins)
        
a = Member("kim", 180, 77, 24)
b = Member("Ihm", 170, 71, 16)
c = Member("Choi", 160, 51, 23)
d = Member("Park", 170, 63, 20)

height_mean = [m.height for m in Member._ins]
pprint(height_mean)