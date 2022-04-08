# ch02_exercise2.7
"""The Remainder Operator"""

nmarble = int(input('Masukkan jumlah marble: '))
sisa = nmarble % 4
nmarble_bagi = nmarble // 4

if sisa == 0:
	print('Marble bisa dibagikan sama rata dengan masing - masing mendapatkan', nmarble_bagi, 'marble')
else:
	print('Marble tidak bisa dibagikan sama rata dengan', sisa, 'orang mendapatkan', nmarble_bagi, 'marble, sedangkan', 4 - sisa, 'orang mendapatkan', nmarble_bagi + 1, 'marble')
	
