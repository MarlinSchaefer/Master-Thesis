import matplotlib.pyplot as plt
import numpy as np
import os
from latex_images_path import images_path
from pycbc.waveform import get_td_waveform
from matplotlib import patches
import h5py


def main():
    data_path = '/home/marlin/Documents/Documents/Studium/Masterarbeit/Forschungsphase/Code/Git/master_project/bns_net/saves/inception_res_net_266201913382/inception_res_net_snr_plot_last_epoch_266201913382.hf5'
    
    with h5py.File(data_path, 'r') as FILE:
        x = FILE['x1'][:]
        y = FILE['y'][:]
    
    line = np.linspace(0, 1.1*max(x))
    
    fig = plt.figure(figsize=(1980.0/96, 1080.0/96))
    plt.rcParams.update({'font.size': 32, 'text.usetex': 'true'})
    plt.grid()
    plt.scatter(x, y)
    plt.plot(line, line, color='red', zorder=4)
    plt.xlabel('Label SNR')
    plt.ylabel('Recovered SNR')
    plt.savefig(os.path.join(images_path(), 'streak_plot.png'))
    
    plt.show()
    
    return

main()
