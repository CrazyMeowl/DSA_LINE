import numpy as np

# Alter dimensions as needed


board =[[['gre', 2], ['red', 2], ['red', 2], ['blu', 2], ['yel', 2], ['red', 2], ['gre', 2], ['bro', 2], ['gre', 2]],
		[['gre', 2], ['gre', 2], ['   ', 0], ['yel', 2], ['yel', 2], ['blu', 2], ['bro', 2], ['blu', 2], ['pur', 2]],
		[['pur', 2], ['bro', 2], ['pur', 2], ['bro', 2], ['yel', 2], ['blu', 2], ['red', 2], ['blu', 2], ['yel', 2]],
		[['   ', 0], ['blu', 2], ['gre', 2], ['gre', 2], ['yel', 2], ['blu', 2], ['bro', 2], ['blu', 2], ['yel', 2]],
		[['blu', 2], ['red', 2], ['   ', 0], ['pur', 2], ['pur', 2], ['yel', 2], ['gre', 2], ['yel', 2], ['bro', 2]],
		[['blu', 2], ['bro', 1], ['   ', 0], ['bro', 2], ['gre', 2], ['gre', 2], ['red', 2], ['bro', 2], ['blu', 2]],
		[['gre', 2], ['pur', 2], ['yel', 2], ['bro', 2], ['bro', 2], ['blu', 2], ['gre', 2], ['pur', 2], ['blu', 2]],
		[['   ', 0], ['bro', 2], ['bro', 2], ['bro', 2], ['bro', 2], ['bro', 2], ['bro', 2], ['red', 2], ['yel', 2]],
		[['yel', 2], ['pur', 2], ['pur', 2], ['gre', 2], ['red', 2], ['gre', 2], ['   ', 0], ['   ', 0], ['blu', 2]]]

def createtempboard2(board):
	tempboard = []
	for i in board :
		tempi = []
		for _ in i:

			if _[1] == 0 or _[1] == 1:
				tempi.append('   ')

			elif _[1] == 2 :
				tempi.append(_[0])
		tempboard.append(tempi)
	return tempboard

a =np.array(createtempboard2(board))
print(a)
# a.diagonal returns the top-left-to-lower-right diagonal "i"
# according to this diagram:
#
#  0  1  2  3  4 ...
# -1  0  1  2  3
# -2 -1  0  1  2
# -3 -2 -1  0  1
#  :
#
# You wanted lower-left-to-upper-right and upper-left-to-lower-right diagonals.
#
# The syntax a[slice,slice] returns a new array with elements from the sliced ranges,
# where "slice" is Python's [start[:stop[:step]] format.

# "::-1" returns the rows in reverse. ":" returns the columns as is,
# effectively vertically mirroring the original array so the wanted diagonals are
# lower-right-to-uppper-left.
#
# Then a list comprehension is used to collect all the diagonals.  The range
# is -x+1 to y (exclusive of y), so for a matrix like the example above
# (x,y) = (4,5) = -3 to 4.
diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]

# Now back to the original array to get the upper-left-to-lower-right diagonals,
# starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.
#diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))
diags2 = [a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1)]
# Another list comp to convert back to Python lists from numpy arrays,
# so it prints what you requested.
dlist1 = [n.tolist() for n in diags]
dlist2 = [n.tolist() for n in diags2]
print(dlist1)
print(dlist1)