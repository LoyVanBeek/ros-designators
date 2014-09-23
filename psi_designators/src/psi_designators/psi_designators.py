#!/usr/bin/env python
"""
"""
import rospy
import psi
import designators
import inspect
import pprint

class PsiDesignator(designators.Designator):
	"""A PsiDesignator encapsulates Psi queries to a reasoner.
	A reasoner may return multiple valid answers to a query, but """

	def __init__(self, query, reasoner, sortkey=None, sortorder=min, criteriafuncs=None):
		"""Define a new designator around a Psi query, to be posed to a reasoner
		@param query the query to be posed to the given reasoner
		@param reasoner the reasoner that should answer the query"""
		self.query          = query
		self.reasoner       = reasoner
		self.sortkey        = sortkey
		self.sortorder      = sortorder
		self.criteriafuncs  = criteriafuncs or []

	def resolve(self):
		"""Returns whatever the designator should resolve to"""
		answers = self.reasoner.query(self.query)

		rospy.loginfo("{0} answers before filtering: {1}".format(len(answers), pprint.pformat(answers)))
		for criterium in self.criteriafuncs:
			answers = filter(criterium, answers)
			criterium_code = inspect.getsource(criterium)
			rospy.loginfo("Criterium {0} leaves {1} answers: {2}".format(criterium_code, len(answers), pprint.pformat(answers)))

		if not answers:
			raise ValueError("No answers matched the critera.")

		return self.sortorder(answers, key=self.sortkey)[0]

if __name__ == "__main__":
	import doctest
	doctest.testmod()
