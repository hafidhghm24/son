import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import canaux as MEL
from math import floor

#PAGE 7
fs, signal = wav.read('essai.wav')
print("Fréquence d'échantillonnage : ", fs, " Hz")

print("Valeurs du signal : ", signal[:10]) # Signal est un tableau contenant l'amplitude du signal à chaque instant
duree_intervalle = 1/fs
print("Intervalle de temps entre deux échantillons : ", duree_intervalle, " secondes")

duree_totale = len(signal)/fs
print("Durée totale du signal : ", duree_totale, " secondes")

#PAGE 9

abscisses_temporel = np.arange(0, len(signal))*duree_intervalle

plt.figure(2)
plt.plot(abscisses_temporel,signal)
plt.show()

#PAGE 11 
# SIGNAL NOTE
fs_note , signal_note = wav.read('note.wav')
plt.figure(3)
abscisses_temporel_note = np.arange(0, len(signal_note))* (1/fs_note)
duree_totale_note = len(signal_note)/fs_note
print("Durée totale du signal note.wav : ", duree_totale_note, " secondes")


abscisses_freq_note = np.arange(0, len(signal_note)) * (fs_note/len(signal_note))
spectre_note = abs(np.fft.fft(signal_note))

plt.subplot(2,1,1)
plt.plot(abscisses_temporel_note,signal_note)
plt.subplot(2,1,2)
plt.plot(abscisses_freq_note,spectre_note)
plt.show()
print("Valeur du pic du spectre : ", max(spectre_note))
for i in range(len(spectre_note)):
    if spectre_note[i] == max(spectre_note):
        print("Fréquence du pic du spectre : ", i*fs_note/len(spectre_note), " Hz, cela resprésente la note La 440 Hz")
        break 


# SIGNAL PAROLE 1024 POINTS
signal_1024p = signal[11300:11300+1024]
abscisses_temporel_1024p = np.arange(0, len(signal_1024p))*(1/fs)
abscisses_freq_1024p = np.arange(0, len(signal_1024p))*(fs/len(signal_1024p))
spectre_1024p = abs(np.fft.fft(signal_1024p))

spectre = abs(np.fft.fft(signal))
plt.figure(5)
plt.subplot(2,1,1)
plt.plot(abscisses_temporel_1024p,signal_1024p)
plt.subplot(2,1,2)
plt.plot(abscisses_freq_1024p[:512],spectre_1024p[:512])
plt.show()

#PAGE 12

# Signal 1024 points
plt.subplot(5,1,1)
plt.plot(signal_1024p)

# Fenêtre de Hamming
plt.subplot(5,1,2)
ham1024 = np.hamming(len(signal_1024p))
plt.plot(ham1024)

# Signal 1024 points * fenêtre de Hamming
plt.subplot(5,1,3)
extrait_ham1024 = np.multiply(signal_1024p, ham1024)
plt.plot(extrait_ham1024)

# Spectre du signal 1024 points
plt.subplot(5,1,4)
plt.plot(spectre_1024p[:512])

# Spectre du signal 1024 points * fenêtre de Hamming
plt.subplot(5,1,5)
spectre_f_ham1024 = abs(np.fft.fft(extrait_ham1024))
plt.plot(spectre_f_ham1024[:512])
plt.show()

#PAGE 14
plt.specgram(signal, Fs = fs, window=ham1024, NFFT=1024)
plt.title("Spectrogramme de 0 3 8 et 0")
plt.ylabel("Fréquence (Hz)")
plt.xlabel("Temps (s)")
plt.show() 

#PAGE 16
MEL.canaux(signal_1024p, fs, 26) #échelle psychoacoustique de hauteurs des sons, au sens de leur repérage entre grave et aigu, dont l'unité est le mel

#PAGE 18 Calcul du cepstre
cepstre = abs(np.fft.fft(np.log(spectre_1024p)))

plt.figure(7)
plt.subplot(3,1,1)
plt.suptitle("Signal temporel")
plt.plot(abscisses_temporel_1024p,signal_1024p)
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")

plt.subplot(3,1,2)
plt.title("Spectre fréquentiel")
plt.plot(abscisses_freq_1024p[:512],spectre_1024p[:512])
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")

plt.subplot(3,1,3)
plt.title("Cepstre")
plt.plot(abscisses_temporel_1024p[:512],cepstre[:512])
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()