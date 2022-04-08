# ch02_exercise2.14
"""Target Heart-Rate Calculator"""

usia = int(input('Masukkan usia anda: '))
detak_jantung_permenit = 220 - usia
min_detak_jantung = detak_jantung_permenit * 50 // 100
max_detak_jantung = detak_jantung_permenit * 85 // 100

print('Jadi detak jantung anda seharusnya berada pada kisaran', min_detak_jantung, 'sampai', max_detak_jantung, 'permenit')
