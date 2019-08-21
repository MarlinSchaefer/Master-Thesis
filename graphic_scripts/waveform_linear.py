import matplotlib.pyplot as plt
import numpy as np
import os
from latex_images_path import images_path

def f(x):
    return 3 * x**2 + 2 * x + 1

def g(x):
    return f(x)

def h(x, a):
    return a * x**3 + 3 * x**2 + (2 - a) * x + 1

def rad_to_deg(x):
    return x * 180.0 / np.pi 

def Phi(t, mc, t_coal, phi_coal):
    G = 6.67408 * 10**-11
    c = 3. * 10**8
    return -2. * (5 * G * mc / c**3)**(-5./8.) * (t_coal - t)**(5./8.) + phi_coal

def hp(t, r, mc, t_coal, phi_coal, iota):
    G = 6.67408 * 10**-11
    c = 3. * 10**8
    return 1 / r * (G * mc / c**2)**(5./4.) * (5 / (c * (t_coal - t)))**(1./4.) * ((1 + np.cos(iota)**2) / 2.) * np.cos(Phi(t, mc, t_coal, phi_coal))

def hc(t, r, mc, t_coal, phi_coal, iota):
    G = 6.67408 * 10**-11
    c = 3. * 10**8
    #print("Cos(iota): {}".format(np.cos(iota)))
    #print("Cos(Phi(t)): {}".format(np.cos(Phi(t, mc, t_coal, phi_coal))))
    #print("1/r: {}".format(1 / r))
    #print("Constants: {}".format((G * mc / c**2)**(5./4.)))
    #print("t-part: {}".format((5 / (c * (t_coal - t)))**(1./4.)))
    return 1 / r * (G * mc / c**2)**(5./4.) * (5 / (c * (t_coal - t)))**(1./4.) * np.cos(iota) * np.cos(Phi(t, mc, t_coal, phi_coal))

def F_p(theta, phi):
    return (1 + np.cos(theta)**2) * np.cos(2 * phi) / 2.

def F_c(theta, phi):
    return np.cos(theta) * np.sin(2 * phi)

def detector_response(t, r, mc, t_coal, phi_coal, iota, theta, phi, psi):
    h_p = hp(t, r, mc, t_coal, phi_coal, iota)
    h_c = hc(t, r, mc, t_coal, phi_coal, iota)
    #print('hp = {}'.format(h_p))
    #print('hc = {}'.format(h_c))
    p_part = F_p(theta, phi) * (np.cos(2 * psi) * h_p - np.sin(2 * psi) * h_c)
    c_part = F_c(theta, phi) * (np.sin(2 * psi) * h_p + np.cos(2 * psi) * h_c)
    return p_part + c_part

def f_gw(t, t_coal, mc):
    G = 6.67408 * 10**-11
    c = 3. * 10**8
    return 1 / np.pi * (5 / (256. * (t_coal - t)))**(3./8.) * (G * mc / c**3)**(-5./8.)

def main():
    solar_mass = 2. * 10**30
    m1 = 1.4 * solar_mass
    m2 = 1.4 * solar_mass
    mc = (m1 * m2)**(3. / 5.) / (m1 + m2)**(1. / 5.)
    r = 1000.
    t_coal = 1
    phi_coal = 0
    iota = np.pi / 8
    theta = 0
    phi = 0
    psi = 0
    t_dur = 0.15
    t_max = t_coal - (t_dur / 100.)
    t_from_merger = 0
    
    #print("M_c: {}".format(mc))
    
    num_pts = 10000
    x = np.linspace(t_max - t_dur - t_from_merger, t_max - t_from_merger, num_pts)
    x_disp = np.linspace(0, max(x), num_pts)
    
    #x = np.linspace(0, 0.3, 10000)
    y = np.array([detector_response(t, r, mc, t_coal, phi_coal, iota, theta, phi, psi) for t in x])
    #y = np.array([f_gw(t, t_coal, mc) for t in x])
    
    fig = plt.figure(figsize=(1980.0/96, 1080.0/96))
    plt.rcParams.update({'font.size': 32, 'text.usetex': 'true'})
    
    ax = fig.add_subplot(111)
    ax.plot(x_disp, y, color='black')
    ax.set_ylabel('Strain', rotation=0)
    ax.set_xlabel('t')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_label_coords(1.0, 0.44)
    ax.yaxis.set_label_coords(0.0, 0.9)
    #ax.set_xlim(0, 1.25 * max(x_disp))
    
    plt.savefig(os.path.join(images_path(), 'linear_waveform.png'))
    
    plt.show()
    
    return

main()
