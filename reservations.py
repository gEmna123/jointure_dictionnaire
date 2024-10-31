import pprint
import json
import redis

# Les données de réservations
d = {
    "1001": {"vol": "V601", "classe": "Economique", "nombreDePlaces": "6", "nom": "Becquerel", "numero": "24", "rue": "Rue De Fabre", "code postale": "13015", "ville": "Marseille", "coefPrix": "5"},
    # Ajoutez les autres entrées...
}

def jointure(d1, d2, att):
    c = 1
    for i in d1.keys():
        for j in d2.keys():
            if d1[i][att] == d2[j][att]:
                print('Join #', c, 'between', d1[i], 'and', d2[j])
                c += 1

# Création de sous-dictionnaires
n = len(d)
d1 = {}
d2 = {}
for i, (k, v) in enumerate(d.items()):
    if i < n / 2:
        d1[k] = v
    else:
        d2[k] = v

print('First dictionary:')
pprint.pp(d1)
print('Second dictionary:')
pprint.pp(d2)

# Jointure par classe et ville
jointure(d1, d2, 'classe')
print('--------------')
jointure(d1, d2, 'ville')

# Conversion des résultats en JSON
resultat_jointure = {"d1": d1, "d2": d2}
json_result = json.dumps(resultat_jointure)

# Stockage dans Redis (assurez-vous que Redis est en cours d'exécution)
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('jointure_result', json_result)

print("Résultat jointure stocké dans Redis.")
