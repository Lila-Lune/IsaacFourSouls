import random 
### abreviations
###piece = c
###butin = b
###tresor = t
###pv = v
###ame = s
###donjon = d
###magasin = m
###pioche = p
###le dé sera représenté oar la valeur x
###


recompense = ["c : +1", "v : +1"]
recompense_2 = ["v : +2"]
recompense_3 = ["v : -1"]

joueur = {"piece" : 1, "pv" : 1}


def regulation_piece(c) :
    joueur["piece"] += int(c[4:])
    return joueur["piece"]

def regulation_pv(v) :
    joueur["pv"] += int(v[4:])
    return joueur["pv"]

def dice() : 
    dice = random.randint(1,6)
    return dice


for i in range(len(recompense)) : 
    if recompense[i][5] == "x" : 
        recompense[i][5] = dice()
    if recompense[i][0] == "c" : 
        regulation_piece(recompense[i])
    elif recompense[i][0] == "v" :
        regulation_pv(recompense)
    

##print(regulation_pv(recompense_2[0]))

def test(liste) :
    for i in range(liste) : 
        if liste[i] == 0 : 
            liste[i] = 2
            i += 1
            print(i) 
        else : 
            print(i, "oui")

test([0,1,1,1,0,0,0,0,1,0,1,0,1,0])





d = {'monstre' :
    [ 
    {
        "id": 1,
        "name": "",
        "pv": 1,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : [""],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    }], 
    
    'personnage' : 
    [{
        "id": 1,
        "name": "horse",
        "pv": 1,
        "atk": 1,
        "eternel" : "", 
        "main" : "",
        "action": 2,
        "combat": 1,
        "ambient_text": "These can most often be found on plains. Their usefulness as transportation has made them valuable since ancient times. That said, wild horses do tend to get spooked and run off when approached, so if you_re looking to snag one, it_s best to sneak up on it.",
        "image": "x",
        "category": "personnage",
        "dlc": "false",
    }], 

    'tresor' : 
    [{
        "id" : 1,
        "name" : "",
        "engagement" : "Y/N", 
        "effets" : [""],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    }], 

    'butin' : 
    [{
        "id" : 1,
        "name" : "",
        "defausse" : "Y/N",  ###si oui, la carte sera transformée en tresor  
        "effets" : [""],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    }],

    'eternel' : 
    [{
        "id" : 1,
        "name" : "",
        "engagement" : "Y/N", 
        "effets" : [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    }],

    'ame_bonus' : 
    [{
        "id" : 1, 
        "name" : "Soul of Glutony",
        "condition" : "if len(joueur.butin) == 10 : joueur.ame += 1, del Soul of glutony", ###a recoder correctement
        "image": "x",
        "category": "ame_bonus",
        "dlc": "false"
    }
    {
        "id" : 2, 
        "name" : "Soul of Greed",
        "condition" : "if len(joueur.butin) == 10 : joueur.ame += 1, del Soul of glutony", ###a recoder correctement
        "image": "x",
        "category": "ame_bonus",
        "dlc": "false"
    }
    {
        "id" : 3, 
        "name" : "Soul of Guppy",
        "condition" : "si le joeuur controle au moins deux objets de guppy il remporte cette ame", ###a recoder correctement
        "image": "x",
        "category": "ame_bonus",
        "dlc": "false"
    }]
    
}

###les trois pioches sont melangées au hasard en debut de game et puis c'est tout. (puisqu'elles ne sont pas decouverte quand on fait un rechrche)

###faire une fonction de defausse qui permet de choisir la carte dont on ne veut plus parmis celle qu'on a dans la main (ou parmis les tresors)

### a penser : piece, butin et tresors ne peuvent etre negatif donc : if piece/butin/tresor <0 : piece/butin/tresor = 0