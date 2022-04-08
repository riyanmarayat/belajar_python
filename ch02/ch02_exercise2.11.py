# ch02_exercise2.11
"""Calculating Time"""

inp_second = int(input('Masukkan banyak detik: '))
second = inp_second % 60
inp_menit = inp_second // 60
menit = inp_menit % 60
jam = inp_menit // 60

print(jam, '-', menit, '-', second)
