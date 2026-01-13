import scipy.io.wavfile as wav 
import matplotlib.pyplot as plt
import numpy as np
from math import floor

#lire le fichier audio
fs, signal = wav.read("essai.wav")

#signal : cest un vecteur qui contien tout les points du signal
#fs     : cest la frequence d'échantillonage (16000hz)

print("\n--- AFFICHAGE DES VALEURS ---\n")
print(f"la valeur du signal : ", signal, "\n")
print(f"la valeur de fs : ", fs)

print("\naffichage des 10 premiéres valeurs de signal")
print(signal[0:10])

#lintervale depend du nombre de bit de quantification (ici 16)
print(f"\navec 16bits de quantification l'intervalle est : [{min(signal)} , {max(signal)}]")

print("\n--- AFFICHAGE DU SIGNAL AUDIO ---\n")
#plt.figure(1)
#plt.plot(signal) #afficher le signal
#plt.xlabel("Temp (second)")
#plt.ylabel("Amplitude")
#plt.show()

nb_points = len(signal)
durée = (nb_points * 1)/fs

print(f"\nla durée du signal (en secondes) est: {durée}")

#afficher avec la durée du signal en seconde
#plt.figure(2)
#plt.plot( (np.arange(nb_points))/fs , signal ) #preciser les abscisses
#plt.xlabel("Temp (second)")
#plt.ylabel("Amplitude")
#plt.title("signal essai.wav")
#plt.show()

print("\n--- SIGNAL & SPECTRE ---\n")
#charger le fichier 
fs2, signal2 = wav.read("note.wav")
nb_points2 = len(signal2)
plt.figure(3)
plt.subplot(2,2,1)
plt.xlabel("Temp (second)")
plt.ylabel("Amplitude")
plt.title("signal note.wav")
plt.plot( (np.arange(nb_points2))/fs2 , signal2 ) #abcisses en seconds
plt.subplot(2,2,2)
spectre_s2 = abs(np.fft.fft(signal2))
plt.plot((np.arange(len(spectre_s2)))/len(spectre_s2)*fs2,spectre_s2)
plt.xlabel("frequence (hz)")
plt.ylabel("Amplitude")
plt.title("spectre signal note.wav")

#en zooment sur la seul valeur differente de 0, on trouve la frequence de la note (le seul pic) a 440hz 
#il sagit de la note : la

plt.subplot(2,2,3)
plt.plot( (np.arange(nb_points))/fs , signal )
plt.xlabel("Temp (second)")
plt.ylabel("Amplitude")
plt.title("signal essai.wav")

spectre_s1 = abs(np.fft.fft(signal[11300:(11300+1024)]))
plt.subplot(2,2,4)

#on divise le spectre par deux
demi_spectre = spectre_s1[0:floor(len(spectre_s1)/2)] #floor pour prendre les partie entirer

plt.plot(((np.arange(len(demi_spectre))))/len(demi_spectre)*fs,demi_spectre)
plt.xlabel("frequence (hz)")
plt.ylabel("Amplitude")
plt.title("spectre signal essai.wav")
plt.show()










