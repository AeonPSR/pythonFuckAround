
produits = {
	1: {'nom': 'Ordi', 'prix': 1200, 'quantite':5},
	2: {'nom': 'Souris', 'prix': 22, 'quantite':0},
	3: {'nom': 'Clavier', 'prix': 130, 'quantite':0},
	4: {'nom': 'Ecran', 'prix': 215, 'quantite':3},
	5: {'nom': 'Disque', 'prix': 130, 'quantite':0}
}
filtered_produits = {key: value for key, value in produits.items() if value['quantite'] == 0}
sort = sorted(filtered_produits.items(), key=lambda x: (-x[1]['prix'], x[0]))
clean = [{id : {'nom': value['nom'], 'prix': value['prix']}} for key, value in sort]

for produit in clean:
	print(produit)