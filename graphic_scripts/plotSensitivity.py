import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
from latex_images_path import images_path

def main():
    FontSize = 48
    results_path = '/home/marlin/Documents/Documents/Studium/Masterarbeit/Forschungsphase/Code/Git/master_project/bns_net/saves/long_data_2/results'
    snrSensPath = os.path.join(results_path, 'new_SNR_200_steps_sensitivty.hf5')
    pSensPath = os.path.join(results_path, 'p_score_200_steps_new_log_sensitivty.hf5')
    
    #combinedSnrFalseAlarmPath = os.path.join(results_path, 'combined_snr_100_steps.hf5')
    #combinedPFalseAlarmPath = os.path.join(results_path, 'combined_snr_100_steps.hf5')
    
    #Plot sensitivity as range
    dpi = 96
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    fig, ax = plt.subplots(figsize=(1920.0/dpi, 1440.0/dpi), dpi=dpi)
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    
    with h5py.File(snrSensPath, 'r') as f:
        x = f['x'][:]
        y = f['radius'][:]
    
    with h5py.File(pSensPath, 'r') as f:
        x2 = f['x'][1:]
        y2 = f['radius'][1:]
    
    ax.semilogx(x, y, label='SNR', linewidth=3)
    ax.semilogx(x2, y2, label='p-score', linewidth=3)
    ax.set_xlabel('False alarm per month')
    ax.set_ylabel('Sensitive distance in Mpc')
    x_low, x_high = ax.get_xlim()
    ax.set_xlim(x_high, x_low)
    ax.grid()
    ax.legend()
    plotName = 'SensitivitySNR.png'
    plt.savefig(os.path.join(images_path(), plotName))
    plt.show()
    
    #Plot sensitivity as percentage
    dpi = 96
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    fig, ax = plt.subplots(figsize=(1920.0/dpi, 1440.0/dpi), dpi=dpi)
    plt.rcParams.update({'font.size': FontSize, 'text.usetex': 'true'})
    
    with h5py.File(snrSensPath, 'r') as f:
        x = f['x'][:]
        y = f['percentage'][:]
    
    with h5py.File(pSensPath, 'r') as f:
        x2 = f['x'][1:]
        y2 = f['percentage'][1:]
    
    ax.semilogx(x, y, label='SNR', linewidth=3)
    ax.semilogx(x2, y2, label='p-score', linewidth=3)
    ax.set_xlabel('False alarm per month')
    ax.set_ylabel('Ratio of detected signals')
    x_low, x_high = ax.get_xlim()
    ax.set_xlim(x_high, x_low)
    ax.grid()
    ax.legend()
    plotName = 'SensitivityPercentage.png'
    plt.savefig(os.path.join(images_path(), plotName))
    plt.show()
    return

main()
