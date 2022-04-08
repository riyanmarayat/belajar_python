# ch02_exercise2.10
"""Arithmetic, Highest and Lowest"""

math_grade = int(input('Masukkan nilai matematika: '))
fis_grade = int(input('Masukkan nilai fisika: '))
kim_grade = int(input('Masukkan nilai kimia: '))

jumlah = math_grade + fis_grade + kim_grade
rata_2 = jumlah / 3
terendah = min(math_grade, fis_grade, kim_grade)
tertinggi = max(math_grade, fis_grade, kim_grade)

print('Nilai rata - rata dari tiga matkul adalah', rata_2)
if terendah == math_grade == fis_grade == kim_grade:
	print('\nTidak ada matkul dengan nilai terendah karena semua matkul mempunyai nilai yang sama')
elif terendah == math_grade == fis_grade:
	print('\nMatkul matematika dan fisika merupakan matkul dengan nilai terendah yaitu', terendah)
elif terendah == math_grade == kim_grade:
	print('\nMatkul matematika dan kimia merupakan matkul dengan nilai terendah yaitu', terendah)
elif terendah == fis_grade == kim_grade:
	print('\nMatkul fisika dan kimia merupakan matkul dengan nilai terendah yaitu', terendah)
elif terendah == math_grade:
	print('\nMatkul terendah adalah matematika dengan nilai', terendah)
elif terendah == fis_grade:
	print('\nMatkul terendah adalah fisika dengan nilai', terendah)
elif terendah == kim_grade:
	print('\nMatkul terendah adalah kimia dengan nilai', terendah)

if tertinggi == math_grade == fis_grade == kim_grade:
	print('\nTidak ada matkul dengan nilai tertinggi karena semua matkul mempunyai nilai yang sama')
elif tertinggi == math_grade == fis_grade:
	print('\nMatkul matematika dan fisika merupakan matkul dengan nilai tertinggi yaitu', tertinggi)
elif tertinggi == math_grade == kim_grade:
	print('\nMatkul matematika dan kimia merupakan matkul dengan nilai tertinggi yaitu', tertinggi)
elif tertinggi == fis_grade == kim_grade:
	print('\nMatkul fisika dan kimia merupakan matkul dengan nilai tertinggi yaitu', tertinggi)
elif tertinggi == math_grade:
	print('\nMatkul tertinggi adalah matematika dengan nilai', tertinggi)
elif tertinggi == fis_grade:
	print('\nMatkul tertinggi adalah fisika dengan nilai', tertinggi)
elif tertinggi == kim_grade:
	print('\nMatkul tertinggi adalah kimia dengan nilai', tertinggi)
	
