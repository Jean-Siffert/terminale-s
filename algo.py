def f(x): return x**2.0 # On définit la fonction qui définit la courbe, ici c'est une fonction carré

a = 0 # Borne inférieure de l'intervalle
b = 2 # Borne supérieure de l'intervalle
n = 100 # Nombre de rectangles
m = [] # Liste des aires des rectangles minorants
M = [] # Liste des aires des rectangles majorants
for x in range(n): # Pour x qui prend chaque valeur de n (nombre de rectangles)
    s = (b-a)/n # On définit la taille du rectangle (Taille de l'intervalle divisé par le nombre de rectangles)
    m.append(s*f(x*s)) # On ajoute à la liste des minorants l'aire du rectangle largeur = s, hauteur = f(x*s)
    M.append(s*f((x+1)*s)) # On ajoute à la liste des majorants l'aire du rectangle largeur = s, hauteur = f((x+1)*s)

minorants = sum(m) # On fait la somme de tous les éléments présents dans la liste des minorants pour avoir l'aire totale
majorants = sum(M) # On fait la somme de tous les éléments présents dans la liste des majorants pour avoir l'aire totale
integrale = (minorants+majorants)/2 # On fait la moyenne des deux
print(integrale) # On affiche le résultat
