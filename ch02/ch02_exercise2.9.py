# ch02_exercise2.9
"""Integer Value of a Character"""

T = ord('T')
o = ord('o')
m = ord('m')
J = ord('J')
i = ord('i')

Tom = T + o + m
Jim = J + i + m

if Tom > Jim:
	print('Tom mulai terlebih dahulu')
elif Tom < Jim:
	print('Jim mulai terlebih dahulu')
else:
	print('Error')
	
