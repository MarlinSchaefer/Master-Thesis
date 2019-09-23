import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
from latex_images_path import images_path

def main():
    FontSize = 48
    
    results_path = '/home/marlin/Documents/Documents/Studium/Masterarbeit/Forschungsphase/Code/Git/master_project/bns_net/saves/long_data_2/results'
    snrFalseAlarmPath = os.path.join(results_path, 'combined_steps_P_log_scale_SNR_false_alarm.hf5')
    pFalseAlarmPath = os.path.join(results_path, 'combined_steps_P_log_scale_false_alarm.hf5')
    
    #combinedSnrFalseAlarmPath = os.path.join(results_path, 'combined_snr_100_steps.hf5')
    #combinedPFalseAlarmPath = os.path.join(results_path, 'combined_snr_100_steps.hf5')
    
    #Plot SNR false alarm rate
    dpi = 96
    plt.figure(figsize=(1920.0/dpi, 1440.0/dpi), dpi=dpi)
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    
    with h5py.File(snrFalseAlarmPath, 'r') as f:
        x = f['x'][:]
        y = f['y'][:]
        z = f['z'][:]
    
    shape = (int(np.sqrt(len(x))), int(np.sqrt(len(x))))
    x = x.reshape(shape)
    y = y.reshape(shape)
    z = z.reshape(shape)
    
    snr = x[0]
    p = y.transpose()[0]
    
    ps = [0.408, 0.5, 0.75, 0.95]
    colors = ['blue', 'red', 'green', 'black']
    for i, pt in enumerate(ps):
        minIdx = np.argmin(np.abs(p - pt))
        lab = p[minIdx]
        plt.semilogy(x[0], z[minIdx], label='p-score: %.2f' % lab, color=colors[i])
    plt.xlabel('SNR')
    plt.ylabel('False alarms per month')
    #plt.plot([min(snr), max(snr)], [15500, 15500], color='black', linestyle='dotted', label='Upper limit Krastev', linewidth=2)
    plt.grid()
    plt.legend()
    plotName = 'CombinedFalseAlarmSNR.png'
    plt.savefig(os.path.join(images_path(), plotName))
    plt.show()
    
    #Plot p-score false alarm rate
    dpi = 96
    plt.figure(figsize=(1920.0/dpi, 1440.0/dpi), dpi=dpi)
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    
    with h5py.File(pFalseAlarmPath, 'r') as f:
        x = f['x'][:]
        y = f['y'][:]
        z = f['z'][:]
    
    shape = (int(np.sqrt(len(x))), int(np.sqrt(len(x))))
    x = x.reshape(shape)
    y = y.reshape(shape)
    z = z.reshape(shape)
    
    snr = x[0]
    p = y.transpose()[0]
    
    snrs = [4, 6.7, 8, 15]
    colors = ['blue', 'red', 'green', 'black']
    for i, pt in enumerate(snrs):
        minIdx = np.argmin(np.abs(snr - pt))
        lab = snr[minIdx]
        plt.semilogy(y.transpose()[0], z.transpose()[minIdx], label='SNR: %.2f' % lab, color=colors[i])
    plt.xlabel('p-score')
    plt.ylabel('False alarms per month')
    #plt.plot([min(p), max(p)], [15500, 15500], color='black', linestyle='dotted', label='Upper limit Krastev', linewidth=2)
    plt.grid()
    plt.legend()
    plotName = 'CombinedFalseAlarmP.png'
    plt.savefig(os.path.join(images_path(), plotName))
    plt.show()
    
    #Plot p-score false alarm rate 2
    dpi = 96
    plt.figure(figsize=(1920.0/dpi, 1440.0/dpi), dpi=dpi)
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    
    with h5py.File(pFalseAlarmPath, 'r') as f:
        x = f['x'][:]
        y = -np.log(1-f['y'][:])
        z = f['z'][:]
    
    shape = (int(np.sqrt(len(x))), int(np.sqrt(len(x))))
    x = x.reshape(shape)
    y = y.reshape(shape)
    z = z.reshape(shape)
    
    snr = x[0]
    p = y.transpose()[0]
    
    snrs = [4, 6.7, 8, 15]
    colors = ['blue', 'red', 'green', 'black']
    for i, pt in enumerate(snrs):
        minIdx = np.argmin(np.abs(snr - pt))
        lab = snr[minIdx]
        plt.loglog(y.transpose()[0], z.transpose()[minIdx], label='SNR: %.2f' % lab, color=colors[i])
    plt.xlabel('$-\log (1-$p-score$)$')
    plt.ylabel('False alarms per month')
    #plt.plot([min(p), max(p)], [15500, 15500], color='black', linestyle='dotted', label='Upper limit Krastev', linewidth=2)
    plt.grid()
    plt.legend()
    plotName = 'CombinedFalseAlarmP2.png'
    plt.savefig(os.path.join(images_path(), plotName))
    plt.show()
    
    ##Plot p-score false alarm rate 2
    #dpi = 96
    #plt.figure(figsize=(1920.0/dpi, 1440.0/dpi), dpi=dpi)
    #plt.rcParams.update({'font.size': 32, 'text.usetex': 'true'})
    
    #with h5py.File(pFalseAlarmPath, 'r') as f:
        #x = -np.log(1-f['x'][1:])
        #y = f['y'][1:]
    
    #plt.loglog(x, y, label='Our network')
    #plt.plot([plt.xlim()[0], plt.xlim()[1]], [15500, 15500], color='black', linestyle='dotted', label='Upper limit Krastev', linewidth=2)
    #plt.xlabel('$-\log (1-$p-score$)$')
    #plt.ylabel('False alarms per month')
    #plt.grid()
    ##plt.ylim(plt.ylim()[0], 100000)
    #plt.legend()
    #plotName = 'CombinedFalseAlarmP2.png'
    #plt.savefig(os.path.join(images_path(), plotName))
    #plt.show()
    return

main()
