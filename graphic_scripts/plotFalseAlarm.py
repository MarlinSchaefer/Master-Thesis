import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
from latex_images_path import images_path

def main():
    FontSize = 48
    
    results_path = '/home/marlin/Documents/Documents/Studium/Masterarbeit/Forschungsphase/Code/Git/master_project/bns_net/saves/long_data_2/results'
    snrFalseAlarmPath = os.path.join(results_path, 'SNR_200_steps_false_alarm.hf5')
    pFalseAlarmPath = os.path.join(results_path, 'p_score_200_steps_new_log_false_alarm.hf5')
    
    #combinedSnrFalseAlarmPath = os.path.join(results_path, 'combined_snr_100_steps.hf5')
    #combinedPFalseAlarmPath = os.path.join(results_path, 'combined_snr_100_steps.hf5')
    
    #Plot SNR false alarm rate
    dpi = 96
    plt.figure(figsize=(1920.0/dpi, 1440.0/dpi), dpi=dpi)
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    
    with h5py.File(snrFalseAlarmPath, 'r') as f:
        x = f['x'][:]
        y = f['y'][:]
    
    plt.semilogy(x, y, label='Our network')
    plt.xlabel('SNR')
    plt.ylabel('False alarms per month')
    plt.plot([min(x), max(x)], [15500, 15500], color='black', linestyle='dotted', label='Upper limit Krastev', linewidth=2)
    y_low, y_high = plt.ylim()
    plt.ylim(9*10**-1, y_high)
    plt.grid()
    plt.legend()
    plotName = 'FalseAlarmSNR.png'
    plt.savefig(os.path.join(images_path(), plotName))
    plt.show()
    
    #Plot p-score false alarm rate
    dpi = 96
    plt.figure(figsize=(1920.0/dpi, 1440.0/dpi), dpi=dpi)
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    
    with h5py.File(pFalseAlarmPath, 'r') as f:
        x = f['x'][1:]
        y = f['y'][1:]
    
    plt.semilogy(x, y, label='Our network')
    plt.xlabel('p-score')
    plt.ylabel('False alarms per month')
    plt.plot([min(x), max(x)], [15500, 15500], color='black', linestyle='dotted', label='Upper limit Krastev', linewidth=2)
    y_low, y_high = plt.ylim()
    plt.ylim(9*10**-1, y_high)
    plt.grid()
    plt.legend()
    plotName = 'FalseAlarmP.png'
    plt.savefig(os.path.join(images_path(), plotName))
    plt.show()
    
    #Plot p-score false alarm rate 2
    dpi = 96
    plt.figure(figsize=(1920.0/dpi, 1440.0/dpi), dpi=dpi)
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    
    with h5py.File(pFalseAlarmPath, 'r') as f:
        x = -np.log(1-f['x'][1:])
        y = f['y'][1:]
    
    plt.loglog(x, y, label='Our network')
    plt.plot([plt.xlim()[0], plt.xlim()[1]], [15500, 15500], color='black', linestyle='dotted', label='Upper limit Krastev', linewidth=2)
    plt.xlabel('$-\log (1-$p-score$)$')
    plt.ylabel('False alarms per month')
    y_low, y_high = plt.ylim()
    plt.ylim(9*10**-1, y_high)
    plt.grid()
    #plt.ylim(plt.ylim()[0], 100000)
    plt.legend()
    plotName = 'FalseAlarmP2.png'
    plt.savefig(os.path.join(images_path(), plotName))
    plt.show()
    return

main()
