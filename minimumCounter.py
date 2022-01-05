"""
Write a function that takes in an integer matrix and returns the minimum number of passes 
required to convert all negative integers in the matrix to positive integers. Negative integer
can only be converted to a positive integer if one or more of its neighboring elements is positive.
Note: 0 is neither positive nor negative.
"""

def minimumPassesOfMatrix(matrix):
    # Write your code here.
    counts = convertsNegatives(matrix)
	return counts if not containsNegative(matrix) else -1

def convertsNegatives(matrix):
	nextStack = getPositivePositions(matrix)
	count = 0
	while len(nextStack) > 0:
		currentStack = nextStack
		nextStack = []
		
		while len(currentStack) > 0:
			currentPosition = currentStack.pop()
			currentRow, currentCol = currentPosition
			
			neighborsPositions = getNeighborsPositions(currentRow, currentCol, matrix)
			for position in neighborsPositions:
				row, col = position
				value = matrix[row][col]
				if value < 0:
					matrix[row][col] *= -1
					nextStack.append([row, col])
					
		count += 1
	
	return count - 1

def getPositivePositions(matrix):
	positivePositions = []
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			value = matrix[row][col]
			if value > 0:
				positivePositions.append([row, col])
				
	return positivePositions

def getNeighborsPositions(row, col, matrix):
	neighbors = []
	if row > 0:
		neighbors.append([row - 1, col])
	if row < len(matrix) - 1:
		neighbors.append([row + 1, col])
	if col > 0:
		neighbors.append([row, col - 1])
	if col < len(matrix[0]) - 1:
		neighbors.append([row, col + 1])
	
	return neighbors

def containsNegative(matrix):
	for row in matrix:
		for value in row:
			if value < 0:
				return True
	return False