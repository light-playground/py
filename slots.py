

class Student(object):
	"""docstring for Student"""

	__slots__ = ('name', 'age')



if __name__ == '__main__':
	s = Student

	s.name = 'light'
	s.age = 12

	s.score = 12

	print s
