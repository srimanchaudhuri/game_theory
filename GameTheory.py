import numpy as np
import sys

print(" ")
R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))


print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
A = np.array(entries).reshape(R, C)

print(" ")

row_min = sys.maxsize
col_max = -sys.maxsize-1

row_min_list = []
col_max_list = []

n = len(A)
m = len(A[0])

for i in range(0,n):
	for j in range(0,m):
		row_min = min(row_min,A[i][j])
		col_max = max(col_max,A[j][i])
	row_min_list.append(row_min)
	row_min = sys.maxsize
	col_max_list.append(col_max)
	col_max = -sys.maxsize-1

found = False

for i in row_min_list:
	for j in col_max_list:
		if i == j:
			found = True
			saddle_point = i

if(found):
	print(f"\nSaddle point is found and it is : {saddle_point}")
else:
	print("Saddle point could not be determined")

print(" ")

# For 2 by 2 square matrix

if len(A)==len(A[0]) and len(A) == 2:
	diff_row_1 = abs(A[0][0]-A[0][1])
	diff_row_2 = abs(A[1][0]-A[1][1])
	diff_col_1 = abs(A[0][0]-A[1][0])
	diff_col_2 = abs(A[0][1]-A[1][1])

	total_row_diff = diff_row_1 + diff_row_2
	total_col_diff = diff_col_1 + diff_col_2
	p1 = diff_row_1/total_row_diff
	p2 = 1 - p1
	q1 = diff_col_1/total_col_diff
	q2 = 1 - q1

	print(f"p1 = {p1} p2 = {p2} q1 = {q1} q2 = {q2}\n")
