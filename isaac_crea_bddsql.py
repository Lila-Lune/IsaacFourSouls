# Créé par Lila, le 06/01/2025 en Python 3.7
import sqlite3


conn = sqlite3.connect('test13_isaac.db')
cursor = conn.cursor()

#créer les tables de la base de données

cursor.execute('''CREATE TABLE IF NOT EXISTS Monstre (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    pv INTEGER NOT NULL,
    atk INTEGER NOT NULL,
    resultat_dé INTEGER NOT NULL,
    effets TEXT,
    recompenses TEXT
    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Item (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    usage TEXT,
    effets TEXT
    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Tresor (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    effets TEXT
    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Personnage (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    pv INTEGER NOT NULL,
    atk INTEGER NOT NULL,
    eternel_id INTEGER
    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Eternel (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    effets TEXT
    )''')



conn.commit() #sauvegarde



#fonctions d'ajout des cartes pour remplir la base de données

def str_to_liste(string) :
    '''transforme une chaine de caractère en liste
    utile pour faire une liste d'effets ou de recompenses'''
    return string.split(",") if string else []

def ajouter_monstre() :
    print("Création d'une carte monstre")
    id = eval(input("entrer l'ID du monstre : "))
    nom = input("entrer le nom du monstre : ")
    pv = eval(input("entrer le nombre de pv du monstre : "))
    atk = eval(input("entrer l'attaque du monstre : "))
    resultat_dé = eval(input("entrer le resulatt minimum du dé pour faire des degats au monstre : "))    
    effets = input("entrer les effets du monstre, que ce soit pendant ou apres le combat (séparés par des virgules s'il y en a plusieurs et sans espace) : ") #ouais je sais pas trop comment je vais faire pour que les effets soient efficaces au bon moment....... tkt pour l'instant je crée juste les cartes)
    recompenses = input("entrer les récompenses promises après la mort du monstre (séparés par des virgules s'il y en a plusieurs et sans espace) : ")

    effets = str_to_liste(effets)
    recompenses = str_to_liste(recompenses)
    cursor.execute('''INSERT INTO Monstre (id, nom, pv, atk, resultat_dé, effets, recompenses) VALUES (?, ?, ?, ?, ?, ?, ?)''', (id, nom, pv, atk, resultat_dé, str(effets), str(recompenses)))
    conn.commit()
    print("Le monstre", nom, "a été ajouté avec succès !")

def ajouter_item() :
    print("Création d'un item")
    id = eval(input("entrer l'ID de l'item  : "))
    nom = input("entrer le nom de l'item : ")
    usage = input("defausse ou board ?") # a voir si je le transforme pas en booléen
    effets = input("entrer les effets de l'item, que ce soit pendant ou apres le combat (séparés par des virgules s'il y en a plusieurs et sans espace) : ")

    effets = str_to_liste(effets)
    cursor.execute('''INSERT INTO Item (id, nom, usage, effets) VALUES (?, ?, ?, ?)''', (id, nom, usage, str(effets)))
    conn.commit()
    print("L'item", nom, "a été ajouté avec succès !")

def ajouter_tresor() :
    print("Création d'un trésor")
    id = eval(input("entrer l'ID du trésor : "))
    nom = input("entrer le nom du trésor : ")
    effets = input("entrer les effets du trésor, que ce soit pendant ou apres le combat (séparés par des virgules s'il y en a plusieurs et sans espace) : ")  #il faut mettre la condition (s'il n'y en a pas mettre "rien") et un tiret puis l'effet (faudra que je me fasse une liste de comment je met es diff effets genre +1c == un coin supplémentaire, +1pv == plus un pv etc...)

    effets = str_to_liste(effets)
    cursor.execute('''INSERT INTO Tresor (id, nom, effets) VALUES (?, ?, ?)''', (id, nom, str(effets)))
    conn.commit()
    print("Le trésor", nom, "a été ajouté avec succès !")

def ajouter_personnage() :
    print("Création d'un personnage")
    id = eval(input("entrer l'ID du personnage  : "))
    nom = input("entrer le nom du personnage : ")
    pv = eval(input("entrer le nombre de pv du personnage : "))
    atk = eval(input("entrer l'attaque du personnage : "))
    eternel_id = input("entrer l'ID de l'eternel associé au personnage : ") #oui c'est chiant je me demande si je devrait pas mettre directement le nom de l'eternel en cle unique pusqiu'ils sont uniques

    cursor.execute('''INSERT INTO Personnage (id, nom, pv, atk, eternel_id) VALUES (?, ?, ?, ?, ?)''', (id, nom, pv, atk, eternel_id))
    conn.commit()
    print("Le personnage", nom, "a été ajouté avec succès !")

def ajouter_eternel() :
    print("Création d'un eternel")
    id = eval(input("entrer l'ID de l'eternel : "))
    nom = input("entrer le nom de l'eternel : ")
    effets = input("entrer les effets de l'eternel, que ce soit pendant ou apres le combat (séparés par des virgules s'il y en a plusieurs et sans espace) : ")

    effets = str_to_liste(effets)
    cursor.execute('''INSERT INTO Eternel (id, nom, effets) VALUES (?, ?, ?)''', (id, nom, str(effets)))
    conn.commit()
    print("L'eternel", nom, "a été ajouté avec succès !")



#fonction pour interface de créationde carte (faut que je créer l'interface qui n'existe pour l'instant pas encore)
def creer_carte() :
    print("Bienvenue dans le créateur de cartes :)") #oui je m'amuse
    print("Choisissez le type de carte a créer : ")
    print("1 : Monstre")
    print("2 : Item")
    print("3 : Trésor")
    print("4 : Personage")
    print("5 : Eternel")

    choix = eval(input("Entrez votre choix (entre 1 et 5) : "))

    if choix == 1 :
        ajouter_monstre()
    elif choix == 2 :
        ajouter_item()
    elif choix == 3 :
        ajouter_tresor()
    elif choix == 4 :
        ajouter_personnage()
    elif choix == 5 :
        ajouter_eternel()
    else :
        print("J'ai dit entre 1 et 5 connard")

    recommencer = input("Voulez vous créer une nouvelle carte ? (Y/N)")
    if recommencer == "Y" :
        creer_carte()

creer_carte()



def reload() :
    """on efface tout et on recommance"""
    cursor.execute('''DROP TABLE Monstre''')
    cursor.execute('''DROP TABLE Item''')
    cursor.execute('''DROP TABLE Personnage''')
    cursor.execute('''DROP TABLE Tresor''')
    cursor.execute('''DROP TABLE Eternel''')












