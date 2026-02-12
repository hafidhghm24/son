import scipy.io.wavfile as wav 
import matplotlib.pyplot as plt
import numpy as np
from math import floor


fs, signal = wav.read("son2.wav")

print(f"la frequence dechantillonage est {fs}")

nb_points = len(signal)

print(f"le nombre de canaux est  {nb_points}")

duree = nb_points/fs

print(f"la durée est  {duree}")


print("---extrait---")

extrait = signal[35800:36311]

nb_points_extrait = len(extrait)

#affichage
plt.figure(1)

plt.subplot(3,1,1)
plt.subplot(3,1,1)
plt.xlabel("Temp (second)")
plt.ylabel("Amplitude")
plt.title("extrait signal son2.wav")
plt.plot( (np.arange(nb_points_extrait))/fs , extrait )


print("---FFT de l'extrait---")
#calcule de la FFT
spectre_extrait = abs(np.fft.fft(extrait))
#demi spectre pour eviter la partie symétrique.
demi_spectre = spectre_extrait[0:floor(len(spectre_extrait)/2)]

#affichage
plt.subplot(3,1,2)
plt.plot(((np.arange(len(demi_spectre))))/len(demi_spectre)*fs/2,demi_spectre)
plt.xlabel("frequence (hz)")
plt.ylabel("Amplitude")
plt.title("spectre signal essai.wav")



print("\n--- Calcul du cepstre ---\n")

#on creer une fenetre de hamming
ham = np.hamming(len(extrait))

#on applique la fenetre a lextrait
extrait_ham = np.multiply(extrait, ham)

#spectre de lextrait auquelle on a appliquer hamming
spectre_ham = abs(np.fft.fft(extrait_ham))  # spectre avec Hamming

#calcule du cestre avec le spectre propre
cepstre = abs(np.fft.ifft(np.log(np.maximum(spectre_ham, 1e-10)))) #on met un plt.plot(np.arange(len(cepstre))/fs, cepstre)

plt.subplot(3,1,3)
plt.title("cepstre de l'extrait")
plt.xlabel("quéfrency (s)")
plt.ylabel("amplitude")

plt.show()



print("---QUESTION2---")

fe = 16000
nb_echantillons = fe * 1 # 8000 points = 1 seconde

#creer le silence de 0.1s
silence = np.zeros(nb_echantillons // 10)


# Créer les notes (sinusoïdes)
t = np.arange(nb_echantillons) / fe  # axe temps : [0, 1/8000, 2/8000, ..., 7999/8000]
    
#sin(2pift)
do3  = np.sin(t * 2 * np.pi * 262)   # DO3 = 262 Hz 
mi3  = np.sin(t * 2 * np.pi * 330)   # MI3 = 330 Hz
sol3 = np.sin(t * 2 * np.pi * 392)   # SOL3 = 392 Hz    
la3  = np.sin(t * 2 * np.pi * 440)   # LA3 = 440 Hz
si3  = np.sin(t * 2 * np.pi * 494)   # si3 = 494
do4  = np.sin(t * 2 * np.pi * 523)   # DO4 = 523 Hz
re4  = np.sin(t * 2 * np.pi * 587)   # RE = 587 Hz


# Concaténation
s = np.concatenate((silence, sol3, la3, si3, sol3, la3, silence, la3, si3, do4, silence, do4 ,si3, silence, si3, sol3, la3, si3, sol3, la3, silence, la3, si3, do4, re4, sol3, sol3, silence))


#sauvegarder le fichier
wav.write("melodie_exam.wav", fe, s.astype(np.float32))  # float32 pour les valeurs -1 à +1

print("--- Calcul du spectrogramme ---\n")
    
taille_fenetre = 1024   # w = 1024
pas = 512               # p = 512

# le nombre de fenêtres qu'on peut placer sur le signal
nb_fenetre = (len(s) - taille_fenetre) // pas + 1
    
# tableau de zero pour le silence
sp = np.zeros((taille_fenetre // 2, nb_fenetre))
    
# creation de la enêtre de Hamming 
fenetre_ham = np.hamming(taille_fenetre)
    
for i in range(nb_fenetre):
    p = i * pas                                          # position de début
    segment = signal[p:p + taille_fenetre] * fenetre_ham # découper + fenêtrer de hamming
    spectre = np.fft.fft(segment)                        # FFT
    sp[:, i] = np.abs(spectre[:taille_fenetre // 2])     # demi-spectre, avec sp[:, i] on lajoute a la colonne i
    
#affichage
plt.figure(3)
plt.imshow(
    20 * np.log10(sp + 1e-6),
    extent=[0, len(signal) / fe, 0, fe / 2],
    aspect='auto',
    origin='lower'
)
plt.colorbar(label="Amplitude (dB)")
plt.xlabel("Temps (s)")
plt.ylabel("Fréquence (Hz)")
plt.title("Spectrogramme du signal")
plt.show()