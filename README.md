## decorator

https://www.zhihu.com/question/26930016


```python
from functools import wraps

class Route(object):
	"""docstring for Route"""
	def __init__(self, *args, **kwargs):
		self.__args = args
		self.__kwaras = kwargs

	def __call__(self, func):

		@wraps(func)
		def wrapper(*args, **kwargs):
			print 'class decorator running'
			print self.__args
			print self.__kwaras

			func(*args, **kwargs)
			print 'class decorator ending'

		return wrapper



@Route(method = 'GET')
def hello():
	"""this is hello"""
	print '%s world' % 'hello'


if __name__ == '__main__':

	print hello.__doc__

	hello()
```