import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

# fréquence d'échantillonnage
fe = 8000  

#on fabrique le son
def generate_sine_wave(frequence, duree, fe):
    n = np.arange(int(duree * fe))
    return np.sin(2 * np.pi * frequence * n / fe)

duree_note = 1.0     # une note en seconde
duree_silence = 0.1  # un silence en seconde

silence = np.zeros(int(duree_silence * fe))

do3  = generate_sine_wave(262, duree_note, fe)
mi3  = generate_sine_wave(330, duree_note, fe)
sol3 = generate_sine_wave(392, duree_note, fe)
do4  = generate_sine_wave(523, duree_note, fe)


signal = np.concatenate((
    silence, do3,
    silence, mi3,
    silence, sol3,
    silence, do4,
    silence
))

temps = np.arange(len(signal)) / fe

#affichage
plt.figure()
plt.plot(temps, signal)
plt.title("Signal sonore")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

#sauvegarde de laudio
wav.write("musique.wav", fe, signal.astype(np.float32))

#creation du spectrogramme
def spectro(signal, taille_fenetre, pas):
    nb_fen = (len(signal) - taille_fenetre) // pas + 1
    spec = np.zeros((taille_fenetre // 2, nb_fen))

    fenetre_hann = np.hanning(taille_fenetre)

    for i in range(nb_fen):
        p = i * pas
        segment = signal[p:p + taille_fenetre] * fenetre_hann
        spectre = np.fft.fft(segment)
        spec[:, i] = np.abs(spectre[:taille_fenetre // 2])

    return spec

sp = spectro(signal, 1024, 512)

#affichage
plt.figure()
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
