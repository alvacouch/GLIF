"""
	Licence: GPLv2
	Author: Jason White
	
	Definition of Group and Coordiate classes
"""


#Note that all coordinates are to be stored in nanometers
class vector:
	def __init__(self, x, y):
		self.x=x
		self.y=y
		
	def __str__(self):
		return self.__repr__()
	
	def __repr__(self):
		#print the name of the class and the X/Y coordinates
		#__class__._name__ is used to suppport inheritance
		return """<%s, x=%d y=%d>""" % (self.__class__._name__ ,self.x, self.y)
		
	def __add__(self, b):              
		return vector(self.x+b.x, self.y+b.y)
		
	def __sub__(self, b):
		return vector(self.x-b.x, self.y-b.y)

#coordinate inherits from vector
class coordinate(vector):
	def __repr__(self):
		return """<coordinate, x=%d y=%d>""" % (self.x, self.y)

#angle_pair inherits from vector		
class angle_pair(vector):
	def __repr__(self):
		return """<angle_pair, x=%d y=%d>""" % (self.x, self.y)

#design rules common to all primitives
class design_rule:
	def __init__(self, thickness, clearance):
		self.thickness=thickness
		self.clearance=clearance

class group:
	def __init__(self, x, y, layer, members):
		self.members=members
		self.location=coordinate(x, y)
		self.layer=layer
		self.angle=0
		self.attributes={}
		
	"""
		Normal member functions
	"""
        
	def move(self, x, y):
		self.location.x=x
		self.location.y=y
		
	def change_layer(self, layer):
		self.location.layer=layer
	
	"""
		Default functions which make this class behave like a list
	"""
	
	def __iter__(self):
		for member in self.members:
		    yield member
        
	def __len__(self):
		return len(self.members)
		
	def __getitem__(self, i):
		return self.members[i]
		
	def __delitem__(self, i):
		del self.members[i]
		
	def __setitem__(self, i, value):
		self.members[i] = value
		return self.members[i]
		
	def __str__(self):
		return self.__repr__()
	
	def __repr__(self):
		return """<group, %s, layer=%s, members=%s>""" % (self.location, str(self.layer), self.members)
		
	def insert(self, i, value):
		self.members.insert(i, value)
		
	def append(self, value):
		list_index = len(self.members)
		self.insert(list_index, value)
		


def test_coordinate():		
	a=coordinate(1, 2)
	b=coordinate(3, 4)
	print a
	print b
	print a+b
	print a-b
	
def test_groups():		
	a=group(1, 2, 0, [1, 2, 3])
	b=group(3, 4, 0, [4, 5, 6])
	print a
	print b

	print a[2]
