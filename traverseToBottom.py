"""
Two positive integers representing the width and height of a grid-shaped, rectangular graph are given.
Write a function that returns the number of ways to reach the bottom right corner of the graph when starting 
at the top left corner. Note: Only move down or right.
"""


# O(2^(m + n)) time | O(m + n) space
# n-width, m-height
def solution(width, height):
	if width == 1 or height == 1:
		return 1
	return solution(width - 1, height) + solution(width, height - 1)



# O(n * m) time | O(n * m) space
# n-width, m-height
def solution(width, height):
	graph = [[None for _ in range(width + 1)] for _ in range(height + 1)]
	for heightIdx in range(1, height + 1):
		for widthIdx in range(1, width + 1):
			if heightIdx == 1 or widthIdx == 1:
				graph[heightIdx][widthIdx] == 1
			else:
				graph[heightIdx][widthIdx] = graph[heightIdx - 1][widthIdx] + graph[heightIdx][widthIdx - 1]

	return graph[height][width] 




