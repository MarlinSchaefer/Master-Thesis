import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
from latex_images_path import images_path

def main():
    FontSize = 48
    
    results_path = '/home/marlin/Documents/Documents/Studium/Masterarbeit/Forschungsphase/Code/Git/master_project/bns_net/saves/long_data_2/results'
    snrSensPath = os.path.join(results_path, 'combined_steps_P_log_scale_SNR_sensitivity.hf5')
    pSensPath = os.path.join(results_path, 'combined_steps_P_log_scale_sensitivity.hf5')
    
    #combinedSnrFalseAlarmPath = os.path.join(results_path, 'combined_snr_100_steps.hf5')
    #combinedPFalseAlarmPath = os.path.join(results_path, 'combined_snr_100_steps.hf5')
    
    #Plot SNR sensitivity as range
    with h5py.File(snrSensPath, 'r') as f:
        x = f['snr'][:]
        y = f['p-score'][:]
        z = f['radius'][:]
        fa = f['xy'][:]
        per = f['percentage'][:]
        
    shape = (int(np.sqrt(len(x))), int(np.sqrt(len(x))))
    x = x.reshape(shape)
    y = y.reshape(shape)
    z = z.reshape(shape)
    fa = fa.reshape(shape)
    per = per.reshape(shape)
    
    snr = x[0]
    p = y.transpose()[0]
    
    dpi = 96
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    fig, ax = plt.subplots(figsize=(1920.0/dpi, 1440.0/dpi), dpi=dpi)
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    
    ps = [0.408, 0.5, 0.75, 0.95]
    colors = ['blue', 'red', 'green', 'black']
    for i, pt in enumerate(ps):
        minIdx = np.argmin(np.abs(p - pt))
        lab = p[minIdx]
        ax.semilogx(fa[minIdx], z[minIdx], label='p-score: %.2f' % lab, color=colors[i])
    ax.set_xlabel('False alarms per month')
    ax.set_ylabel('Sensitive distance in Mpc')
    x_low, x_high = ax.get_xlim()
    ax.set_xlim(x_high, x_low)
    #plt.plot([min(snr), max(snr)], [15500, 15500], color='black', linestyle='dotted', label='Upper limit Krastev', linewidth=2)
    ax.grid()
    ax.legend()
    plotName = 'CombinedSensitivitySNR.png'
    plt.savefig(os.path.join(images_path(), plotName))
    plt.show()
    
    #Plot SNR percentages
    dpi = 96
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    fig, ax = plt.subplots(figsize=(1920.0/dpi, 1440.0/dpi), dpi=dpi)
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    for i, pt in enumerate(ps):
        minIdx = np.argmin(np.abs(p - pt))
        lab = p[minIdx]
        ax.semilogx(fa[minIdx], per[minIdx], label='p-score: %.2f' % lab, color=colors[i])
    ax.set_xlabel('False alarms per month')
    ax.set_ylabel('Ratio of detected signals')
    x_low, x_high = ax.get_xlim()
    ax.set_xlim(x_high, x_low)
    #plt.plot([min(snr), max(snr)], [15500, 15500], color='black', linestyle='dotted', label='Upper limit Krastev', linewidth=2)
    ax.grid()
    ax.legend()
    plotName = 'CombinedSensitivityPercentageSNR.png'
    plt.savefig(os.path.join(images_path(), plotName))
    plt.show()
    
    #Plot p-score sensitivity as range
    with h5py.File(snrSensPath, 'r') as f:
        x = f['snr'][:]
        y = f['p-score'][:]
        z = f['radius'][:]
        fa = f['xy'][:]
        per = f['percentage'][:]
        
    shape = (int(np.sqrt(len(x))), int(np.sqrt(len(x))))
    x = x.reshape(shape)
    y = y.reshape(shape)
    z = z.reshape(shape)
    fa = fa.reshape(shape)
    per = per.reshape(shape)
    
    snr = x[0]
    p = y.transpose()[0]
    
    dpi = 96
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    fig, ax = plt.subplots(figsize=(1920.0/dpi, 1440.0/dpi), dpi=dpi)
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    
    snrs = [4, 6.7, 8, 15]
    colors = ['blue', 'red', 'green', 'black']
    for i, pt in enumerate(snrs):
        minIdx = np.argmin(np.abs(snr - pt))
        lab = snr[minIdx]
        ax.semilogx(fa.transpose()[minIdx], z.transpose()[minIdx], label='SNR: %.2f' % lab, color=colors[i])
    ax.set_xlabel('False alarms per month')
    ax.set_ylabel('Sensitive distance in Mpc')
    x_low, x_high = ax.get_xlim()
    ax.set_xlim(x_high, x_low)
    #plt.plot([min(snr), max(snr)], [15500, 15500], color='black', linestyle='dotted', label='Upper limit Krastev', linewidth=2)
    ax.grid()
    ax.legend()
    plotName = 'CombinedSensitivityP.png'
    plt.savefig(os.path.join(images_path(), plotName))
    plt.show()
    
    #Plot p-score percentages
    dpi = 96
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    fig, ax = plt.subplots(figsize=(1920.0/dpi, 1440.0/dpi), dpi=dpi)
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    for i, pt in enumerate(snrs):
        minIdx = np.argmin(np.abs(snr - pt))
        lab = snr[minIdx]
        ax.semilogx(fa.transpose()[minIdx], per.transpose()[minIdx], label='SNR: %.2f' % lab, color=colors[i])
    ax.set_xlabel('False alarms per month')
    ax.set_ylabel('Ratio of detected signals')
    x_low, x_high = ax.get_xlim()
    ax.set_xlim(x_high, x_low)
    #plt.plot([min(snr), max(snr)], [15500, 15500], color='black', linestyle='dotted', label='Upper limit Krastev', linewidth=2)
    ax.grid()
    ax.legend()
    plotName = 'CombinedSensitivityPercentageP.png'
    plt.savefig(os.path.join(images_path(), plotName))
    plt.show()
    
    return

main()
