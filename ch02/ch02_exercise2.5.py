# ch02_exercise2.5
"""Eggs per Box"""

box = 6
egg = int(input('Masukkan jumlah telur yang akan disetorkan: '))
nbox = egg // box
sisa_egg = egg % box
butuh_egg = box - sisa_egg

if sisa_egg == 0:
	print('Terdapat', egg, 'telur yang akan dimasukkan ke dalam', nbox, 'box')
elif sisa_egg > 0:
	print('Terdapat', egg, ' telur yang akan dimasukkan dalam', nbox + 1, 'box dengan salah satu box hanya terisi', sisa_egg, 'telur, sehingga membutuhkan', butuh_egg, 'telur agar box tersebut terisi dengan penuh')


