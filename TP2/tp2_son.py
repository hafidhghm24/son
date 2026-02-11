import numpy as np
import matplotlib.pyplot as plt
from math import *
import scipy.io.wavfile as wav 

def spectro(signal, taille_fenetre, pas):
    # le nombre de fenêtres qu'on peut placer sur le signal
    nb_fenetre = (len(signal) - taille_fenetre) // pas + 1
    
    # tableau de zero pour le silence
    sp = np.zeros((taille_fenetre // 2, nb_fenetre))
    
    # creation de la enêtre de Hamming 
    fenetre_ham = np.hamming(taille_fenetre)
    
    for i in range(nb_fenetre):
        p = i * pas                                          # position de début
        segment = signal[p:p + taille_fenetre] * fenetre_ham # découper + fenêtrer de hamming
        spectre = np.fft.fft(segment)                        # FFT
        sp[:, i] = np.abs(spectre[:taille_fenetre // 2])     # demi-spectre, avec sp[:, i] on lajoute a la colonne i
    
    return sp


def main():
    print("--- Génération d'un signal ---\n")
    
    fe = 8000           # fréquence d'échantillonnage
    nb_echantillons = fe * 1  # 8000 points = 1 seconde (car fe = 8000)

    # Créer un silence de 100ms (que des 0)
    silence = np.zeros(nb_echantillons // 10)  # 8000/10 = 800 points = 0.1s

    # Créer les notes (sinusoïdes)
    t = np.arange(nb_echantillons) / fe  # axe temps : [0, 1/8000, 2/8000, ..., 7999/8000]
    
    #sin(2pift)
    sin_do3  = np.sin(t * 2 * np.pi * 262)   # DO3 = 262 Hz 
    sin_mi3  = np.sin(t * 2 * np.pi * 330)   # MI3 = 330 Hz
    sin_sol3 = np.sin(t * 2 * np.pi * 392)   # SOL3 = 392 Hz
    sin_do4  = np.sin(t * 2 * np.pi * 523)   # DO4 = 523 Hz

    # Concaténation
    s = np.concatenate((silence, sin_do3, silence, sin_mi3, silence, sin_sol3, silence, sin_do4, silence))


    # Affichage avec axe X en secondes
    plt.figure(6)
    plt.plot(np.arange(len(s)) / fe, s) 
    plt.title("Signal mélodique")
    plt.ylabel("Amplitude")            
    plt.xlabel("Temps (s)")
    plt.show()

    wav.write("melodie.wav", fe, s.astype(np.float32))  # float32 pour les valeurs -1 à +1





    print("--- Calcul du spectrogramme ---\n")
    
    taille_fenetre = 1024   # w = 1024
    pas = 512               # p = 512
    
    spectroM = spectro(s, taille_fenetre, pas)
    
    duree_melodie = len(s) / fe
    freq_max = fe / 2       # Shannon : 8000/2 = 4000 Hz
    
    plt.figure(7)
    plt.imshow(
        20 * np.log10(spectroM + 1e-6),               # en dB 
        extent=[0, duree_melodie, 0, freq_max],        # bornes des axes
        aspect='auto',
        origin='lower'                                  # 0 Hz en bas
    )
    plt.colorbar(label="Amplitude (dB)")
    plt.xlabel("Temps (s)")
    plt.ylabel("Fréquence (Hz)")
    plt.title("Spectrogramme du signal")
    plt.show()

    print("--- Triangle vocalique ---\n")


main()