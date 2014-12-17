CRF Library
===========

This is a small Python library that allows users to find a final ranking (in the form of a sorted array) from a Poset using the Cumulative Rank Frequency method.

This library requires Sage and NumPy to run. Simply copying and pasting the code into a Sage window should be sufficient if you need to use it.

##Usage##
(This assumes that the code is already in an environment where Sage and NumPy are installed)

 1. Use the `calculate_crf_ranks(poset,elems)` method by passing a [Sage Poset object](http://www.sagemath.org/doc/reference/combinat/sage/combinat/posets/posets.html) as the first argument and a list of elements in the poset as the second argument.
 2. The result returned will be the final ranking, returned as a list in sorted descending (i.e. top rank first) order.

----
This code is licensed under the MIT license.
