#!/usr/bin/env python
"""
"""
import rospy
import psi
import designators

class PsiDesignator(designators.Designator):
	"""A PsiDesignator encapsulates Psi queries to a reasoner.
	A reasoner may return multiple valid answers to a query, but """

	def __init__(self, query, reasoner, filterfunc=None, sortkey=None, sortorder=None, criteriafuncs=None):
		self.query 			= query
		self.reasoner 		= reasoner
		self.filterfunc 	= filterfunc
		self.sortkey 		= sortkey
		self.sortorder 		= sortorder
		self.criteriafuncs 	= criteriafuncs

	def resolve(self):
		"""Returns whatever the designator should resolve to"""
		raise NotImplementedError()

if __name__ == "__main__":
	import doctest
	doctest.testmod()
