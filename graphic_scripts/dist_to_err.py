import numpy as np
import matplotlib.pyplot as plt
from latex_images_path import images_path
import os

def f(x):
    if x >= 1:
        return x**2 * np.exp(-x)
    else:
        return 1 / np.e * (1 / (2 - x))

def dist(x):
    return f(x + 2)

def Err_1(x):
    return 4 / (np.e**2 * dist(x)) - 1

def Err_2(x):
    return Err_1(3 * x)

def loss_c1(x, y):
    #Initialization
    k = 2.2
    k = float(y > 6) * -1.2 + float(y <= 6) * k
    sf = 3
    z = x - y
    
    #Part 1
    part11 = 4 / np.e * sf * z - 1 # y > 6, z > 1
    u = 4 / np.square(2 - sf * (k - 1)) * np.exp(-sf * (k - 1)) - 1 #Err_total(y+k-1,y)
    part12 = 4 / np.e * sf * np.abs(z) + (u - 4 / np.e * sf * (1 - k)) #y>6, z<k-1
    l = 4 / np.square(2- sf * k) * np.exp(-sf * k) - 1 #Err_total(y+k,y)
    d1 = -4 * sf**2 * k * np.exp(-sf * k) / ((2 - sf * k) * (2 - sf * k) * (2 - sf * k))
    d2 = sf * 4 / np.e
    inp = k - z
    a = d2 + d1 - 2 * (u - l)
    b = 3 * (u - l) - 2* d1 - d2
    part13 = a * inp * inp * inp + b * np.square(inp) + d1 * inp + l #smooth_polynomial(-z, -k, u, l, d1, d2)
    part14 = float(sf * z <= 1) * (4 / np.square(2 - sf * z) * np.exp(-sf * z) - 1) + float(sf * z > 1) * part11 #y>6, z\in[k, 1]
    part1 = float(z > 1) * part11 + float(z < k) * (float(z < k - 1) * part12 + float(z >= k - 1) * part13) + float(z <= 1) * float(z >= k) * part14
    
    #Part 2
    part21 = -4 / np.e * sf * z - 1 #y<=6, z<-1
    u = 4 / np.square(2 + sf * k) * np.exp(sf * k) - 1
    part22 = 4 / np.e * sf * z + (u - 4 / np.e * sf * k)
    l = 4 / np.square(2 + sf * (k - 1)) * np.exp(sf * (k - 1)) - 1
    d1 = 4 * sf**2 * (k - 1) * np.exp(sf * (k - 1)) / ((2 + sf * (k - 1)) * (2 + sf * (k - 1)) * (2 + sf * (k - 1)))
    inp = z - k + 1
    a = d2 + d1 - 2 * (u - l)
    b = 3 * (u - l) - 2* d1 - d2
    part23 = a * inp * inp * inp + b * np.square(inp) + d1 * inp + l #smooth_polynomial(-z, -k, u, l, d1, d2)
    part24 = float(sf * z >= -1) * (4 / np.square(2 + sf * z) * np.exp(sf * z) - 1) + float(sf * z < -1) * part21
    part2 = float(z < -1) * part21 + float(z > k - 1) * (float(z > k) * part22 + float(z <= k) * part23) + float(z >= -1) * float(z <= k - 1) * part24
    
    #Return
    return float(y > 6) * part1 + float(y <= 6) * part2

def Err_3(x):
    return loss_c1(x, 0)

def main():
    x = np.linspace(-4, 4, 10000)
    y_1 = np.array([Err_1(pt) for pt in x])
    y_2 = np.array([Err_2(pt) for pt in x])
    y_3 = np.array([Err_3(pt) for pt in x])
    
    gridsize = (6, 3)
    #Sets the aspect-ratio of all the small plots
    #0.25 is the part that sets it to have a usual aspect-ratio of 1
    #The factor behind is y / x, (i.e. 3 / 4 for 4:3 final aspect-ratio)
    global_aspect = 0.25 * 10.0 / 16.0
    
    fig = plt.figure(figsize=(1980.0/96, 1080.0/96))
    plt.rcParams.update({'font.size': 22, 'text.usetex': 'true'})
    
    ax1 = plt.subplot2grid(gridsize, (0, 0), rowspan=5)
    ax2 = plt.subplot2grid(gridsize, (0, 1), rowspan=5)
    ax3 = plt.subplot2grid(gridsize, (0, 2), rowspan=5)
    ax4 = plt.subplot2grid(gridsize, (5, 0))
    ax5 = plt.subplot2grid(gridsize, (5, 1))
    ax6 = plt.subplot2grid(gridsize, (5, 2))
    
    #Plot non squished error
    ax1.plot(x, y_1)
    ax1.grid()
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_xticks([-4, -2, 0, 2, 4])
    
    #Plot squished error
    ax2.plot(x, y_2)
    ax2.grid()
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_xticks([-4, -2, 0, 2, 4])
    
    #Plot squished and cutoff error
    ax3.plot(x, y_3)
    ax3.grid()
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.set_xticks([-4, -2, 0, 2, 4])
    
    #Put label (a)
    ax4.set_xlim(-1, 1)
    ax4.set_ylim(-1, 1)
    ax4.axis('off')
    ax4.text(0, 0, '(a)', ha='center', va='bottom')
    
    #Put label (b)
    ax5.set_xlim(-1, 1)
    ax5.set_ylim(-1, 1)
    ax5.axis('off')
    ax5.text(0, 0, '(b)', ha='center', va='bottom')
    
    #Put label (c)
    ax6.set_xlim(-1, 1)
    ax6.set_ylim(-1, 1)
    ax6.axis('off')
    ax6.text(0, 0, '(c)', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig(os.path.join(images_path(), 'loss_evolution.png'))
    plt.show()
    return

main()
