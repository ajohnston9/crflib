#!/usr/bin/env python
"""
Cumulative Rank Frequency Library for Python 2.X with Sage and NumPy
----
This library will calculate the Cumulative Rank Frequency for a Poset (as defined by the Sage library)
and return a final ranking based on the Cumulative Rank Frequency. While the code has been tested with
multiple very small examples (i.e. fewer than ten nodes), it should work for larger sets. Note however 
that due to the algorithmically complex process of calculating the cumulative ranks, this code could take
a while if a Poset is particularly large.

This library requires Sage (in particular its Poset class) and NumPy to function.
"""

__status__     = "Production"
 
from numpy import transpose

def rev_lin_ex(lin_ex):
	rev_exts = []
	for llist in lin_ex:
		llist.reverse()
		rev_exts.append(llist)
	return rev_exts

def calc_partial_ranks(lin_ex):
    pranks = transpose(lin_ex).tolist()
    return pranks

def get_cum_ranks(lists, elems):
	retdict = {}
	#initialize dict
	for e in elems:
		retdict[e] = [] #Empty array
	for li in lists:
		for e in elems:
			#Count number of times
			val = li.count(e)
	 		if (len(retdict.get(e)) > 0 ):
				val += retdict.get(e)[-1] #add last element
			retdict.get(e).append(val)
	return retdict


def calculate_crf_rank(poset, elems):
	l = poset.linear_extensions(facade=True)
	lin_ex = l.list()
	lin_ex = rev_lin_ex(lin_ex)
	part_ranks = calc_partial_ranks(lin_ex)
	rankings = [None]*len(elems) #Actual rank
	rankdict = get_cum_ranks(part_ranks, elems)
	for i in range(0,len(elems)):
		maxletter = ''
		maxnum    = 0
		for lett in elems:
			num = rankdict.get(lett)[i]
			if (num > maxnum and rankings.count(lett) == 0):
				maxletter = lett
				maxnum    = num
		rankings[i] = maxletter
	return rankings
