import matplotlib.pyplot as plt
import numpy as np
import os
from latex_images_path import images_path
from pycbc.waveform import get_td_waveform
from matplotlib import patches


def main():
    approximant = 'TaylorF2'
    mass1 = 1.4
    mass2 = 1.4
    delta_t = 1.0 / 4096
    f_lower = 20
    final_x_sec = 68
    
    hp, hc = get_td_waveform(approximant=approximant, mass1=mass1, mass2=mass2, delta_t=delta_t, f_lower=f_lower)
    
    dur = hp.sample_times[-1]
    
    hp = hp.time_slice(dur - final_x_sec - hp.delta_t, dur)
    
    x = hp.sample_times
    
    y = hp.data[:]
    
    box_height = 1.1 * max(abs(y))
    
    print("Duration: {}".format(hp.duration))
    print("Length y: {}".format(len(y)))
    
    fig = plt.figure(figsize=(1980.0/96, 1080.0/96))
    plt.rcParams.update({'font.size': 32, 'text.usetex': 'true'})
    
    ax = fig.add_subplot(111)
    lw = 2
    separate = 0.25
    
    window_size = 0.5
    left_edge = dur - window_size
    rect_1s_1 = patches.Rectangle((left_edge + separate / 2, - box_height), window_size - separate / 2, 2 * box_height, linewidth=lw, edgecolor='black', facecolor='none', zorder=4)
    ax.add_patch(rect_1s_1)
    
    window_size = 0.5
    left_edge -= window_size
    rect_1s_2 = patches.Rectangle((left_edge + separate / 2, - box_height), window_size - separate / 2, 2 * box_height, linewidth=lw, edgecolor='purple', facecolor='none', zorder=4)
    ax.add_patch(rect_1s_2)
    
    window_size = 1.0
    left_edge -= window_size
    rect_2s = patches.Rectangle((left_edge + separate / 2, - box_height), window_size - separate / 2, 2 * box_height, linewidth=lw, edgecolor='blue', facecolor='none', zorder=4)
    ax.add_patch(rect_2s)
    
    window_size = 2.0
    left_edge -= window_size
    rect_4s = patches.Rectangle((left_edge + separate / 2, - box_height), window_size - separate / 2, 2 * box_height, linewidth=lw, edgecolor='cyan', facecolor='none', zorder=4)
    ax.add_patch(rect_4s)
    
    window_size = 4.0
    left_edge -= window_size
    rect_8s = patches.Rectangle((left_edge + separate / 2, - box_height), window_size - separate / 2, 2 * box_height, linewidth=lw, edgecolor='green', facecolor='none', zorder=4)
    ax.add_patch(rect_8s)
    
    window_size = 8.0
    left_edge -= window_size
    rect_16s = patches.Rectangle((left_edge + separate / 2, - box_height), window_size - separate / 2, 2 * box_height, linewidth=lw, edgecolor='yellow', facecolor='none', zorder=4)
    ax.add_patch(rect_16s)
    
    window_size = 16.0
    left_edge -= window_size
    rect_32s = patches.Rectangle((left_edge + separate / 2, - box_height), window_size - separate / 2, 2 * box_height, linewidth=lw, edgecolor='magenta', facecolor='none', zorder=4)
    ax.add_patch(rect_32s)
    
    window_size = 32.0
    left_edge -= window_size
    rect_64s = patches.Rectangle((left_edge + separate / 2, - box_height), window_size - separate / 2, 2 * box_height, linewidth=lw, edgecolor='red', facecolor='none', zorder=4)
    ax.add_patch(rect_64s)
    
    ax.plot(x, y)
    
    #ax.set_ylabel('Strain', rotation=0)
    ax.set_xlabel('t in s')
    ax.set_yticklabels([])
    ax.set_yticks([])
    ax.xaxis.set_label_coords(1.05, 0)
    #ax.yaxis.set_label_coords(0.05, 0.9)
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_ylim((-1.2 * max(abs(y)), 1.2 * max(abs(y))))
    
    plt.savefig(os.path.join(images_path(), 'multirate_filtering.png'))
    
    plt.show()
    
    return

main()
