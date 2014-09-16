#!/usr/bin/env python
"""
A Designator encapsulates the resolution of a value.
The 'description' of a value can be defined at write-time of the robot behavior,
	but the resolution of that value happens at runtime.
"""

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

	#Implement the same interface as a concurrent.Future support, because in some way, a Designator is kind of a Future.
	def cancel():
		"""Attempt to cancel the call."""
		raise NotImplementedError()

	def cancelled():
		"""Return True if the call was successfully cancelled."""
		raise NotImplementedError()

	def running():
		"""Return True if the call is currently being executed and cannot be cancelled."""
		raise NotImplementedError()

	def done():
		"""Return True if the call was successfully cancelled or finished running."""
		raise NotImplementedError()

	def exception(timeout=None):
		"""Return the exception raised by the call. If the call hasn't yet completed then this method will wait up to timeout seconds. """

	def result(timeout=None):
		"""Return the value returned by the call."""
		return self.resolve()

	def add_done_callback(fn):
		"""Attaches the callable fn to the future. fn will be called, with the future as its only argument, when the future is cancelled or finishes running."""
		raise NotImplementedError()

class PredefinedDesignator(Designator):
	"""For the occasion a value is already know at runtime but still should still be compatible with functions that use Designators"""

	def __init__(self, value):
		"""Set the value of this designator to 'value' at 'write-time', .g. when it is defined:
		>>> designator = PredefinedDesignator("Hello")
		>>> designator.resolve()
		'Hello'
		"""
		super(PredefinedDesignator, self).__init__()

		self.value = value

	def resolve(self):
		return self.value

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
