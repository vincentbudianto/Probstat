''' NIM/Nama  : 13517050/Christopher Billy Setiawan, 13517137/Vincent Budianto
	Nama file : stat.py
	Topik     : Tugas Besar 01 IF2122 - Probabilitas dan Statistika
	Tanggal   : 09 April 2019
	Deskripsi : Pemrosesan data statistika '''

import pandas as pd
import matplotlib as plt

#Statistical descriptions
def stat(data):
	print('a. Minimum value')
	a = data.min(numeric_only = True)
	print(((a.round(3)).reset_index()).to_string(header = None, index = None))
	print()
	print('b. Maximum value')
	b = data.max(numeric_only = True)
	print(((b.round(3)).reset_index()).to_string(header = None, index = None))
	print()
	print('c. Mean')
	c = data.mean(numeric_only = True)
	print(((c.round(3)).reset_index()).to_string(header = None, index = None))
	print()
	print('d. Mode')
	d = data.mode(numeric_only = True)
	print((d.round(3)).to_string(index = None))
	print()
	print('e. Median')
	e = data.median(numeric_only = True)
	print(((e.round(3)).reset_index()).to_string(header = None, index = None))
	print()
	print('f. Variance')
	f = data.var(numeric_only = True)
	print(((f.round(3)).reset_index()).to_string(header = None, index = None))
	print()
	print('g. Standard deviation')
	g = data.std(numeric_only = True)
	print(((g.round(3)).reset_index()).to_string(header = None, index = None))
	print()
	print('h. Skewness')
	h = data.skew(numeric_only = True)
	print(((h.round(3)).reset_index()).to_string(header = None, index = None))
	print()
	print('i. Kurtosis')
	i = data.kurt(numeric_only = True)
	print(((i.round(3)).reset_index()).to_string(header = None, index = None))
	print()

#Algoritma
print('Dataset 1')
da = pd.read_csv('fifa.csv')
stat(da)
input()
print('Dataset 3')
db = pd.read_csv('black_friday.csv', header = None, names = ['total'])
stat(db)
input()
print('Dataset 4')
dc = pd.read_csv('crypto.csv', header = None, names = ['cryptocurrency'])
stat(dc)
input()
print('Dataset 5')
dd = pd.read_csv('athletes.csv')
stat(dd)

