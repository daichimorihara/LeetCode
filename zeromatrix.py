def solution(matrix):
	m = len(matrix)
	n = len(matrix[0])
	zero_place = []
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == 0:
				zero_place.append([i, j])

	while zero_place:
		index = zero_place.pop()
		for i in range(n):
			matrix[index[0]][i] = 0
		for j in range(m):
			matrix[j][index[1]] = 0

#same logic with different sintax
def solution(matrix):
	m = len(matrix)
	n = len(matrix[0])
	rows = []
	columns = []
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == 0:
				rows.append(i)
				columns.append(j)

	for row in rows:
		for i in range(n):
			matrix[row][i] == 0

	for column in columns:
		for i in range(m):
			matrix[i][column] == 0