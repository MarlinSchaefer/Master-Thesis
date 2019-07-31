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

def main():
    x = np.linspace(-2, 2, 1000)
    y_true = f(x)
    y_para = g(x)
    y_over = h(x, 5)
    x_sample = np.array([-1, 0, 1])
    y_sample = f(x_sample)
    
    #Sets how many parts the figure has
    gridsize = (2, 3)
    #Sets the aspect-ratio of all the small plots
    #0.25 is the part that sets it to have a usual aspect-ratio of 1
    #The factor behind is y / x, (i.e. 3 / 4 for 4:3 final aspect-ratio)
    global_aspect = 0.25 * 10.0 / 16.0
    
    fig = plt.figure(figsize=(1980.0/96, 1080.0/96))
    plt.rcParams.update({'font.size': 22, 'text.usetex': 'true'})
    
    ax1 = plt.subplot2grid(gridsize, (0, 0), rowspan=2)
    ax2 = plt.subplot2grid(gridsize, (0, 1))
    ax3 = plt.subplot2grid(gridsize, (1, 1))
    ax4 = plt.subplot2grid(gridsize, (0, 2))
    ax5 = plt.subplot2grid(gridsize, (1, 2))
    
    #Ground trues
    ax1.set_aspect(global_aspect)
    ax1.spines['left'].set_position('zero')
    ax1.spines['bottom'].set_position('zero')
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    ax1.set_yticks([5, 10, 15])
    ax1.plot(x, y_true, '--', color='black', zorder=1)
    ax1.scatter(x_sample, y_sample, color='red', zorder=2)
    
    #Plot arrow pointing up
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.axis('off')
    x_start = -0.6
    y_start = -0.22 - 0.3
    dx = 2 * 0.6
    dy = 2 * 0.22
    ax2.arrow(x_start, y_start, dx, dy, color='black', width = 0.001, head_width=0.075, length_includes_head=True, head_length=0.15)
    mid_x = x_start + dx / 2
    mid_y = y_start + dy / 2
    ax2.text(mid_x, mid_y, "Quadratic fit", ha='center', va='top', rotation=rad_to_deg(np.arctan(dy / dx)))
    
    #Plot arrow pointing down
    ax3.set_xlim(-1, 1)
    ax3.set_ylim(-1, 1)
    ax3.axis('off')
    x_start = -0.6
    y_start = 0.22 + 0.3
    dx = 2 * 0.6
    dy = -2 * 0.22
    ax3.arrow(x_start, y_start, dx, dy, color='black', width = 0.001, head_width=0.075, length_includes_head=True, head_length=0.15)
    mid_x = x_start + dx / 2
    mid_y = y_start + dy / 2
    ax3.text(mid_x, mid_y, "Cubic fit", ha='center', va='bottom', rotation=rad_to_deg(np.arctan(dy / dx)))
    
    #Parabola regression
    ax4.set_aspect(global_aspect)
    ax4.spines['left'].set_position('zero')
    ax4.spines['bottom'].set_position('zero')
    ax4.spines['right'].set_color('none')
    ax4.spines['top'].set_color('none')
    ax4.set_yticks([5, 10, 15])
    ax4.plot(x, y_para, zorder=1)
    ax4.scatter(x_sample, y_sample, color='red', zorder=2)
    
    #Cubic regression
    ax5.set_ylim(ax4.get_ylim())
    ax5.set_aspect(global_aspect)
    ax5.spines['left'].set_position('zero')
    ax5.spines['bottom'].set_position('zero')
    ax5.spines['right'].set_color('none')
    ax5.spines['top'].set_color('none')
    ax5.set_yticks([5, 10, 15])
    ax5.plot(x, y_true, '--', color='black', zorder=1)
    ax5.plot(x, y_over, zorder=2)
    ax5.scatter(x_sample, y_sample, color='red', zorder=3)
    
    plt.savefig(os.path.join(images_path(), 'overfitting.png'))
    
    plt.show()
    
    return

main()
