"""
Python basic
"""

from functools import wraps

class Human(object):

	species = "H, in space"
	__species = "Other. species"

	__dict = {}
	__set = set()
	__tuple = (1, 2, 3)

	__list = [1, 2, 3]

	"""docstring for Human"""
	def __init__(self, name):
		self.name = name
		self.age = 0

		self.__dict['name'] = name


		self.__list.append(4)

	def say(self, msg):
		return ": ".format(self.name, msg)

	@classmethod
	def get_species(cls):
		return cls.species

	@staticmethod
	def grunt():
		return "*Grunt*"

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, age):
		self.__age = age

	@age.deleter
	def age(self):
		del self.__age


	def print_self(self):
		print '*' * 10
		self.__set.add(1)

		print self.__dict
		print self.__set
		print self.__tuple
		print self.__list
		print '*' * 10



	def list_oper(self):
		a = []

		b = [4, 5, 6]

		a.append(1)
		a.append(2)
		a.append(3)

		print 'pop from list:',  a.pop()
		a.append(3)

		print 'origin: ', a, 'slice[1:3]:', a[1:3]

		print a, '+', self.__list, '=', a + self.__list

		a.extend(self.__list)

		print a

		print 'the index of 2 ', a.index(2)

		a.remove(3) # remove 3 from the list

		print 'remove 3 from the list ',  a

		a.insert(1, 4)

		print a

		#lower than 4
		x = filter(lambda x: x < 4, self.__list)
		print 'lower than 4:', x

		y = [x for x in self.__list if x > 2]
		print 'higher than 2:', y


	def pargs(self, *args):
		print args

	def pkwargs(self, **kwargs):
		print kwargs


	def test_lambda(self):
		return (lambda x: x > 5)(6)


def beg(**kwargs):
	def decorator(target_func):
		@wraps(target_func)
		def wrapper(*args, **kwargs1):
			print kwargs
			msg, say_pls = target_func(*args, **kwargs1)

			if say_pls:
				return '{} {}'.format(msg, 'Please! I am poor :(')

			return msg

		return wrapper

	return decorator

@beg(name="light", age=10)
def buy_me_coffe(say_please = False):
	msg = 'Can you buy me a coffe?'
	return msg, say_please


class Route(object):
	"""docstring for Route"""
	def __init__(self, func):
		self.__func = func

	def __call__(self):
		print 'class decorator running'
		self.__func()
		print 'class decorator ending'


@Route
def hello():
	"""aaa"""
	print __name__

if __name__ == '__main__':
	h = Human('huang')

	print h.say('hi')

	print h.get_species()

	print Human.grunt()

	h.age = 42
	print h.age

	h.print_self()

	h.list_oper()


	print '*' * 10
	print buy_me_coffe()
	print buy_me_coffe(True)


	hello()
	print hello.__doc__