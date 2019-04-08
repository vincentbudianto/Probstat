''' NIM/Nama  : 13517050/Christopher Billy Setiawan, 13517137/Vincent Budianto
	Nama file : stat.py
	Topik     : Tugas Besar 01 IF2122 - Probabilitas dan Statistika
	Tanggal   : 09 April 2019
	Deskripsi : Pemrosesan data statistika '''
'''
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
'''

import warnings
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib
import matplotlib.pyplot as plt

def best_fit_distribution(data, bins=200):
    #Data bertipe array-like. x dan y akan menjadi array karena fungsi np.histogram
    y,x = np.histogram(data, bins=bins, density=True)
    x = (x + np.roll(x, -1))[:-1] / 2.0

    DISTRIBUTIONS = [        
        st.binom,st.multinomial,st.hypergeom,st.nbinom,st.geom,st.poisson, st.uniform,st.chi2,st.f,st.norm,st.lognorm,st.t,st.gamma,st.beta,st.alpha,st.expon,st.weibull_min,st.weibull_max
    ]

    # Best holders
    best_distribution = st.norm
    best_params = (0.0, 1.0)
    best_sse = np.inf

    # Estimate distribution parameters from data
    for distribution in DISTRIBUTIONS:
        # Try to fit the distribution
        try:
            # Ignore warnings from data that can't be fit
            with warnings.catch_warnings():
                warnings.filterwarnings('ignore')
                
                # fit dist to data
                params = distribution.fit(data)
                
                # Separate parts of parameters
                arg = params[:-2]
                loc = params[-2]
                scale = params[-1]

                # Calculate fitted PDF and error with fit in distribution
                pdf = distribution.pdf(x, loc=loc, scale=scale, *arg)
                sse = np.sum(np.power(y - pdf, 2.0))

                # identify if this distribution is better
                if best_sse > sse > 0:
                    best_distribution = distribution
                    best_params = params
                    best_sse = sse

        except Exception:
            pass

    return (best_distribution.name, best_params)

# Load data from statsmodels datasets
data = pd.read_csv(r'fifa.csv',  header = None, skiprows = 1)
data = data[1].values
# Find best fit distribution
best_fit_name, best_fit_params = best_fit_distribution(data, 200)
best_dist = getattr(st, best_fit_name)
print(best_fit_name)
