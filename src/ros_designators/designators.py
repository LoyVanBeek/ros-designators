#!/usr/bin/env python
"""
A Designator encapsulates the resolution of a value.
The 'description' of a value can be defined at write-time of the robot behavior,
	but the resolution of that value happens at runtime.
"""

import rospy

class Designator(object):
	"""A Designator encapsulates the resolution of a value.
	The 'description' of a value can be defined at write-time of the robot behavior,
		but the resolution of that value happens at runtime.
	For example, an instantiation of a subclass of Designator could exist that is called drink_location.
	It may not be possible to know this location at write-time,
		but we can encapsulate the process of determining this location in a Designator.
	The subclass may do a query to a database, await a message from a perception routine or just do a heavy calculation,
		as long as the result is finally obtained via .resolve()"""

	def __init__(self):
		pass

	def resolve(self):
		"""Returns whatever the designator should resolve to"""
		raise NotImplementedError()

class SettableDesignator(Designator):
	"""SettableDesignator can be set to a value, which is then returned by resolve().
	Can be used as a passthrough between otherwise independent objects"""

	def __init__(self):
		super(SettableDesignator, self).__init__()

		self.value = None

	def set(self, value):
		"""Set the value of this designator to 'value'
		>>> designator = SettableDesignator()
		>>> designator.set("Hello")
		>>> designator.resolve()
		'Hello'
		"""

		self.value = value

	def resolve(self):
		return self.value

if __name__ == "__main__":
	import doctest
	doctest.testmod()
