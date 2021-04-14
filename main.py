# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    # donner la database
lisaDB = client['supermarche']
produit = lisaDB['produit']
commande = lisaDB['commande']
InventaireProduit = lisaDB['inventaireProduit']
caisse = lisaDB['caisse']

InventaireProduit1 = {"_id": "1",
                      "Quantité": 150}
InventaireProduit2 = {"_id": "2",
                      "Quantite": 50}
InventaireProduit3 = {"_id": "3",
                      "Quantite": 70}
InventaireProduit4 = {"_id": "4",
                      "Quantite": 80}
InventaireProduit5 = {"_id": "5",
                      "Quantite": 100}

produit1 = {"_id": "1", "Nom_Produit": "chips", "Description": "Bio Paprika", "Quantite": [InventaireProduit1]}
produit2 = {"_id": "2", "Nom_Produit": "bonbons", "Description": "Sucre Haribo", "Quantite": [InventaireProduit2]}
produit3 = {"_id": "3", "Nom_Produit": "salade", "Description": "Bio Origine France", "Quantite": [InventaireProduit3]}
produit4 = {"_id": "4", "Nom_Produit": "viande", "Description": "Boeuf Origine France", "Quantite": [InventaireProduit4]}
produit5 = {"_id": "5", "Nom_Produit": "fromage", "Description": "Emmental Origine France", "Quantite": [InventaireProduit5]}

commande1 = {"_id": "1", "Contenu": [produit1, produit5], "Date": '14/04/2021'}
commande2 = {"_id": "2", "Contenu": [produit2, produit4], "Date": '13/04/2021'}
commande3 = {"_id": "3", "Contenu": [produit3, produit1, produit3], "Date": '12/04/2021'}
commande4 = {"_id": "4", "Contenu": [produit1, produit3, produit5], "Date": '11/04/2021'}

caisse1 = {"_id": "1", "Commande": [commande1, commande4]}
caisse2 = {"_id": "2", "Commande": [commande3, commande2]}


#insertion des produits

"""x1 = produit.insert_one(produit1)
x2 = produit.insert_one(produit2)
x3 = produit.insert_one(produit3)
x4 = produit.insert_one(produit4)
x5 = produit.insert_one(produit5)

print(x1)
print(x2)
print(x3)
print(x4)
print(x5)"""

#insertion des commandes

"""x1 = commande.insert_one(commande1)
x2 = commande.insert_one(commande2)
x3 = commande.insert_one(commande3)
x4 = commande.insert_one(commande4)

print(x1)
print(x2)
print(x3)
print(x4)"""

#insertion des caisses

"""x1 = caisse.insert_one(caisse1)
x2 = caisse.insert_one(caisse2)
print(x1)
print(x2)"""

#insertion des inventaires produits

"""x1 = InventaireProduit.insert_one(InventaireProduit1)
x2 = InventaireProduit.insert_one(InventaireProduit2)
x3 = InventaireProduit.insert_one(InventaireProduit3)
x4 = InventaireProduit.insert_one(InventaireProduit4)
print(x1)
print(x2)
print(x3)
print(x4)"""


#Question 1
pipe = [{'_id': None, 'totalcommande':{}
]
aggregation = caisse.aggregate()

