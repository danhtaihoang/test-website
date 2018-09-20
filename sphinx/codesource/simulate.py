"""
functions for generating binary variables
"""
import numpy as np
import function as ft

#=========================================================================================
"""generate binary time-series 
    input: interaction matrix w[n,n], interaction variance g, data length l
    output: time series s[l,n]
""" 
def gen_binary(w,h0,l):
    n = np.shape(w)[0]
    s = np.ones((l,n))
    for t in range(1,l-1):
        h = h0 + np.sum(w[:,:]*s[t,:],axis=1) # Wij from j to i
        p = 1/(1+np.exp(-2*h))
        s[t+1,:]= ft.sign_vec(p-np.random.rand(n))
    return s
#=========================================================================================
"""generate coupling matrix w and binary time-series s
    input: number of variables n, coupling variance g, data length l
    output: coupling w[n,n] time series s[l,n]
""" 
def simulate_data(n,g,l):
    # generate interaction matrix
    w0 = np.random.normal(0.0,g/np.sqrt(n),size=(n,n))
    
    # generate data from actual couplings
    s0 = gen_binary(w0,0.,l)
    return w0,s0
