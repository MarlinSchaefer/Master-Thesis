import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
from latex_images_path import image_path

def main():
    results_path = '/home/marlin/Documents/Documents/Studium/Masterarbeit/Forschungsphase/Code/Git/master_project/bns_net/saves/long_data_2/results'
    snrFalseAlarmPath = os.path.join(results_path, 'SNR_200_steps_false_alarm.hf5')
    pFalseAlarmPath = os.path.join(results_path, 'new_p_score_200_steps_false_alarm.hf5')
    #combinedSnrFalseAlarmPath = os.path.join(results_path, 'combined_snr_100_steps.hf5')
    #combinedPFalseAlarmPath = os.path.join(results_path, 'combined_snr_100_steps.hf5')
    return

main()
