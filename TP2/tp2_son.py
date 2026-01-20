import numpy as np
import matplotlib.pyplot as plt
from math import *
import scipy.io.wavfile as wav 

def spectro(signal, taille_fenetre, pas):




def main():
    print("--- Génération d'un signal ---\n")
    #generer un signal S decrivent la melodie [Silence] [DO3] [Silence] [MI3] [Silence] [SOL3] [Silence] [DO4] [Silence].
    nb_echentillons = 8000

    fe = 8000

    #creer Un [Silence] (100ms) (que des 0)
    silence = np.zeros((nb_echentillons//10))

    #creer Un [DO3] (262 Hz)
    fs_do3 = 262
    do3  = np.arange(nb_echentillons)/fe #[0:8000]/Fe
    sin_do3= np.sin(do3 * (2*np.pi) * fs_do3) #on aurra un sinus entre 0 et 1 composer de 8000 ptns

    #creer Un [MI3] (330 Hz)
    fs_mi3 = 330
    mi3  = np.arange(nb_echentillons)/fe
    sin_mi3 = np.sin(mi3 * (2*np.pi) * fs_mi3)

    #creer Un [SOL3] (392 Hz)
    fs_sol3 = 392
    sol3 = np.arange(nb_echentillons)/fe
    sin_sol3 = np.sin(sol3 * (2*np.pi) * fs_sol3)

    #creer Un [DO4] (523 Hz)
    fs_do4 = 523
    do4  = np.arange(nb_echentillons)/fe
    sin_do4 = np.sin(do4 * (2*np.pi) * fs_do4)

    #concatenation
    s = np.concatenate((silence, sin_do3, silence, sin_mi3, silence, sin_sol3, silence, sin_do4))

    plt.figure(6)
    plt.plot(s)
    plt.title("signal concater")
    plt.ylabel("Fréquence (Hz)")
    plt.xlabel("Temps (s)")
    plt.show()

    wav.write("melodie.wav", fe, s)


    print("--- Calcul du spectrogramme ---\n")
    sp = np.zeros(recouvrement, nb_fenetre)
    for (fenetre in range (nb_fenetre)): #nombre de fenetre correspond a la taille du fichier
        p = 
        spectre = 
    sp[:,fenetre]

    duree_melodie= 
    freq_max= fe/2
    spectroM = spectro(signal, taille_fentre, pas)
    imshow(spectroM, extent=[0,duree_melodie, 0, freq_max])
    print("--- Triangle vocalique ---\n")

