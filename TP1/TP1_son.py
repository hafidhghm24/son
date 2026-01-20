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

#extrait du signal  essai.wav
extrait = signal[11300:(11300+1024)]

#nombre de points de lextrait
nb_points = len(extrait)

plt.subplot(2,2,3)
plt.plot( (np.arange(nb_points))/fs , extrait )
plt.xlabel("Temp (second)")
plt.ylabel("Amplitude")
plt.title("signal essai.wav")

spectre_s1 = abs(np.fft.fft(extrait))
plt.subplot(2,2,4)

#on divise le spectre par deux
demi_spectre = spectre_s1[0:floor(len(spectre_s1)/2)] #floor pour prendre les partie entirer

plt.plot(((np.arange(len(demi_spectre))))/len(demi_spectre)*fs/2,demi_spectre)
plt.xlabel("frequence (hz)")
plt.ylabel("Amplitude")
plt.title("spectre signal essai.wav")
plt.show()

print("\n--- CALCULE DU SPECTRE ET FENETRE DE HAMMING ---\n")
plt.figure(4)
plt.subplot(5,1,1)
#EXPLICATION: 

#1er  tracer:   cest l'éxtrait du signal essai.wav
plt.plot(extrait)
plt.subplot(5,1,2)

#2eme tracer:   cest la fenetre de hamming avec le meme nombre de point que l'éxtrait
ham1024 = np.hamming(len(extrait))
plt.plot(ham1024)
plt.subplot(5,1,3)


#3eme tracer:   cest on as multiplier le 1erx2eme et de ce fait on a appliquer la fenetre de hamming sur l'éxtrait
extrait_ham1024 = np.multiply(extrait, ham1024)
plt.plot(extrait_ham1024)
plt.subplot(5,1,4)

#4eme tracer: (avant le hamming) cest le spectre de lextrait  limiter a 512 points 
spectre_f = abs(np.fft.fft(extrait))
plt.plot(spectre_f[:512])
plt.subplot(5,1,5)

#5eme tracer: (apres le hamming) cest le spectre de lextrait  limiter a 512 points 

spectre_f_ham1024 = abs(np.fft.fft(extrait_ham1024))
plt.plot(spectre_f_ham1024[:512])
plt.show()

#fenetre de hamming cest .... son interet cest ....
#les autres fenetres: 

print("\n--- SPECTROGRAMME DU SIGNAL ---\n")

plt.figure(5)
plt.specgram(signal, Fs=fs, window=ham1024, NFFT=1024)
plt.title("Spectrogramme de 0 3 8 et 0")
plt.ylabel("Fréquence (Hz)")
plt.xlabel("Temps (s)")
plt.show()
#on remarque que ....


print("\n --- Echelle MEL ---\n")

import canaux as MEL
MEL.canaux(extrait, 16000, 26)
#1er tracer: lextrait 
#2eme tracer: spectre de lextrait
#3eme tracer: ça regroupe toute les valeur denergie (les plus faible deviene plus grand yen as plus de cumuler comparer au pick ou cest plus faible)


print("\n--- Calcul du cepstre ---\n")

#calcule du cepstre: on fait le log du spectre 
cepstre = abs(np.fft.fft(np.log(spectre_s1)))
plt.figure(6)
plt.plot( (np.arange(nb_points))/fs , cepstre )
plt.title("cpestre de lextrait")
plt.ylabel("Fréquence (Hz)")
plt.xlabel("Temps (s)")
plt.show()
