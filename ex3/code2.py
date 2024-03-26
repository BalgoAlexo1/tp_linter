import numpy as np
import matplotlib.pyplot as plt

# Définition de la grille de valeurs pour x et y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calcul de la fonction sin(x) * sin(y)
Z = np.sin(X) * np.sin(Y)

# Création du plot
plt.figure()
plt.contourf(X, Y, Z, cmap='viridis')  # Utilisation de contourf pour le remplissage de couleur
plt.colorbar(label='sin(x) * sin(y)')  # Ajout d'une barre de couleur pour indiquer les valeurs
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot de sin(x) * sin(y)')
plt.grid(True)
plt.show()
