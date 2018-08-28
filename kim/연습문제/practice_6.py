# 6.1
class thing ():
	pass
print(thing)

example = thing()
print(example)

# 6.2
class thing2():
	letters = 'abc'
	
print(thing2.letters)

# 6.3
class thing3():
		def __init__(self, letters):
			self.letters = letters

example2 = thing3('xyz')
print(example2.letters)

# 6.4
class Element:
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number
		
hydrogen = Element('hydrogen', 'H', 1)
print(hydrogen.name)

# 6.5
el_dict = {'name':'hydrogen','symbol':'H','number':1}
hydrogen = Element(**el_dict)
print(hydrogen.name)

# 6.6
class Element:
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number
		
	def dump(self):
		print ('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))

hydrogen = Element(**el_dict)
hydrogen.dump()
	
# 6.7
class Element:
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number
	def __str__(self):
		return ('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))
		
hydrogen = Element(**el_dict)
print(hydrogen)

# 6.8
class Element:
	def __init__(self, name, symbol, number):
		self.__name = name
		self.__symbol = symbol
		self.__number = number
		
	@property
	def name(self):
		return self.__name
	@property
	def symbol(self):
		return self.__symbol
	@property
	def number(self):
		return self.__number
		
hydrogen = Element(**el_dict)
print(hydrogen.name)

# 6.9

class Bear:
	def eats(self):
		print('barries')
		
class Rabbit:
	def eats(self):
		print('clover')
		
class Octothorpe:
	def eats(self):
		print('campers')
		
bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()

bear.eats()
rabbit.eats()
octothorpe.eats()

# 6.10

class Laser:
	def does(self):
		return 'distingerate'
		
class Claw:
	def does(self):
		return 'crush'
		
class SmartPhone:
	def does(self):
		return 'ring'
		
class Robot:
	def __init__(self):
		self.laser = Laser()
		self.claw = Claw()
		self.smartphone = SmartPhone()
		
	def does(self):
		return 'Laser does %s, Claw does %s, SmartPhone does %s' %(self.laser.does(), self.claw.does(), self.smartphone.does())
		
robot = Robot()
print(robot.does())
