import scipy.io.wavfile as wav 
import matplotlib.pyplot as plt

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
plt.figure(1)
plt.plot(signal) #afficher le signal
plt.show()


