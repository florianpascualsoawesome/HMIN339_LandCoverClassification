#flatten array -> List (coorcoef ne marche qu'avec des listes)
#bands = l'image (200 * 145 * 145)
samples = [np.array(bands[:,:,i]).flatten() for i in range(bands.shape[-1])]

corMat=np.corrcoef(samples)
#corMat : la matrice de corrélation, affichable grâce à :

#import matplotlib.pyplot as plt
plt.imshow(corMat)
plt.show()
