import random 

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





d = {'personnage' : 
    {
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
        "category": "monstre",
        "dlc": "false",
    }
}

### a penser : piece, butin et tresors ne peuvent etre negatif donc : if piece/butin/tresor <0 : piece/butin/tresor = 0