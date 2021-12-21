"""
A magic index in an array A[0...n-1] is defined to be an index such that 
A[i] = i. Given a sorted array of distinct integers, write a method to find
a magic index, if one exists, in array A.
"""

#brute-force
def solution(A):
	for i in len(A):
		if i == A[i]:
			return i
	return -1
	
#O(logN)
def magic_index(A, min_index=0, max_index=None):
	if max_index is None:
		max_index = len(A)-1

	if max_index < min_index:
		return -1
	mid_index = (min_index + max_index) // 2
	if A[mid_index] == mid_index:
		return mid_index
	if A[mid_index] < min_index:
		return magic_index(A, mid_index+1, max_index)
	if A[mid_index] > mid_index:
		return magic_index(A, min_index, mid_index-1)


#supposed that array A may contain duplicate integers.
def magic_index_duplicate(A, min_index=0, max_index=None):
	if max_index is None:
		max_index = len(A) - 1
	if max_index < min_index:
		return -1
	mid_index = (min_index + max_index) // 2
	if A[mid_index] == mid_index:
		return mid_index

	#search left side
	left_index = min(A[mid_index], mid_index-1)
	left = magic_index_duplicate(A, min_index, left_index)
	if left >= 0:
		return left

	#search right side
	right_index = max(A[mid_index], mid_index+1)
	return magic_index_duplicate(A, right_index, max_index)














