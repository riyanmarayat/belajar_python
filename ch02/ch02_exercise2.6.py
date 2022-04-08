# ch02_exercise2.6
"""Odd or Even"""

angka = int(input('Masukkan sebuah angka: '))
sisa_angka = angka % 2

if sisa_angka == 1:
	print(angka, 'merupakan angka ganjil')
elif sisa_angka == 0:
	print(angka, 'merupakan angka genap')
	
