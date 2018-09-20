import numpy as np
import matplotlib.pyplot as plt

#=========================================================================================
""" plot actual coupling matrix w0 and predicted coupling matrix w    
""" 
def plot_w(w0,w):
    w0min = w0.min()
    w0max = w0.max()
    w0max = max(abs(w0min),w0max)

    if w0max < 0.3:
        wmax = 0.3
    else:
        wmax = np.round(w0max)+0.5

    wtick = np.round(wmax/2.)+0.2

    plt.figure(figsize=(12,3.5))
    plt.subplot2grid((1, 3), (0, 0), colspan=1,rowspan=1)
    plt.title('actual coupling matrix')
    plt.imshow(w0,cmap='rainbow',origin='lower')
    plt.xlabel('j')
    plt.ylabel('i')
    plt.clim(-wmax,wmax)
    plt.colorbar(fraction=0.045, pad=0.05,ticks=[-wmax,0,wmax])

    plt.subplot2grid((1, 3), (0, 1), colspan=1,rowspan=1)
    plt.title('predicted coupling matrix')
    plt.imshow(w,cmap='rainbow',origin='lower')
    plt.xlabel('j')
    plt.ylabel('i')
    plt.clim(-wmax,wmax)
    plt.colorbar(fraction=0.045, pad=0.05,ticks=[-wmax,0,wmax])


    plt.subplot2grid((1, 3), (0, 2), colspan=1, rowspan=1)
    plt.plot([-wmax,wmax],[-wmax,wmax],'r--')
    plt.scatter(w0,w)
    plt.title('predicted couplings vs. actual couplings')
    plt.xlabel('$w_{ij}^{true}$')
    plt.ylabel('$w_{ij}^{predicted}$')
    plt.xlim([-wmax,wmax+0.01])
    plt.ylim([-wmax,wmax+0.01])
    plt.xticks(np.arange(-wmax,wmax+0.01,wtick))
    plt.yticks(np.arange(-wmax,wmax+0.01,wtick))

    plt.tight_layout(h_pad=0.5, w_pad=0.5)
    #plt.savefig('w.pdf', format='pdf', dpi=100)
    plt.show()

    MSE = np.mean((w0-w)**2)
    print('MSE:',MSE)
