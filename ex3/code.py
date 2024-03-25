import numpy as np
import matplotlib.pyplot as plt

# Définition de l'intervalle des valeurs x
x = np.linspace(0, 10, 400)

# Définition des fonctions sinus en opposition de phase
y1 = np.sin(x)
y2 = np.sin(x + np.pi)  # Décalage de phase de pi radians

# Création de la figure
plt.figure(figsize=(8, 6))

# Tracé des fonctions
plt.plot(x, y1, label='Sinus')
plt.plot(x, y2, label='Sinus décalé de $\pi$ radians')

# Ajout de titres et d'étiquettes
plt.title('Deux fonctions sinus en opposition de phase')
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.legend()

# Sauvegarde de la figure au format png
plt.savefig('sinus_opposition_phase.png')

# Affichage de la figure
plt.show()