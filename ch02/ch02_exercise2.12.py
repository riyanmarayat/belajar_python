# ch02_exercise2.12
"""Hourly Wage Calculator"""

w = int(input('Masukkan upah perjam: '))
upah_per_tahun = 10 * 365 * w
tot_upah = upah_per_tahun
w = w * (1 + (3 / 100))
tot_upah = tot_upah + upah_per_tahun
w = w * (1 + (3 / 100))
tot_upah = tot_upah + upah_per_tahun
w = w * (1 + (3 / 100))
tot_upah = tot_upah + upah_per_tahun
w = w * (1 + (3 / 100))
tot_upah = tot_upah + upah_per_tahun
w = w * (1 + (3 / 100))
tot_upah = tot_upah + upah_per_tahun
w = w * (1 - (3 / 100))
tot_upah = tot_upah + upah_per_tahun
w = w * (1 - (3 / 100))
tot_upah = tot_upah + upah_per_tahun

print('Total upah yang dikumpulkan selama 8 tahun adalah', tot_upah)
