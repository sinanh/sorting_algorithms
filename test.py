#!/usr/bin/python
import numpy as np

def test(sorting_alg):
	for i in range(5):
		rnd = np.random.randint(1,50,7)
		unsorted = rnd.copy()
		sorted  = sorting_alg(rnd)
		rnd.sort()
		assert (rnd == sorted).all(), "Fail"
	print("passed the tests")
