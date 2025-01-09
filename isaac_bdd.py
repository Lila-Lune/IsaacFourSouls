# Créé par LOGET, le 07/05/2024 en Python 3.7

from PIL import Image
import sqlite3

d = {'monstres' :

[
    {
        "id": 1,
        "name": "Dip",
        "pv": 1,
        "atk": 1,
        "ambient_text": "Ils auront tellement faim et soif qu'il en mangeront leurs excrements et en boiront leur urine. Esaïe 36:12",
        "dice_result": 4,
        "effects" : [""],
        "drops": ["c : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 2,
        "name": "Pooter",
        "pv": 2,
        "atk": 1,
        "ambient_text": "Il parle, et il vint des mouches venimeuses, et des poux dans tous leurs confins. Psaume 105:31",
        "dice_result": 3,
        "effects" : [""],
        "drops": ["b : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 3,
        "name": "Fly",
        "pv": 1,
        "atk": 1,
        "ambient_text": "Malheur au pays qui fait ombre avec des ailes, qui est au-delà des fmeuves de cush. Esaïe 18:1",
        "dice_result": 2,
        "effects" : [""],
        "drops": ["c : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 4,
        "name": "Trite",
        "pv": 1,
        "atk": 1,
        "ambient_text": "Le sacrificateur sacrifiera l'oiseau sur l'autel; il lui ouvrira la tête avec l'ongle, et la brûlera sur l'autel, et il exprimera le sang contre un côté de l'autel. Lévitique 1:15",
        "dice_result": 5,
        "effects" : [""],
        "drops": ["b : +2"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 5,
        "name": "Fatty",
        "pv": 4,
        "atk": 1,
        "ambient_text": "Car l'ivrogne et celui qui se livre à des excès s'appauvrissent. Proverbes 23:21",
        "dice_result": 2,
        "effects" : [""],
        "drops": ["b : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 6,
        "name": "Spider",
        "pv": 1,
        "atk": 1,
        "ambient_text": "Tu saisis l'araignée avec les mains, et il est dans les palais des rois. Proverbes 23:21",
        "dice_result": 4,
        "effects" : [""],
        "drops": ["b : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 7,
        "name": "Conjoined Fatty",
        "pv": 4,
        "atk": 2,
        "ambient_text": "Les jours où elle devait accoucher s'accomplirent; et voici, il y avait deux jumeaux dans son ventre. Genèse 25:24",
        "dice_result": 3,
        "effects" : [""],
        "drops": ["b : +2"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 8,
        "name": "Pale Fatty",
        "pv": 4,
        "atk": 1,
        "ambient_text": "Alors le roi changea de couleur, et ses pensées le troublèrent; les jointures de ses reins se relâchèrent, et ses genoux se heurtèrent l'un contre l'autre. Daniel 5:6",
        "dice_result": 3,
        "effects" : [""],
        "drops": ["c : +6"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 9,
        "name": "Leech",
        "pv": 1,
        "atk": 2,
        "ambient_text": "C'est un peuple qui se lève comme une lionne, et qui se dresse comme un lion : il ne se couche point jusqu'à ce qu'il ai dévoré la proie et qu'il ait bu le sang des blessés. Nombres 23:24",
        "dice_result": 4,
        "effects" : [""],
        "drops": ["b : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 10,
        "name": "Clotty",
        "pv": 2,
        "atk": 1,
        "ambient_text": "La fin de toute chair est arrêtée par-devers moi : car ils ont rempli la terre de violence : voici, je vais les détruire avec la Terre. Genèse 6:13",
        "dice_result": 3,
        "effects" : [""],
        "drops": ["c : +4"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 11,
        "name": "Red Host",
        "pv": 2,
        "atk": 2,
        "ambient_text": "Le Soleil est devenu noir comme un sac, la pleine Lune est devenue comme du sang. Révélation 6:12",
        "dice_result": 3,
        "effects" : [""],
        "drops": ["c : +5"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 12,
        "name": "Squirt",
        "pv": 2,
        "atk": 1,
        "ambient_text": "Ne comprenez-vous pas que tout ce qui entre dans la bouche va dans le ventre, puis est jeté dans les excréments ? Mathieu 15:17",
        "dice_result": 4,
        "effects" : [""],
        "drops": ["b : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 13,
        "name": "Fat Bat",
        "pv": 3,
        "atk": 1,
        "ambient_text": "Qui sont ceux-là qui volent comme des nuées, comme des colombes vers leur colombier ? Ésaïe 60:8",
        "dice_result": 5,
        "effects" : [""],
        "drops": ["t : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 14,
        "name": "Cod Worm",
        "pv": 1,
        "atk": 0,
        "ambient_text": "Où leur ver ne meurt point, et où le feu ne s'éteint point. Marc 9:48",
        "dice_result": 6,
        "effects" : [""],
        "drops": ["c : +3"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 15,
        "name": "Swarm of Flies",
        "pv": 5,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 2,
        "effect": ["if dice == 5 : joueur.pv -= 1"],
        "drops": ["c : +5"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 16,
        "name": "Black Bony",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effect": ["if monstre.pv <= 0 : joueur.pv -= 1"],
        "drops": ["b : +x"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 17,
        "name": "Dinga",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["if monstre.pv <= 0 and dice == 6 : drops.add(drops[0])"],
        "drops": ["c : +x"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 18,
        "name": "Ring of flies",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["Chaque fois que l'attaquant obtient 3 au dé, il doit voler 1 carte butin au hasard à un joueur (joueur_x, les joueurs seront direct les persos)"], ###a reforumuler en codage
        "drops": ["c : +3"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 19,
        "name": "Hanger",
        "pv": 2,
        "atk": 2,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if montre.pv <= 0 : m += 1"],
        "drops": ["c : +7"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 20,
        "name": "Wizoob",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 5,
        "effects" : ["if montre.pv <= 0 : joueur_x.soul -= 1"],
        "drops": ["b : +3"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 21,
        "name": "Mulligan",
        "pv": 1,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["Quand ce monstre meurt, augmentez de 1 le nombre de monstres actifs"], ### a reformuler en codage
        "drops": ["c : +3"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 22,
        "name": "Hopper",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["if dice == 6 : montre.pv += 1"],
        "drops": ["c : +3"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 23,
        "name": "Keeper Head",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice < monstre.dice_result : joueur.piece -= 2"],
        "drops": ["c : +x"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 24,
        "name": "Big Spider",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["Quand ce monstre meurt, vous pouvez attaquer le paquet monstre une fois supplémentaire"], ### a reformuler en codage
        "drops": ["b : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 25,
        "name": "Boom Fly",
        "pv": 1,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if monstre.pv <= 0, (all)joueur.pv -= 1"], ###trouver comment definir les joueurs, en faisant une liste des persos actif par ex
        "drops": ["c : +4"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 26,
        "name": "Leaper",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 1  : joueur.pv -=1"],
        "drops": ["c : +5"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 27,
        "name": "Dople",
        "pv": 2,
        "atk": 2,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["Tous les dégâts infligés à ce monstre sont aussi infligés au joueur à votre droite."], ###tjrs le pb de trouver cmment definir les joueurs
        "drops": ["c : +7"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 28,
        "name": "Psy Horf",
        "pv": 1,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 5,
        "effects" : ["Quand ce monstre meurt, rechargez tous vos objets actifs"], ### a revoir quand j'aurais defini les objets
        "drops": ["b : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 29,
        "name": "Portal",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["quand ce monstre meurt (if monstre.pv <= 0), vous devez attaquer une fois supplementaire (appeler fonction combat)"], ###trouver comment nommer les actions
        "drops": ["c : +3"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 30,
        "name": "Mom's dead hand",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 5,
        "effects" : ["Qaund ce monstre meurt vous pouvez voler un objet a un joueur"], ###pb de comment definir un joueur
        "drops": ["c : +4"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 31,
        "name": "Greedling",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 5,
        "effects" : ["if monstre.pv <= 0 : choixjoueur().pieces -= 7"], ###definir fonction pour choisir un joueur
        "drops": ["c : +7"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 32,
        "name": "Dank Goblin",
        "pv": 2,
        "atk": 2,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if monstre.pv <= 0 : choix_joueur().butin -= 2"],
        "drops": ["b : +2"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 33,
        "name": "Evil twin",
        "pv": 3,
        "atk": 2,
        "ambient_text": "",
        "dice_result": 5,
        "effects" : ["Tous les dégats infligés à ce monstre sont aussi infligés au joueur de gauche"], ###pb definir le joueur
        "drops": ["t : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 34,
        "name": "Mulliboom",
        "pv": 1,
        "atk": 4,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if monstre.pv <= 0 : choix_joueur().pv -= 3"],
        "drops": ["c : +6"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 35,
        "name": "Mom's eye",
        "pv": 1,
        "atk": 2,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["quand ce monstre meurt, vous pouvez regarder la main d'un joueur"], ### avoir une fonction choix_joueur() et une fonction show (peut etre qui serait utile pour montrer les cartes des pioches aussi)
        "drops": ["b : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 36,
        "name": "Rage Creep",
        "pv": 1,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 5,
        "effects" : ["chaque fois que ce monstre vous inflige des degats il en inflige aussi au joeuur a votre droite"], ###pb de choix du joueur
        "drops": ["b : +2"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 37,
        "name": "Horf",
        "pv": 1,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 2 : joueur.pv -= 1"],
        "drops": ["c : +3"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 38,
        "name": "Mom's hand",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 6 : end_turn"], ###faire une fonction qui arrete le tour
        "drops": ["c : +4"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 39,
        "name": "Stoney",
        "pv": 3,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["dice -= 1 en combat", "si un monstre de la pile meurt, il meurt aussi"], ###a recoder correctement quand j'aurais les fonctions
        "drops": ["b : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 40,
        "name": "Holy Dip",
        "pv": 1,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 1 : joueur.piece += 1"], ### faire en sorte que le dice soit pris en compte pndnt toutes les phases, pas que l'attaque du monstre 
        "drops": ["c : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 41,
        "name": "Holy Mom's eye",
        "pv": 1,
        "atk": 2,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 2 : choix_objet().recharge"], ### faire fonction de recharge + faire en sorte que le dice soit pris en compte pndnt toutes les phases, pas que l'attaque du monstre 
        "drops": ["b : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 42,
        "name": "Holy Dinga",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["if dice == 6 and monstre.pv < 3 : monstre.pv +=1"], ###faire en sorte que le dice soit pris en compte pndnt toutes les phases, pas que l'attaque du monstre 
        "drops": ["c : +x"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 43,
        "name": "Holy keeper",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 4 : joueur.piece += 2"], ###faire en sorte que le dice soit pris en compte pndnt toutes les phases, pas que l'attaque du monstre 
        "drops": ["c : +x"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 44,
        "name": "Holy Squirt",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["if dice == 5 : joueur.butin += 1"], ###faire en sorte que le dice soit pris en compte pndnt toutes les phases, pas que l'attaque du monstre 
        "drops": ["b : +2"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 45,
        "name": "Cursed Keeper head",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 1 : joueur.piece -= 2"], ###faire en sorte que le dice soit pris en compte pndnt toutes les phases, pas que l'attaque du monstre 
        "drops": ["c : +x"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 46,
        "name": "Cursed Horf",
        "pv": 1,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 2 : joueur.pv -= 2"], ###faire en sorte que le dice soit pris en compte pndnt toutes les phases, pas que l'attaque du monstre 
        "drops": ["c : +3"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 47,
        "name": "Cursed Fatty",
        "pv": 4,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 2,
        "effects" : ["if dice == 5 : joueur.butin -= 1"], ###faire en sorte que le dice soit pris en compte pndnt toutes les phases, pas que l'attaque du monstre + choix de la carte a défausser 
        "drops": ["b : +2"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 48,
        "name": "Cursed Mom's hand",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 6 : end_turn"], ###faire fonction de fin de tour + faire en sorte que le dice soit pris en compte pndnt toutes les phases, pas que l'attaque du monstre 
        "drops": ["c : +4"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 49,
        "name": "Cursed Psy Horf",
        "pv": 1,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 5,
        "effects" : ["quand le joeuur active un objet, il subit un degat"], ###une fonction qui detecte l'enclenchement d'un objet, peut importe la phase en cours
        "drops": ["b  : +2"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 50,
        "name": "Cursed Gaper",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["Quand un joueur obtient (4) au dé, tous les monstres actifs obtiennent +1atk jusqu'à la fin du tour"], ### a encoder correctement ###faire en sorte que le dice soit pris en compte pndnt toutes les phases, pas que l'attaque du monstre 
        "drops": ["c : +3"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 51,
        "name": "Gold Chest",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["if dice < 3 : joueur.tresor += 1", "elif dice < 5 : joueur.piece += 5", "elif dice <=6 : joueur.piece +=7"],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 52,
        "name": "Gold Chest",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["if dice < 3 : joueur.tresor += 1", "elif dice < 5 : joueur.butin += 1", "elif dice <=6 : joueur.butin +=2"],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 53,
        "name": "Dark Chest",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["if dice < 3 : joueur.butin += 1", "elif dice < 5 : joueur.piece += 3", "elif dice <=6 : joueur.pv -=2"],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 54,
        "name": "Dark Chest",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["if dice < 3 : joueur.piece += 1", "elif dice < 5 : joueur.butin += 2", "elif dice <=6 : joueur.pv -=2"],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 55,
        "name": "Chest",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["if dice < 3 : joueur.piece += 1", "elif dice < 5 : joueur.piece += 3", "elif dice <=6 : joueur.piece += 6"],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 56,
        "name": "Chest",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["if dice < 3 : joueur.butin += 1", "elif dice < 5 : joueur.butin += 2", "elif dice <=6 : joueur.butin += 3"],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 57,
        "name": "Secret Room",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["if dice == 1 : joueur.pv -= 3", "elif dice < 4 : joueur.butin -= 2", "elif dice < 6 : joueur.piece += 7", "if dice == 6 : joueur.tresor += 1"], ###faire fcontion de chxoi de butin
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 58,
        "name": "XL Floor",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["donjon += 1", "joueur.action_atk += 1"],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 59,
        "name": "Shop Upgrade !!!",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["magasin += 2", "joueur.action_atk += 1"],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 60,
        "name": "We need to go deeper !",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["Placer autant de monsrte que vous voulez au-dessus du paquet monstre dans l'ordre de votre choix", "joueur.action_atk += 1"], ###cette carte je sens elle va jerter
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 61,
        "name": "I can see Forever !",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["regardez les six premieres cartes du paquet butin, replacez les dans l'ordre de votre choix puis piochez une carte butin"],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 62,
        "name": "Troll Bombs",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["joueur.pv -= 2"],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 63,
        "name": "Mega Troll Bomb !",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["tous les joeuurs subissent 2 degats"], ###definir tous les joueurs
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 64,
        "name": "Ambush",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["vous devez attaquer deux fois le paquet monstre ce tour ci"], ### a recoder corretement
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 65,
        "name": "Greed",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["choix_joueur().piece = 0"],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 66,
        "name": "Devil Deal",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["choisissez un des trois : defausser une carte, piocher une carte butin et subissez un degat, guppy_finder()"], ### a recoder correctement + faire une fonction guppy
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 67,
        "name": "Cursed Chest",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["if dice < 4 : joueur.pv -= 1", "elif dice < 6 : joueur.pv -= 2", "elif dice == 6 : guppy_finder"], ###faire fonction guppy
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    ###Cartes curse qui nescessite encore un gameplay different... pas la priorité
    {
        "id": 68,
        "name": "Malédiction de l'amnésie",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : [""],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 69,
        "name": "Curse of greed",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : ["", ""],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 70,
        "name": "Curse of loss",
        "pv": 1,
        "atk": 0,
        "ambient_text": "",
        "dice_result": 0,
        "effects" : [""],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 71,
        "name": "Curse of pain",
        "pv": 1,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : [""],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 72,
        "name": "Curse of the blind",
        "pv": 1,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : [""],
        "drops": [""],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 73,
        "name": "Gurdy",
        "pv": 5,
        "atk": 1,
        "ambient_text": "Et que ces eaux-là qui apportent la malédiction, entrent dans tes entrailles pour te faire enfler le ventre, et faire tomber ta cuisse. Alors la femme répondra, Amen, Amen. Nombres 5:22",
        "dice_result": 4,
        "effects" : [""],
        "drops": ["c : +7", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 74,
        "name": "Monstro",
        "pv": 4,
        "atk": 1,
        "ambient_text": "Car aucun homme en qui il y aura quelque défaut n'en approchera : l'homme aveugle, ou boiteux, ou qui aura quelque superfluité dans ses membres. Lévitique 21:18",
        "dice_result": 4,
        "effects" : [""],
        "drops": ["c : +6", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    }
    {
        "id": 75,
        "name": "Little Horn",
        "pv": 2,
        "atk": 1,
        "ambient_text": "Little Horn avait les yeux et la bouche comme un Homme, les yeux pouvaient voir des choses que les autres cornes ne pouvaient pas et sa bouche parlait avec arrogance. Daniel 7:8",
        "dice_result": 6,
        "effects" : [""],
        "drops": ["b : +2", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 76,
        "name": "Dark one",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice >= 4 : monstre.atk += 1", "when end_turn : monstre.atk = 1"],
        "drops": ["t : +1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 77,
        "name": "Larry Jr.",
        "pv": 4,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["if monstre.pv <= 2 : monstre.dice_result += 4"],
        "drops": ["c : +6", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 78,
        "name": "The Duke of flies",
        "pv": 4,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["if monstre.pv <= 1  : if dice == 1 : monstre.pv = 1"],
        "drops": ["b : +1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 79,
        "name": "Daddy Long Legs",
        "pv": 4,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 1 : (all)monstre.dice_result += 1"], ###a recoder correctement
        "drops": ["c : +7", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 80,
        "name": "Mega Fatty",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["if dice_result < 3 and monstre.pv < 3 : monstre.pv += 1"],
        "drops": ["b : +1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 81,
        "name": "Famine",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["quand ce monstre meurt, le joueur actif passe son rpochain tour"], ### a recoder correctement
        "drops": ["b : +3", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 82,
        "name": "War",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["if dice_result < 3 : monstre.atk += 1"],
        "drops": ["c : +8" , "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 83,
        "name": "Death",
        "pv": 3,
        "atk": 2,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if monstre.pv <= 0 : choix_joueur().pv = 0"],
        "drops": ["t : +1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 84,
        "name": "Pestilence",
        "pv": 4,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if monstre.pv <= 0 : repartir 2 degats entre des joeuurs ou des monstres"], ###faire une focntion choix
        "drops": ["b : +2", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 85,
        "name": "Conquest",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["if monstre.pv <= 0 : combat()"], ###lance la fonction combat()
        "drops": ["c : +6", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 86,
        "name": "Pride",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["quand vous attaquez ce monstre, forcez un joueur a se defausser d'une carte butin"], ### a coder correctement
        "drops": ["c : +5", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 87,
        "name": "Wrath",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["if monstre.pv <= 0 : dice() : if dice < 4 : (all)joueur.pv -= 1, else :  (all)joueurs.pv -= 2"], ### a recoder correctement
        "drops": ["c : +6", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 88,
        "name": "Gluttony",
        "pv": 4,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["if dice() == 6 : choix_joueur().pv -= 1"], ###choisir le joueur de gauche
        "drops": ["b : +1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 89,
        "name": "Envy",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 5,
        "effects" : ["if monstre.pv <= 0 : combat()"],
        "drops": ["c : +1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 90,
        "name": "Greed",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice_result < 4 : (all)joueurs.piece -= 4"],
        "drops": ["c : +9", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 91,
        "name": "Lust",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice_result > 3 : joueur.pv -= 1"],
        "drops": ["b : +2", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 92,
        "name": "Sloth",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if monstre.pv <= 0 : joueur.butin = 0"], ###choix du joueur
        "drops": ["c : +1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 93,
        "name": "Pin",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 6 : monstre.pv += 1"],
        "drops": ["c : +5", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 94,
        "name": "The Bloat",
        "pv": 4,
        "atk": 2,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["quand ce monstre inflige des degats a l'attaquant, il en inflige aussi a tous les joueurs"], ###a recoder correctement 
        "drops": ["t : +1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 95,
        "name": "Chub",
        "pv": 4,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["if dice == 1 and monstre.pv < 4 : monstre.pv +=2, if monstre.pv > 4 : monstre.pv = 4"],
        "drops": ["c : +7", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 96,
        "name": "Scolex",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 5,
        "effects" : ["a chaque fois que ce monstre inflige des degats a un joueur, ce dernier defausse 1 butin"], ###a recoder correctement
        "drops": ["t : +=1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 97,
        "name": "Gemini",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if monstre.pv == 1 : monstre.atk = 2"], ###Faire un fonction qui end turn et qui remet a zero
        "drops": ["c : +5", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 98,
        "name": "Gurdy Jr.",
        "pv": 2,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 5,
        "effects" : ["a chaque fois que l'attaquant active un objet, deals one damage to this monster"], ###a recoder correctement
        "drops": ["t : +1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 99,
        "name": "Peep",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["quand ce monstre meurt, chercher the bloat dans le âquet monstre, placez le sur un emplacement de monstre et melangez le paquet monstre"], ###a recoder correctement
        "drops": ["t : +1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 100,
        "name": "Ragman",
        "pv": 2,
        "atk": 2,
        "ambient_text": "",
        "dice_result": 3,
        "effects" : ["Quand ce monstre meurt et que vous avez recup ses recompenses, replacer la carte au dessu du aquer si vous obtenez un ou six"], ###a recoder correctement
        "drops": ["b : +3", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 101,
        "name": "Carrion queen",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 4 or dice == 5 : monstre.pv += 1"],
        "drops": ["t : +1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 102,
        "name": "The Haunt",
        "pv": 3,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["chaqe fois que ce monstre subit deux degats, il obtient dice_result += 1 jusqu'a la fin du tour."], ###a recoder correctement
        "drops": ["t : +1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 103,
        "name": "Mask of infamy",
        "pv": 4,
        "atk": 1,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if monstre.pv == 1 : dice_result += 2"], ###fonction reinitialisation a la fin du tour
        "drops": ["t : +1", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 104,
        "name": "Mom !",
        "pv": 5,
        "atk": 2,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 1 : joueur.pv -= 1", "if monstre.pv <= 0 : d += 1"],
        "drops": ["t : +1", "s : +2"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 105,
        "name": "Satan !",
        "pv": 6,
        "atk": 2,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if dice == 6 : choix_joueur().pv = 0"],
        "drops": ["t : +1", "s : +2"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 106,
        "name": "The Lamb",
        "pv": 6,
        "atk": 6,
        "ambient_text": "Je vais avaler ton âme ! Ne vient pas de la bible",
        "dice_result": 3,
        "effects" : ["quand ce monstre meurt, vous pouvez forcer un joueur à vous donner une ame"], ###a recoder 
        "drops": ["c : +3", "s : +1"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 107,
        "name": "Delirium",
        "pv": 5,
        "atk": 3,
        "ambient_text": "",
        "dice_result": 4,
        "effects" : ["if monster.pv <= 0, replacer le en sixieme position dans la pioche", "tant que ce monstre est actif les autres monstres ont dice_result += 1"], ### a voir comment j'appelle la pioche et comment elle est codée
        "drops": ["t : +2"],
        "image": "x",
        "category": "monstre",
        "dlc": "false"
    },
    {
        "id": 108,
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
    },
    {
        "id": 109,
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
    },
    {
        "id": 110,
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
    },
    {
        "id": 111,
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
    },
    {
        "id": 112,
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
    },
    {
        "id": 113,
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
    },
    {
        "id": 114,
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
    },
    {
        "id": 115,
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
    },
    {
        "id": 116,
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
    },
    {
        "id": 117,
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
    },
    {
        "id": 118,
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
    },
    {
        "id": 119,
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
    },
    {
        "id": 120,
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
    }
    {
        "id": 121,
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
    },
    {
        "id": 122,
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
    },
    {
        "id": 123,
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
    },
    {
        "id": 124,
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
    },
    {
        "id": 125,
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
    },
    {
        "id": 126,
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
    },
    {
        "id": 127,
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
    },
    {
        "id": 128,
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
    },
    {
        "id": 129,
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
    },
    {
        "id": 130,
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
    },
    {
        "id": 131,
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
    },
    {
        "id": 132,
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
    },
    {
        "id": 133,
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
    },
    {
        "id": 134,
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
    },
    {
        "id": 135,
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
    },
    {
        "id": 136,
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
    },
    {
        "id": 137,
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
    },
    {
        "id": 138,
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
    },
    {
        "id": 139,
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
    },
    {
        "id": 140,
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
    },
    {
        "id": 141,
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
    },
    {
        "id": 142,
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
    },
    {
        "id": 143,
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
    },
    {
        "id": 144,
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
    },
    {
        "id": 145,
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
    },
    {
        "id": 146,
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
    },
    {
        "id": 147,
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
    },
    {
        "id": 148,
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
    },
    {
        "id": 149,
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
    },
    {
        "id": 150,
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
    },
    {
        "id": 151,
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
    },
    {
        "id": 152,
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
    },
    {
        "id": 153,
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
    },
    {
        "id": 154,
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
    },
    {
        "id": 155,
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
    },
    {
        "id": 156,
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
    },
    {
        "id": 157,
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
    }

]
, 'equipement' :

[
    {
        "id": 201,
        "name": "master sword",
        "description": "The legendary sword that seals the darkness. Its blade gleams with a sacred luster that can oppose the Calamity. Only a hero chosen by the sword itself can wield it.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/master_sword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 30,
            "defense": 0
        }
    },
    {
        "id": 202,
        "name": "tree branch",
        "description": "Wooden branches such as this are pretty common, but it_s surprisingly well-balanced. It doesn_t do much damage, but can serve as a weapon in a pinch.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/tree_branch/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 2,
            "defense": 0
        }
    },
    {
        "id": 203,
        "name": "torch",
        "description": "This torch will stay lit once ignited, but if you put it away, the flame will be extinguished until you light it again.",
        "common_locations": [
            "Great Hyrule Forest",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/torch/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 2,
            "defense": 0
        }
    },
    {
        "id": 204,
        "name": "soup ladle",
        "description": "A kitchen implement often used for serving delicious soups. It was carved from the wood of a sturdy tree, so it actually packs quite the wallop.",
        "common_locations": [
            "Hyrule Field",
            "Tabantha Frontier"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/soup_ladle/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 4,
            "defense": 0
        }
    },
    {
        "id": 205,
        "name": "boomerang",
        "description": "This throwing weapon was originally used by the forest-dwelling Koroks. Its unique shape allows it to return after being thrown.",
        "common_locations": [
            "West Necluda",
            "Faron Grasslands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/boomerang/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 8,
            "defense": 0
        }
    },
    {
        "id": 206,
        "name": "spring-loaded hammer",
        "description": "This strange hammer is one of Kilton_s specialties. Being struck by it doesn_t hurt much, but the forth swing in a string of attacks will send the victim flying.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/spring-loaded_hammer/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 1,
            "defense": 0
        }
    },
    {
        "id": 207,
        "name": "traveler_s sword",
        "description": "A very common sword often kept by travelers to fend off small beasts. It_s fairly durable, but a bit unreliable against monsters.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/travelers_sword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 5,
            "defense": 0
        }
    },
    {
        "id": 208,
        "name": "soldier_s broadsword",
        "description": "A sword brandished by the soldiers who once protected Hyrule Castle. Its durable blade is well tuned for slaying monsters.",
        "common_locations": [
            "Hyrule Field",
            "Faron Grasslands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/soldiers_broadsword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 14,
            "defense": 0
        }
    },
    {
        "id": 209,
        "name": "knight_s broadsword",
        "description": "Knights of Hyrule once carried this sword. These days it_s the weapon of choice for seasoned adventurers thanks to its ease of use and high attack power.",
        "common_locations": [
            "Gerudo Desert",
            "Tabantha Frontier"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/knights_broadsword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 26,
            "defense": 0
        }
    },
    {
        "id": 210,
        "name": "royal broadsword",
        "description": "The Hyrulean royal family would award this sword to knights who achieved remarkable feats. A sword that balances strength and beauty as elegantly as this one is a rare find.",
        "common_locations": [
            "Tabantha Frontier",
            "Akkala Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/royal_broadsword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 36,
            "defense": 0
        }
    },
    {
        "id": 211,
        "name": "forest dweller_s sword",
        "description": "Koroks made this sword for Hylians. It_s made of wood, so it isn_t the best choice for head-on attacks. Its original intent was likely clearing vines to forge paths through forests.",
        "common_locations": [
            "Great Hyrule Forest",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/forest_dwellers_sword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 22,
            "defense": 0
        }
    },
    {
        "id": 212,
        "name": "zora sword",
        "description": "The ornamentation that adorns this blade is a traditional Zora design. It_s forged from a very durable and rust-proof metal.",
        "common_locations": [
            "Lanayru Great Spring",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/zora_sword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 15,
            "defense": 0
        }
    },
    {
        "id": 213,
        "name": "feathered edge",
        "description": "Rito craftsmen forged this lightweight, double-edged sword so Rito warriors could soar into battle unhindered by its weight.",
        "common_locations": [
            "Tabantha Frontier",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/feathered_edge/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 15,
            "defense": 0
        }
    },
    {
        "id": 214,
        "name": "gerudo scimitar",
        "description": "This common sword is often carried by Gerudo women for self-defense. Its short, curved blade is easily recognized.",
        "common_locations": [
            "Gerudo Highlands",
            "Gerudo Desert"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/gerudo_scimitar/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 16,
            "defense": 0
        }
    },
    {
        "id": 215,
        "name": "moonlight scimitar",
        "description": "Delicate Gerudo carvings decorate this curved sword. The engraved blade is extremely sharp. Apparently it once served ceremonial purposes in festivals.",
        "common_locations": [
            "Gerudo Highlands",
            "Gerudo Desert"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/moonlight_scimitar/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 25,
            "defense": 0
        }
    },
    {
        "id": 216,
        "name": "scimitar of the seven",
        "description": "A famous sword once beloved by the Gerudo Champion Urbosa. It is said that when Urbosa swung this sword in battle, her movements resembled a beautiful dance.",
        "common_locations": [
            "Gerudo Town"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/scimitar_of_the_seven/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 32,
            "defense": 0
        }
    },
    {
        "id": 217,
        "name": "eightfold blade",
        "description": "A single-edged sword traditional to the Sheikah tribe. Forged using ancient technology, it_s said to be among the sharpest conventional weapons ever made.",
        "common_locations": [
            "West Necluda",
            "Lake Hylia"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/eightfold_blade/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 15,
            "defense": 0
        }
    },
    {
        "id": 218,
        "name": "ancient short sword",
        "description": "The blade of this ancient sword was made using an ancient power lost to this modern age. Its blade appears only when drawn, and its cutting power surpasses metal swords.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ancient_short_sword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 40,
            "defense": 0
        }
    },
    {
        "id": 219,
        "name": "rusty broadsword",
        "description": "This once-fearsome sword has seen better days. It can do some damage in the right hands but also breaks quickly.",
        "common_locations": [
            "Hyrule Field",
            "Eldin Canyon"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/rusty_broadsword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 6,
            "defense": 0
        }
    },
    {
        "id": 220,
        "name": "royal guard_s sword",
        "description": "A Sheikah-made replica of the sword that seals the darkness. It was made with ancient technology to oppose the Great Calamity, but its low durability made it inefficient.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/royal_guards_sword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 48,
            "defense": 0
        }
    },
    {
        "id": 221,
        "name": "flameblade",
        "description": "This magical sword was forged in the lava of Death Mountain. It leaves white-hot flames in its wake when the blade glows red.",
        "common_locations": [
            "Hyrule Field",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/flameblade/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 24,
            "defense": 0
        }
    },
    {
        "id": 222,
        "name": "frostblade",
        "description": "A magical sword forged in the frigid mountains of the Hebra region. When the blade glows blue, enemies struck by it will become frozen.",
        "common_locations": [
            "Gerudo Highlands",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/frostblade/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 20,
            "defense": 0
        }
    },
    {
        "id": 223,
        "name": "thunderblade",
        "description": "A magical sword forged and refined by lightning from the Hyrule Hills. When the blade shines with a golden light, it will electrocute enemies struck by it.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/thunderblade/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 22,
            "defense": 0
        }
    },
    {
        "id": 224,
        "name": "boko club",
        "description": "A crude Bokoblin club made to clobber small prey. It_s essentially a stick, so its durability is low.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/boko_club/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 4,
            "defense": 0
        }
    },
    {
        "id": 225,
        "name": "spiked boko club",
        "description": "A reinforced Bokoblin club made to maximize damage. The sharpened bones jabbed into make it a brutal weapon.",
        "common_locations": [
            "Faron Grasslands",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/spiked_boko_club/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 12,
            "defense": 0
        }
    },
    {
        "id": 226,
        "name": "dragonbone boko club",
        "description": "This Bokoblin club has been reinforced with fossilized bones to maximize clobbering potential. Only the brawniest of Bokoblins can manage its immense weight.",
        "common_locations": [
            "Hyrule Ridge",
            "Necluda Sea"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/dragonbone_boko_club/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 24,
            "defense": 0
        }
    },
    {
        "id": 227,
        "name": "lizal boomerang",
        "description": "A curved sword favored by the Lizalfos. It can be used to attack directly or can be thrown like a boomerang.",
        "common_locations": [
            "Lake Hylia",
            "Lanayru Wetlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lizal_boomerang/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 14,
            "defense": 0
        }
    },
    {
        "id": 228,
        "name": "lizal forked boomerang",
        "description": "Blue Lizalfos in particular like this weapon. It has one more blade than the Lizal boomerang to give it additional cutting power, and it still returns when thrown.",
        "common_locations": [
            "Gerudo Desert",
            "Tabantha Frontier"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lizal_forked_boomerang/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 24,
            "defense": 0
        }
    },
    {
        "id": 229,
        "name": "lizal tri-boomerang",
        "description": "More blades mean more attack power! It can be used as a boomerang, but all those blades make that a bit more dangerous. Carried by Black Lizalfos seasoned in battle.",
        "common_locations": [
            "Hebra Mountains",
            "Akkala Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lizal_tri-boomerang/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 36,
            "defense": 0
        }
    },
    {
        "id": 230,
        "name": "guardian sword",
        "description": "A sword often wielded by Guardian Scouts. Its blue energy blade is a product of ancient technology. It_s not very durable.",
        "common_locations": [
            "Eldin Canyon",
            "Tabantha Frontier"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_sword_i/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 20,
            "defense": 0
        }
    },
    {
        "id": 231,
        "name": "guardian sword+",
        "description": "This Guardian sword has enhanced power over the standard model. Its cutting capabilities are improved, and its durability has seen a slight uptick.",
        "common_locations": [
            "Gerudo Highlands",
            "Akkala Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_sword_ii/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 30,
            "defense": 0
        }
    },
    {
        "id": 232,
        "name": "guardian sword++",
        "description": "The abilities of this Guardian sword have been boosted to the maximum., as evidenced by its increase in size. It slices through armor like a hot knife through butter!",
        "common_locations": [
            "Hebra Mountains",
            "Akkala Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_sword_iii/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 40,
            "defense": 0
        }
    },
    {
        "id": 233,
        "name": "lynel sword",
        "description": "This Lynel-made sword was designed with smashing in mind rather than slicing. It_s on the heavy side compared to what Hylians are used to, but it_s very strong.",
        "common_locations": [
            "Lanayru Great Spring",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lynel_sword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 24,
            "defense": 0
        }
    },
    {
        "id": 234,
        "name": "mighty lynel sword",
        "description": "This Lynel-made sword boasts more blades and more attack power. A skilled Lynel can draw this sword simply in passing and still cut a foe in two.",
        "common_locations": [
            "Hyrule Field",
            "Lanayru Great Spring"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/mighty_lynel_sword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 36,
            "defense": 0
        }
    },
    {
        "id": 235,
        "name": "savage lynel sword",
        "description": "A brutal sword carried by white-haired Lynels. The savage blades are strong enough to cut down any foe, no matter how strong.",
        "common_locations": [
            "Hyrule Field",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/savage_lynel_sword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 58,
            "defense": 0
        }
    },
    {
        "id": 236,
        "name": "fire rod",
        "description": "A magical rod that can cast fireballs, crafted by an ancient magician. The rod will break if it strikes something directly, so use it wisely.",
        "common_locations": [
            "Hyrule Field",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/fire_rod/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 10,
            "defense": 0
        }
    },
    {
        "id": 237,
        "name": "meteor rod",
        "description": "A magical rod that can cast three fireballs at once, crafted by an ancient magician. It will break upon running out of magical energy, so make it last!",
        "common_locations": [
            "Hyrule Field",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/meteor_rod/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 10,
            "defense": 0
        }
    },
    {
        "id": 238,
        "name": "ice rod",
        "description": "A magical rod crafted from refined ice found in the Hebra Mountains. This rod can cast waves of freezing air. Great for magic - not so great for melee.",
        "common_locations": [
            "Gerudo Highlands",
            "Eldin Canyon"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ice_rod/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 5,
            "defense": 0
        }
    },
    {
        "id": 239,
        "name": "blizzard rod",
        "description": "A magical rod that can cast extreme cold in a wide range. These are crafted from refined ice found at the summit of Hebra peak. It will break when depleted.",
        "common_locations": [
            "Gerudo Highlands",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/blizzard_rod/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 10,
            "defense": 0
        }
    },
    {
        "id": 240,
        "name": "lightning rod",
        "description": "A magical rod that can shoot balls of electricity. Its gem contains lightning from the Hyrule Hills. It_s not recommended to use as a melee weapon.",
        "common_locations": [
            "West Necluda",
            "Hyrule Ridge"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lightning_rod/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 5,
            "defense": 0
        }
    },
    {
        "id": 241,
        "name": "thunderstorm rod",
        "description": "A magical rod that can hurl three balls of electricity at once. Its gem contains electricity from the Hyrule Hills, and the rod will break when that electricity runs out.",
        "common_locations": [
            "Hyrule Field",
            "Hyrule Ridge"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/thunderstorm_rod/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 10,
            "defense": 0
        }
    },
    {
        "id": 242,
        "name": "vicious sickle",
        "description": "A grim weapon favored by the Yiga. The half-moon shape of the blade allows for the rapid delivery of fatal wounds and serves as a symbol of their terror. Its durability is low.",
        "common_locations": [
            "Gerudo Highlands",
            "Gerudo Desert"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/vicious_sickle/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 16,
            "defense": 0
        }
    },
    {
        "id": 243,
        "name": "demon carver",
        "description": "This lethal weapon is forged by the Yiga. Its unique shape facilitates the sound dispatching of any target and strikes fear into the hearts of all who see it.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/demon_carver/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 40,
            "defense": 0
        }
    },
    {
        "id": 244,
        "name": "one-hit obliterator",
        "description": "A weapon that defeats foes with one hit and causes the user to die within one hit. It loses its sheen and power after two consecutive uses, but it will eventually regain both.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/one-hit_obliterator/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 1000000000,
            "defense": 0
        }
    },
    {
        "id": 245,
        "name": "bokoblin arm",
        "description": "A skeletal arm that keeps moving even after it_s severed from its body. It_s kind of gross to strap it to your back, but it_ll do in a pinch. It_s old and fragile, so it_s quick to break.",
        "common_locations": [
            "Greater Hyrule"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/bokoblin_arm/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 5,
            "defense": 0
        }
    },
    {
        "id": 246,
        "name": "lizalfos arm",
        "description": "The arm of a Stalizalfos that continues to struggle even in death. It can be used as a weapon, but it_s very brittle. You can feel it wiggling when you strap it to your back...",
        "common_locations": [
            "Greater Hyrule"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lizalfos_arm/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 12,
            "defense": 0
        }
    },
    {
        "id": 247,
        "name": "korok leaf",
        "description": "A single swing of this giant, sturdy leaf can create a gust of wind strong enough to blow away light objects. These will sometimes fall off trees as they_re chopped down.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/korok_leaf/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 1,
            "defense": 0
        }
    },
    {
        "id": 248,
        "name": "farming hoe",
        "description": "A farming tool primarily used for tilling fields. Its fine craftsmanship is sturdy enough to withstand backbreaking fieldwork, but its battle applications are untested.",
        "common_locations": [
            "East Necluda",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/farming_hoe/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 16,
            "defense": 0
        }
    },
    {
        "id": 249,
        "name": "boat oar",
        "description": "Made for paddling boats, but it was made sturdy enough to fight strong currents. Maybe it_s useful for self-defense in a pinch.",
        "common_locations": [
            "East Necluda",
            "Necluda Sea"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/boat_oar/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 14,
            "defense": 0
        }
    },
    {
        "id": 250,
        "name": "woodcutter_s axe",
        "description": "A woodcutter_s tool of choice for felling trees. Its formidable weight and uneven balancing make it a slow, inefficient weapon.",
        "common_locations": [
            "West Necluda",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/woodcutters_axe/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 3,
            "defense": 0
        }
    },
    {
        "id": 251,
        "name": "double axe",
        "description": "This double-sided axe was designed with fighting in mind. It_s a bit unwieldy, so it requires a well-practiced technique to use efficiently.",
        "common_locations": [
            "West Necluda",
            "Gerudo Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/double_axe/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 18,
            "defense": 0
        }
    },
    {
        "id": 252,
        "name": "iron sledgehammer",
        "description": "This large iron sledgehammer was originally used for mining, but it works reasonably well as a weapon too.",
        "common_locations": [
            "Eldin Canyon",
            "Akkala Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/iron_sledgehammer/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 12,
            "defense": 0
        }
    },
    {
        "id": 253,
        "name": "giant boomerang",
        "description": "This massive boomerang requires two hands. Originally used for hunting, it was modified for use as a weapon. The blades on the inner curves make it a bit trick to wield.",
        "common_locations": [
            "West Necluda",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/giant_boomerang/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 25,
            "defense": 0
        }
    },
    {
        "id": 254,
        "name": "traveler_s claymore",
        "description": "A basic two-handed sword often wielded by aspiring adventurers. Its immense weight can knock enemies_ shields right out of their hands.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/travelers_claymore/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 10,
            "defense": 0
        }
    },
    {
        "id": 255,
        "name": "soldier_s claymore",
        "description": "A two-handed sword designed for combat. It_s heavy and hard to use but has decent build quality and durability.",
        "common_locations": [
            "Hyrule Field",
            "Faron Grasslands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/soldiers_claymore/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 20,
            "defense": 0
        }
    },
    {
        "id": 256,
        "name": "knight_s claymore",
        "description": "Only the most confident of Hyrule Castle_s knights carried this two-handed sword. Its cutting edge is finely honed.",
        "common_locations": [
            "Gerudo Desert",
            "Tabantha Frontier"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/knights_claymore/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 38,
            "defense": 0
        }
    },
    {
        "id": 257,
        "name": "royal claymore",
        "description": "A two-handed sword issued to the Hyrulean royal family_s immediate guard detail. Its powerful strikes are said to crush an opponent_s body and resolve alike.",
        "common_locations": [
            "Tabantha Frontier",
            "Gerudo Desert"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/royal_claymore/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 52,
            "defense": 0
        }
    },
    {
        "id": 258,
        "name": "silver longsword",
        "description": "Although the Zora prefer spears to swords, they made this two-handed weapon using a special metal. It found popularity among Hylians for its unique design.",
        "common_locations": [
            "Lanayru Great Spring",
            "Lanayru Wetlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/silver_longsword/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 22,
            "defense": 0
        }
    },
    {
        "id": 259,
        "name": "cobble crusher",
        "description": "A Goron-made two-handed weapon. It_s made from thick, hard metal and has no cutting edge, so it relies on its sheer weight to crush all opponents.",
        "common_locations": [
            "Eldin Canyon",
            "Eldin Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/cobble_crusher/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 15,
            "defense": 0
        }
    },
    {
        "id": 260,
        "name": "stone smasher",
        "description": "A two-handed weapon forged from a rare metal mined in Goron City. Its center of gravity is at its tip, so it uses centrifugal force and its sheer weight to smash opponents flat.",
        "common_locations": [
            "Eldin Canyon",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/stone_smasher/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 42,
            "defense": 0
        }
    },
    {
        "id": 261,
        "name": "boulder breaker",
        "description": "This two-handed weapon was once wielded by the Goron Champion Daruk. Daruk made swinging it around look easy, but a Hylian would need and immense amount of strength.",
        "common_locations": [
            "Eldin Canyon"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/boulder_breaker/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 60,
            "defense": 0
        }
    },
    {
        "id": 262,
        "name": "golden claymore",
        "description": "Only the most talented Gerudo sword fighters carry this two-handed sword. It_s actually much lighter than it appears and is surprisingly easy to wield.",
        "common_locations": [
            "Gerudo Highlands",
            "Hyrule Ridge"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/golden_claymore/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 28,
            "defense": 0
        }
    },
    {
        "id": 263,
        "name": "eightfold longblade",
        "description": "A single-edged sword seldom seen in Hyrule. This weapon is passed down through the Sheikah tribe and has an astonishingly shape edge ideal for slicing.",
        "common_locations": [
            "West Necluda",
            "Lanayru Great Spring"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/eightfold_longblade/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 32,
            "defense": 0
        }
    },
    {
        "id": 264,
        "name": "edge of duality",
        "description": "A curious double-edged sword crafted using Sheikah technology. It was originally made for Hyrulean knights unfamiliar with single-edged blades.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/edge_of_duality/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 50,
            "defense": 0
        }
    },
    {
        "id": 265,
        "name": "ancient bladesaw",
        "description": "This two-handed sword was forged using ancient Sheikah technology. Its unique rotating blades give it impressive cutting power that will slice enemies to shreds.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ancient_bladesaw/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 55,
            "defense": 0
        }
    },
    {
        "id": 266,
        "name": "rusty claymore",
        "description": "A two-handed sword not properly cared for. Although it can be used as a weapon, its durability is very low. Don_t expect it to last for more than a few strikes.",
        "common_locations": [
            "Hyrule Field",
            "Eldin Canyon"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/rusty_claymore/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 12,
            "defense": 0
        }
    },
    {
        "id": 267,
        "name": "royal guard_s claymore",
        "description": "The Sheikah used the very essence of ancient technology to forge this greatsword. It was designed to oppose the Calamity, but its low durability made it impractical in battle.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/royal_guards_claymore/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 72,
            "defense": 0
        }
    },
    {
        "id": 268,
        "name": "great flameblade",
        "description": "This magic-infused greatsword was forged in the fires of Death Mountain by Goron smiths in an ancient age. Attack when the blade glows red to expel flames.",
        "common_locations": [
            "Hyrule Field",
            "Eldin Canyon"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/great_flameblade/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 34,
            "defense": 0
        }
    },
    {
        "id": 269,
        "name": "great frostblade",
        "description": "This magic infused greatsword was forged by smelting ore found in the Hebra Mountains_ permafrost. Attack when the blade glows blue to expel freezing air.",
        "common_locations": [
            "Hebra Mountains",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/great_frostblade/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 30,
            "defense": 0
        }
    },
    {
        "id": 270,
        "name": "great thunderblade",
        "description": "This magic-infused greatsword was forged by the Hyrulean royal family using lightning from the Hyrule Hills. Attack when the blade glows golden to expel lightning.",
        "common_locations": [
            "Hyrule Field",
            "Tabantha Frontier"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/great_thunderblade/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 32,
            "defense": 0
        }
    },
    {
        "id": 271,
        "name": "boko bat",
        "description": "A clunky club made by a Bokoblin. If you swing it at an enemy_s shield it may be able to knock the shield out of your foe_s hand.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/boko_bat/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 6,
            "defense": 0
        }
    },
    {
        "id": 272,
        "name": "spiked boko bat",
        "description": "After much consideration by Bokoblins on how to improve the Boko bat, they simply attached sharp spikes to it. A skilled fighter can cause immense damage with this.",
        "common_locations": [
            "Faron Grasslands",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/spiked_boko_bat/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 18,
            "defense": 0
        }
    },
    {
        "id": 273,
        "name": "dragonbone boko bat",
        "description": "Used only by the toughest Bokoblin warriors, this Boko bat has been fortified by fossilized bone. It boasts a high durability and is strong enough to beat down powerful foes.",
        "common_locations": [
            "Hyrule Ridge",
            "Necluda Sea"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/dragonbone_boko_bat/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 36,
            "defense": 0
        }
    },
    {
        "id": 274,
        "name": "moblin club",
        "description": "A crudely fashioned club favored by Moblins. It_s carved from a sturdy tree but is sloppily made, so it breaks easily.",
        "common_locations": [
            "Gerudo Highlands",
            "Faron Grasslands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/moblin_club/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 9,
            "defense": 0
        }
    },
    {
        "id": 275,
        "name": "spiked moblin club",
        "description": "Animal bone has been affixed to this Moblin club to greatly improve its damage.",
        "common_locations": [
            "Hyrule Field",
            "Akkala Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/spiked_moblin_club/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 27,
            "defense": 0
        }
    },
    {
        "id": 276,
        "name": "dragonbone moblin club",
        "description": "The bone of an ancient beast has been affixed to this Moblin club, further increasing its damage. Moblins carrying these in battle are particularly dangerous.",
        "common_locations": [
            "Hebra Mountains",
            "Eldin Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/dragonbone_moblin_club/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 45,
            "defense": 0
        }
    },
    {
        "id": 277,
        "name": "ancient battle axe",
        "description": "A weapon used by Guardian Scouts. Its unique blade was forged using ancient technology. Although powerful, its unusual shape causes it to break easily.",
        "common_locations": [
            "Gerudo Desert",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ancient_battle_axe_i/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 30,
            "defense": 0
        }
    },
    {
        "id": 278,
        "name": "ancient battle axe+",
        "description": "This ancient battle axe_s damage output has been increased to maximum. It_s sharp enough to cut through almost anything, so it may have been used to forge new routes.",
        "common_locations": [
            "Akkala Highlands",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ancient_battle_axe_ii/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 45,
            "defense": 0
        }
    },
    {
        "id": 279,
        "name": "ancient battle axe++",
        "description": "This ancient battle axe_s damage output is scaled up to peak performance. Ancient technology makes it possible to enhance cutting power beyond metal weapons_ limits.",
        "common_locations": [
            "Hebra Mountains",
            "Gerudo Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ancient_battle_axe_iii/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 60,
            "defense": 0
        }
    },
    {
        "id": 280,
        "name": "lynel crusher",
        "description": "This Lynel-made two-handed weapon has been reinforced to increase its durability and striking power. Its overwhelming heft will crush your foe, shield and all.",
        "common_locations": [
            "Gerudo Highlands",
            "Tabantha Frontier"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lynel_crusher/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 36,
            "defense": 0
        }
    },
    {
        "id": 281,
        "name": "mighty lynel crusher",
        "description": "This Lynel-made two-handed weapon has been reinforced to increase its durability and striking power. Its overwhelming heft will crush your foe, shield and all.",
        "common_locations": [
            "Gerudo Highlands",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/mighty_lynel_crusher/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 54,
            "defense": 0
        }
    },
    {
        "id": 282,
        "name": "savage lynel crusher",
        "description": "This Lynel-made two-handed weapon is immensely heavy thank to a rare metal from Death Mountain_s peak. The power of its downward swing is in a class all of its own.",
        "common_locations": [
            "Hebra Mountains",
            "Eldin Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/savage_lynel_crusher/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 78,
            "defense": 0
        }
    },
    {
        "id": 283,
        "name": "windcleaver",
        "description": "This sword is favored by high-ranking members of the Yiga. When wielded by a proficient fighter, its unique shape cleaves the very wind and creates a vacuum.",
        "common_locations": [
            "Gerudo Highlands",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/windcleaver/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 40,
            "defense": 0
        }
    },
    {
        "id": 284,
        "name": "moblin arm",
        "description": "A Moblin bone that continues to move even after being detached from its body. The bone is thick enough to be used as a weapon but is extremely brittle and easily broken.",
        "common_locations": [
            "Greater Hyrule"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/moblin_arm/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 15,
            "defense": 0
        }
    },
    {
        "id": 285,
        "name": "wooden mop",
        "description": "Just a mop to the untrained eye, it excels at tidying up the place. But it owes its sturdy construction to a true craftsman, so it actually has some combat merit.",
        "common_locations": [
            "East Necluda",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/wooden_mop/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 5,
            "defense": 0
        }
    },
    {
        "id": 286,
        "name": "farmer_s pitchfork",
        "description": "A farming tool used to collect hay efficiently. It_s light enough to be used by anyone. The four prongs are very sharp.",
        "common_locations": [
            "East Necluda",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/farmers_pitchfork/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 7,
            "defense": 0
        }
    },
    {
        "id": 287,
        "name": "fishing harpoon",
        "description": "A fisherman_s tool that excels at catching large fish. Its particularly sharp spearhead makes it valuable as a weapon as well.",
        "common_locations": [
            "East Necluda",
            "Lake Hylia"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/fishing_harpoon/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 8,
            "defense": 0
        }
    },
    {
        "id": 288,
        "name": "throwing spear",
        "description": "A specialized spear weighted to excel as a throwing weapon. It_s perfectly balanced to be thrown harder than your average spear, able to pierce targets from a great distance.",
        "common_locations": [
            "West Necluda",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/throwing_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 6,
            "defense": 0
        }
    },
    {
        "id": 289,
        "name": "traveler_s spear",
        "description": "A spear used mainly by travelers to fend off wolves and other beasts. It_s easy to hold and simple to use.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/travelers_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 3,
            "defense": 0
        }
    },
    {
        "id": 290,
        "name": "soldier_s spear",
        "description": "A long spear once used by the guards of Hyrule Castle. Easy to use but difficult to master. The iron tip is very sturdy, and the shaft will not burn when exposed to flame.",
        "common_locations": [
            "Hyrule Field",
            "Faron Grasslands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/soldiers_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 7,
            "defense": 0
        }
    },
    {
        "id": 291,
        "name": "knight_s halberd",
        "description": "A spear used by knights adept in mounted combat. The spearhead is modeled after an axe.",
        "common_locations": [
            "Tabantha Frontier",
            "Gerudo Desert"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/knights_halberd/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 13,
            "defense": 0
        }
    },
    {
        "id": 292,
        "name": "royal halberd",
        "description": "This spear was issued to the knights who guarded Hyrule Castle_s throne room. Its ornate design was applied by a craftsman in service to the royal family.",
        "common_locations": [
            "Gerudo Highlands",
            "Tabantha Frontier"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/royal_halberd/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 26,
            "defense": 0
        }
    },
    {
        "id": 293,
        "name": "forest dweller_s spear",
        "description": "The Koroks made this spear for Hylians. The shaft is made from a light, sturdy wood, offering ease of use. The spearhead is made from a much harder wood, offering strength.",
        "common_locations": [
            "Great Hyrule Forest",
            "Hyrule Ridge"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/forest_dwellers_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 11,
            "defense": 0
        }
    },
    {
        "id": 294,
        "name": "zora spear",
        "description": "This spear is a Zora_s weapon of choice. It_s lighter than it looks due to being made from a special metal and is used by the Zora for both fishing and protecting their domain.",
        "common_locations": [
            "Lanayru Great Spring",
            "Lake Hylia"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/zora_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 9,
            "defense": 0
        }
    },
    {
        "id": 295,
        "name": "silverscale spear",
        "description": "A most skilled Zora fighters wield this spear. Its beautiful fish-tail design belies its impressive strength; the spearhead can piece even the toughest scales.",
        "common_locations": [
            "Akkala Highlands",
            "Lanayru Great Spring"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/silverscale_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 12,
            "defense": 0
        }
    },
    {
        "id": 296,
        "name": "ceremonial trident",
        "description": "A spear modeled after the Lightscale trident wielded by the Zora Champion Mipha. They may be identical in appearance, but this spear_s strength and durability are inferior.",
        "common_locations": [
            "Lanayru Great Spring"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ceremonial_trident/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 14,
            "defense": 0
        }
    },
    {
        "id": 297,
        "name": "lightscale trident",
        "description": "A spear of peerless grace cherished by the Zora Champion Mipha. Although Mipha specialized in healing abilities, her spearmanship was in a class all its own.",
        "common_locations": [
            "Lanayru Great Spring"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lightscale_trident/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 22,
            "defense": 0
        }
    },
    {
        "id": 298,
        "name": "drillshaft",
        "description": "Goron artisans used recycled metal to forge this weapon. The tip is made from an old excavation bore, which affords it unmatched piercing capabilities.",
        "common_locations": [
            "Eldin Canyon",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/drillshaft/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 14,
            "defense": 0
        }
    },
    {
        "id": 299,
        "name": "feathered spear",
        "description": "Its lightweight design is a hallmark of Rito craftsmanship. It_s made from light and sturdy materials, which afford Rito warriors ease of use during aerial combat.",
        "common_locations": [
            "Tabantha Frontier",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/feathered_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 10,
            "defense": 0
        }
    },
    {
        "id": 300,
        "name": "gerudo spear",
        "description": "This spear_s center of gravity is in its tip, making it a bit unwieldy for the average fighter. But in the hands of a skilled Gerudo warrior, it_s a weapon of reliable strength.",
        "common_locations": [
            "Gerudo Desert",
            "Gerudo Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/gerudo_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 16,
            "defense": 0
        }
    },
    {
        "id": 301,
        "name": "serpentine spear",
        "description": "The spearhead of this weapon is uniquely Sheikah in design. Spear masters of the Sheikah tribe can use the crescent shape to snag their opponents and deliver brutal cuts.",
        "common_locations": [
            "East Necluda",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/serpentine_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 12,
            "defense": 0
        }
    },
    {
        "id": 302,
        "name": "ancient spear",
        "description": "This spear is the result of countless hours of research into the ancient technology used by Guardians. The glowing spearhead has piercing potential.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ancient_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 30,
            "defense": 0
        }
    },
    {
        "id": 303,
        "name": "rusty halberd",
        "description": "A rusty polearm likely used by knights from an age past. The spearhead is in bad shape due to prolonged exposure to the elements, so its durability is low.",
        "common_locations": [
            "Hyrule Field",
            "Great Hyrule Forest"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/rusty_halberd/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 5,
            "defense": 0
        }
    },
    {
        "id": 304,
        "name": "royal guard_s spear",
        "description": "This Sheikah-made spear was created using ancient technology to combat the Calamity. Its attack power is very high, but a critical design flaw left it with poor durability.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/royal_guards_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 32,
            "defense": 0
        }
    },
    {
        "id": 305,
        "name": "flamespear",
        "description": "A magical spear forged in the magma of Death Mountain. Attack when the blade glows to expel powerful flames.",
        "common_locations": [
            "Hyrule Field",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/flamespear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 24,
            "defense": 0
        }
    },
    {
        "id": 306,
        "name": "frostspear",
        "description": "A magical spear forged from ancient ice taken from the Hebra Mountains. Attack when the blade glows blue to chill the air and freeze your foe.",
        "common_locations": [
            "Hebra Mountains",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/frostspear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 20,
            "defense": 0
        }
    },
    {
        "id": 307,
        "name": "thunderspear",
        "description": "A magical spear that contains thunder from Thundra Plateau in its tip. Attack when the blade glows with a golden light to unleash an electric attack.",
        "common_locations": [
            "Hyrule Ridge",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/thunderspear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 22,
            "defense": 0
        }
    },
    {
        "id": 308,
        "name": "boko spear",
        "description": "A spear haphazardly carved from a large tree branch. It looks like its original intent was for skewering meat and cooking it, but it does have some combat merit as well.",
        "common_locations": [
            "West Necluda",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/boko_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 2,
            "defense": 0
        }
    },
    {
        "id": 309,
        "name": "spiked boko spear",
        "description": "A Boko spear enhanced with sharpened animal bones. It_s light, easy to use, and deals a decent amount of damage.",
        "common_locations": [
            "Faron Grasslands",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/spiked_boko_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 6,
            "defense": 0
        }
    },
    {
        "id": 310,
        "name": "dragonbone boko spear",
        "description": "This Boko spear has been strengthened with fossilized bones. The bones are positioned outward so the fangs bite at the opponent. Beware Bokoblins carrying this weapon.",
        "common_locations": [
            "Necluda Sea",
            "Hyrule Ridge"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/dragonbone_boko_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 12,
            "defense": 0
        }
    },
    {
        "id": 311,
        "name": "moblin spear",
        "description": "This wooden spear is most often used by Moblins. It_s made from a hastily whittled tree, so its stabbing power and durability are both pretty low.",
        "common_locations": [
            "Faron Grasslands",
            "Gerudo Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/moblin_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 4,
            "defense": 0
        }
    },
    {
        "id": 312,
        "name": "spiked moblin spear",
        "description": "This Moblin-made spear uses a horned animal bone as the spearhead. Like many Moblin weapons it_s sloppily made, but this one packs some respective piercing power.",
        "common_locations": [
            "Gerudo Highlands",
            "Akkala Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/spiked_moblin_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 9,
            "defense": 0
        }
    },
    {
        "id": 313,
        "name": "dragonbone moblin spear",
        "description": "This spear is a fan favorite among Moblins. The spearhead is made from fossilized bones adorned with spikes, which greatly increases its stabbing power.",
        "common_locations": [
            "Hebra Mountains",
            "Eldin Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/dragonbone_moblin_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 15,
            "defense": 0
        }
    },
    {
        "id": 314,
        "name": "lizal spear",
        "description": "The brutal, ripping edge of this weapon_s spearhead is a distinctly Lizalfos design. Its low durability doesn_t lend itself to extended use.",
        "common_locations": [
            "Lanayru Wetlands",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lizal_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 7,
            "defense": 0
        }
    },
    {
        "id": 315,
        "name": "enhanced lizal spear",
        "description": "Judging by the harpoon-like spearhead of this Lizalfos-made spear, the Lizalfos use it for fishing as well as combat. Try not to get caught on the wrong end of its barbs.",
        "common_locations": [
            "Tabantha Frontier",
            "Gerudo Desert"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/enhanced_lizal_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 12,
            "defense": 0
        }
    },
    {
        "id": 316,
        "name": "forked lizal spear",
        "description": "Skilled Lizalfos warriors tend to favor this spear. What it lacks in piercing power, it makes up for with the brutal wounds its dual ripping blades will inflict.",
        "common_locations": [
            "Eldin Canyon",
            "Akkala Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/forked_lizal_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 18,
            "defense": 0
        }
    },
    {
        "id": 317,
        "name": "guardian spear",
        "description": "Wielded by Guardian Scouts, this spear has a high piercing power and is a testament to the Sheikah_s high level of technology. The spearhead appears only when brandished.",
        "common_locations": [
            "Hyrule Field",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_spear_i/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 10,
            "defense": 0
        }
    },
    {
        "id": 318,
        "name": "guardian spear+",
        "description": "The tip of this Guardian spear has been enlarged and strengthened. It_s a bit shorter than your average spear, perhaps to facilitate use in tight spaces.",
        "common_locations": [
            "Gerudo Highlands",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_spear_ii/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 15,
            "defense": 0
        }
    },
    {
        "id": 319,
        "name": "guardian spear++",
        "description": "This guardian spear_s output has been boosted to the maximum. The spearhead is designed for optimal stabbing, capable of easily piercing most armor.",
        "common_locations": [
            "Hebra Mountains",
            "Akkala Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_spear_iii/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 20,
            "defense": 0
        }
    },
    {
        "id": 320,
        "name": "lynel spear",
        "description": "The crescent-shaped spearhead of this Lynel-made weapon gives it poor balance, making it difficult to wield. Lynels, however, can swing it effectively with one hand.",
        "common_locations": [
            "Gerudo Highlands",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lynel_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 14,
            "defense": 0
        }
    },
    {
        "id": 321,
        "name": "mighty lynel spear",
        "description": "The weight and cutting edge of this Lynel-made spear have both been enhanced. It_s immensely heavy for a Hylian, but a Lynel can cleave through rock with a single swing.",
        "common_locations": [
            "Great Hyrule Forest",
            "Deep Akkala"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/mighty_lynel_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 20,
            "defense": 0
        }
    },
    {
        "id": 322,
        "name": "savage lynel spear",
        "description": "White-haired Lynels favor this brutal spear. Its axe-like spearhead and exceptional weight give it absolute destructive power.",
        "common_locations": [
            "Gerudo Highlands",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/savage_lynel_spear/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 30,
            "defense": 0
        }
    },
    {
        "id": 323,
        "name": "bow of light",
        "description": "Princess Zelda gave you this bow and arrow for the battle with Dark Beast Ganon. When wielded by the hero, it fires arrows of pure light strong enough to oppose the Calamity.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/bow_of_light/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 100,
            "defense": 0
        }
    },
    {
        "id": 324,
        "name": "wooden bow",
        "description": "This wooden bow may not be the most reliable for battling monsters, but is excellent for hunting small animals.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/wooden_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 4,
            "defense": 0
        }
    },
    {
        "id": 325,
        "name": "traveler_s bow",
        "description": "A small bow used by travelers for protection. It doesn_t do a lot of damage, but it can be used to attack foes from a distance.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/travelers_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 5,
            "defense": 0
        }
    },
    {
        "id": 326,
        "name": "soldier_s bow",
        "description": "A bow designed for armed conflict. Inflicts more damage than a civilian bow, but it will still burn if it touches fire.",
        "common_locations": [
            "Hyrule Field",
            "Faron Grasslands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/soldiers_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 14,
            "defense": 0
        }
    },
    {
        "id": 327,
        "name": "knight_s bow",
        "description": "The sturdy metal construction of this bow offers superior durability, while its lack of firing quirks makes it quite reliable. Once favored by the knights at Hyrule Castle.",
        "common_locations": [
            "Gerudo Desert",
            "Tabantha Frontier"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/knights_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 26,
            "defense": 0
        }
    },
    {
        "id": 328,
        "name": "royal bow",
        "description": "In the past, the king of Hyrule presented this bow to only the most talented archers in the land. Its combat capabilities are as impressive as its extravagant design.",
        "common_locations": [
            "Tabantha Frontier",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/royal_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 38,
            "defense": 0
        }
    },
    {
        "id": 329,
        "name": "forest dweller_s bow",
        "description": "The Koroks made this bow for Hylians. It_s crafted from flexible wood and uses sturdy vines for the bowstring. Its construction may be simple, but it fires multiple arrows at once.",
        "common_locations": [
            "Tabantha Frontier",
            "Hyrule Ridge"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/forest_dwellers_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 15,
            "defense": 0
        }
    },
    {
        "id": 330,
        "name": "silver bow",
        "description": "A bow favored by the Zora for fishing. It doesn_t boast the highest firepower, but the special metal it_s crafted from prioritizes durability.",
        "common_locations": [
            "Lanayru Great Spring",
            "Akkala Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/silver_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 15,
            "defense": 0
        }
    },
    {
        "id": 331,
        "name": "swallow bow",
        "description": "This bow is a favorite among Rito warriors. The bowstring has been specially engineered for aerial combat, which allows it to be drawn faster than a normal bow.",
        "common_locations": [
            "Tabantha Frontier",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/swallow_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 9,
            "defense": 0
        }
    },
    {
        "id": 332,
        "name": "falcon bow",
        "description": "A highly refined Rito-made bow created by a master Rito craftsman. Rito warriors favor it for its superior rate of fire, which helps them excel even further at aerial combat.",
        "common_locations": [
            "Tabantha Frontier",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/falcon_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 20,
            "defense": 0
        }
    },
    {
        "id": 333,
        "name": "great eagle bow",
        "description": "A bow without equal wielded by the Rito Champion, Revali. It_s said that Revali could loose arrows with the speed of a gale, making him supreme in aerial combat.",
        "common_locations": [
            "Tabantha Frontier"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/great_eagle_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 28,
            "defense": 0
        }
    },
    {
        "id": 334,
        "name": "golden bow",
        "description": "This Gerudo-made bow is popular for the fine ornamentations along its limbs. Designed for hunting and warfare alike, this bow was engineered to strike distant targets.",
        "common_locations": [
            "Gerudo Highlands",
            "Gerudo Desert"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/golden_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 14,
            "defense": 0
        }
    },
    {
        "id": 335,
        "name": "phrenic bow",
        "description": "A bow passed down through the Sheikah tribe. Concentrating before drawing the string will allow you to target distant enemies as easily as those nearby.",
        "common_locations": [
            "West Necluda",
            "Lake Hylia"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/phrenic_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 10,
            "defense": 0
        }
    },
    {
        "id": 336,
        "name": "ancient bow",
        "description": "This bow is the result of Robbie_s research. Ancient Sheikah technology affords it heightened functionality. Arrows fired from it travel in a perfectly straight line.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ancient_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 44,
            "defense": 0
        }
    },
    {
        "id": 337,
        "name": "royal guard_s bow",
        "description": "This prototype Sheikah-made bow was designed to fight the Great Calamity. Made with ancient technology, it boast a high rate of fire and firepower, but has a low durability.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/royal_guards_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 50,
            "defense": 0
        }
    },
    {
        "id": 338,
        "name": "boko bow",
        "description": "A basic Bokoblin bow made from wood. It_s made by taking any tree branch and just tying a string to either end, so don_t expect much in the way of combat effectiveness.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/boko_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 4,
            "defense": 0
        }
    },
    {
        "id": 339,
        "name": "spiked boko bow",
        "description": "An upgraded Boko bow bound with animal bone to boost its durability and firepower. Its craftsmanship is sloppy, but it_s light and easy to use.",
        "common_locations": [
            "Faron Grasslands",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/spiked_boko_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 12,
            "defense": 0
        }
    },
    {
        "id": 340,
        "name": "dragon bone boko bow",
        "description": "A Boko bow reinforced by fossils. Bokoblins handpicked the materials it_s made from, so it boasts a respectable firepower.",
        "common_locations": [
            "Hyrule Ridge",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/dragon_bone_boko_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 24,
            "defense": 0
        }
    },
    {
        "id": 341,
        "name": "lizal bow",
        "description": "A wooden bow created by Lizalfos. It_s reinforced by the bones of a large fish - a marked improvement over any standard wooden bow.",
        "common_locations": [
            "Lanayru Great Spring",
            "Lanayru Wetlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lizal_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 14,
            "defense": 0
        }
    },
    {
        "id": 342,
        "name": "strengthened lizal bow",
        "description": "A Lizal bow with a grip reinforced by metal. The body is made from the branches of a flexible tree that grows near water, which offers some serious destructive power.",
        "common_locations": [
            "Tabantha Frontier",
            "Gerudo Desert"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/strengthened_lizal_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 25,
            "defense": 0
        }
    },
    {
        "id": 343,
        "name": "steel lizal bow",
        "description": "This bow is wielded by Lizalfos who are expert marksmen. The metal that reinforces much of the weapon adds some additional weight but offers heightened durability.",
        "common_locations": [
            "Hebra Mountains",
            "Akkala Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/steel_lizal_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 36,
            "defense": 0
        }
    },
    {
        "id": 344,
        "name": "lynel bow",
        "description": "A Lynel-made bow crafted from rough metal. True to the vicious nature of Lynel weaponry, it fires a spread of multiple arrows at once. Ideal for taking down quick-moving targets.",
        "common_locations": [
            "Gerudo Highlands",
            "Lanayru Great Spring"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lynel_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 10,
            "defense": 0
        }
    },
    {
        "id": 345,
        "name": "mighty lynel bow",
        "description": "This massive Lynel bow sports a bowstring made from a metal so tough, mere Hylians have trouble drawing it back.",
        "common_locations": [
            "Hyrule Field",
            "Deep Akkala"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/mighty_lynel_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 20,
            "defense": 0
        }
    },
    {
        "id": 346,
        "name": "savage lynel bow",
        "description": "This Lynel bow is made from a special steel found at the peak of Death Mountain. It has tremendous stopping power and can pierce think armor as easily as thin paper.",
        "common_locations": [
            "Hebra Mountains",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/savage_lynel_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 32,
            "defense": 0
        }
    },
    {
        "id": 347,
        "name": "duplex bow",
        "description": "A bow favored by the skilled archers of the Yiga Clan. It_s been engineered to fire two arrows at once to ensure your target comes to a swift a none-two-pleasant halt.",
        "common_locations": [
            "Gerudo Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/duplex_bow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 14,
            "defense": 0
        }
    },
    {
        "id": 348,
        "name": "arrow",
        "description": "A common arrow. Its shaft was carved from the wood of a sturdy tree.",
        "common_locations": [
            "Hyrule Field",
            "Eldin Canyon"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/arrow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": "null",
            "defense": "null"
        }
    },
    {
        "id": 349,
        "name": "fire arrow",
        "description": "An arrow imbued with the power of fire. It breaks apart on impact, igniting objects in the immediate area. It_s incredibly effective against cold things.",
        "common_locations": [
            "Hyrule Field",
            "Eldin Canyon"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/fire_arrow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": "null",
            "defense": "null"
        }
    },
    {
        "id": 350,
        "name": "ice arrow",
        "description": "An arrow imbued with the power of ice. It breaks apart on impact, freezing objects in the immediate area. It_s incredibly effective against hot things.",
        "common_locations": [
            "Hyrule Field",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ice_arrow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": "null",
            "defense": "null"
        }
    },
    {
        "id": 351,
        "name": "shock arrow",
        "description": "An arrow imbued with the power of electricity. It breaks apart on impact, channeling electricity into nearby objects. It_s incredibly effective against metal or anything wet.",
        "common_locations": [
            "Lanayru Great Spring",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/shock_arrow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": "null",
            "defense": "null"
        }
    },
    {
        "id": 352,
        "name": "bomb arrow",
        "description": "A powerful arrow designed to destroy monsters. The explosive powder packed into the tip ignites on impact, dealing massive damage to anything caught in the blast.",
        "common_locations": [
            "Hyrule Field",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/bomb_arrow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": "null",
            "defense": "null"
        }
    },
    {
        "id": 353,
        "name": "ancient arrow",
        "description": "An arrow created using ancient technology. To be struck with one is to be consigned to oblivion in an instant. It deals devastating damage\u2014even against Guardians.",
        "common_locations": [
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ancient_arrow/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": "null",
            "defense": "null"
        }
    },
    {
        "id": 354,
        "name": "hylian shield",
        "description": "A shield passes down through the Hylian royal family, along with the legend of the hero who wielded it. Its defensive capabilities and durability outshine all other shields.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/hylian_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 90
        }
    },
    {
        "id": 355,
        "name": "pot lid",
        "description": "The lid of a large soup pot. It smells vaguely of poultry broth... Yum! It can take quite a beating before breaking.",
        "common_locations": [
            "Hyrule Field",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/pot_lid/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 1
        }
    },
    {
        "id": 356,
        "name": "wooden shield",
        "description": "This lightweight, simple shield is ideal for less-experienced fighters. It can withstand light attacks, but blocking stronger blows is not recommended.",
        "common_locations": [
            "Hyrule Field",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/wooden_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 2
        }
    },
    {
        "id": 357,
        "name": "emblazoned shield",
        "description": "This shield features a traditional design from Necluda. Its combat capabilities aren_t much better than the standard wooden shield, but it found popularity for its design.",
        "common_locations": [
            "East Necluda",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/emblazoned_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 3
        }
    },
    {
        "id": 358,
        "name": "hunter_s shield",
        "description": "Favored by hunters for its rabbit design, which is said to bring luck on hunts. It_s easy to use, but its durability leaves something to be desired.",
        "common_locations": [
            "Hebra Mountains",
            "Lanayru Wetlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/hunters_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 3
        }
    },
    {
        "id": 359,
        "name": "fisherman_s shield",
        "description": "Often carried by fishermen for its fish design, which represents hope for a good catch. Its light wooden construction makes it convenient to take on a boat.",
        "common_locations": [
            "East Necluda",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/fishermans_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 3
        }
    },
    {
        "id": 360,
        "name": "traveler_s shield",
        "description": "A sturdy shield loved by many an adventurer. It is made of animal hide and sturdy wood and is best suited to defending against weak monsters or animals.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/travelers_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 4
        }
    },
    {
        "id": 361,
        "name": "soldier_s shield",
        "description": "A shield once used by the guards of Hyrule Castle. It_s easy to handle, but its core is made of wood, so it can catch fire.",
        "common_locations": [
            "Tabantha Frontier",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/soldiers_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 16
        }
    },
    {
        "id": 362,
        "name": "knight_s shield",
        "description": "A shield favored by the knights who served the Hyrulean royal family. Its sturdy metal construction makes it quite durable, but its weight requires decent skill to wield.",
        "common_locations": [
            "Hebra Mountains",
            "Eldin Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/knights_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 40
        }
    },
    {
        "id": 363,
        "name": "royal shield",
        "description": "A shield issued to the Hyrulean royal family_s immediate guard detail. It boasts a high defense, but these days it_s more a collector_s item due to its ornamentation.",
        "common_locations": [
            "Hyrule Field",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/royal_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 55
        }
    },
    {
        "id": 364,
        "name": "forest dweller_s shield",
        "description": "The Koroks made this shield specifically for Hylians. It_s made from the finest hard wood of trees that only grow in the Korok forest, so it_s sturdier than it looks.",
        "common_locations": [
            "Great Hyrule Forest"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/forest_dwellers_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 30
        }
    },
    {
        "id": 365,
        "name": "silver shield",
        "description": "A Zora-made shield adorned with intricate ornamentation. It_s said that true masters of this shield can redirect attacks as a rock redirects rushing water.",
        "common_locations": [
            "Lanayru Great Spring",
            "Lake Hylia"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/silver_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 18
        }
    },
    {
        "id": 366,
        "name": "kite shield",
        "description": "Rito warriors cherish this shield. Its unique shape is designed with mid-battle flight in mind to facilitate aerial combat.",
        "common_locations": [
            "Hebra Mountains",
            "Tabantha Frontier"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/kite_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 14
        }
    },
    {
        "id": 367,
        "name": "gerudo shield",
        "description": "The design of this metal shield has changed over time to match the Gerudo_s sword-and-shield fighting style. It_s favored by soldiers and travelers alike.",
        "common_locations": [
            "Gerudo Desert",
            "Gerudo Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/gerudo_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 20
        }
    },
    {
        "id": 368,
        "name": "radiant shield",
        "description": "This extravagant shield is presented to Gerudo warriors who rise to the rank of captain. Its apparent opulence is rivaled only by its combat capabilities.",
        "common_locations": [
            "Gerudo Desert",
            "Gerudo Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/radiant_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 35
        }
    },
    {
        "id": 369,
        "name": "daybreaker",
        "description": "This shield was cherished by the Gerudo Champion Urbosa. The gold used to make it was handpicked to ensure a design that is both lightweight and very durable.",
        "common_locations": [
            "Gerudo Desert"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/daybreaker/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 48
        }
    },
    {
        "id": 370,
        "name": "shield of the mind_s eye",
        "description": "A small Sheikah-made shield. Its design is intended to decrease blind spots without sacrificing too much defense.",
        "common_locations": [
            "West Necluda",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/shield_of_the_minds_eye/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 16
        }
    },
    {
        "id": 371,
        "name": "ancient shield",
        "description": "This shield was made using ancient Sheikah technology. Its surface glows blue when raised in defense. Enhanced functionality allows it to deflect Guardian beams.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ancient_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 70
        }
    },
    {
        "id": 372,
        "name": "rusty shield",
        "description": "It_s likely that this rusty old shield once belonged to a knight. It still has some defensive capabilities, but its usefulness has been worn down by time.",
        "common_locations": [
            "Hyrule Field",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/rusty_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 3
        }
    },
    {
        "id": 373,
        "name": "royal guard_s shield",
        "description": "This shield was forged using ancient Sheikah technology. It boasts extremely high stopping power, but its structural weakness made its low durability impractical for combat.",
        "common_locations": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/royal_guards_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 70
        }
    },
    {
        "id": 374,
        "name": "boko shield",
        "description": "A Bokoblin-made shield created by attaching a handhold to any flat tree bark picked up off the ground. It_s pretty shoddy, so don_t expect it to last very long.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/boko_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 3
        }
    },
    {
        "id": 375,
        "name": "spiked boko shield",
        "description": "A Boko shield made of slightly stronger wood and reinforced with animal bones.",
        "common_locations": [
            "Faron Grasslands",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/spiked_boko_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 10,
            "defense": 0
        }
    },
    {
        "id": 376,
        "name": "dragonbone boko shield",
        "description": "This Boko shield is reinforced with fossilized bone. Its defensive capabilities are respectable, but its predictably slipshod craftsmanship spells low durability.",
        "common_locations": [
            "Hyrule Ridge",
            "Necluda Sea"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/dragonbone_boko_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 25
        }
    },
    {
        "id": 377,
        "name": "lizal shield",
        "description": "A common shield found among the Lizalfos. It_s made of metal, but its sloppy craftsmanship offers poor durability.",
        "common_locations": [
            "Lake Hylia",
            "East Necluda"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lizal_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 15
        }
    },
    {
        "id": 378,
        "name": "reinforced lizal shield",
        "description": "This Lizal shield has been strengthened by adding a different type of metal to the mix. The edge is lined with spikes, so handle with care.",
        "common_locations": [
            "Tabantha Frontier",
            "Gerudo Desert"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/reinforced_lizal_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 22
        }
    },
    {
        "id": 379,
        "name": "steel lizal shield",
        "description": "This Lizal shield is adorned with several metal shells as a means of reinforcement. Its defensive capabilities are high, but its weight requires a skilled soldier to bear.",
        "common_locations": [
            "Hebra Mountains",
            "Akkala Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/steel_lizal_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 35
        }
    },
    {
        "id": 380,
        "name": "guardian shield",
        "description": "A shield made with ancient Sheikah technology. It can deflect a Guardian Scout_s beam.",
        "common_locations": [
            "West Necluda",
            "Lanayru Great Spring"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_shield_i/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 18
        }
    },
    {
        "id": 381,
        "name": "guardian shield+",
        "description": "This larger version of a Guardian shield has had its output level boosted. Its defensive capabilities are comparable to those of a metal shield_s.",
        "common_locations": [
            "East Necluda",
            "Faron Grasslands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_shield_ii/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 30
        }
    },
    {
        "id": 382,
        "name": "guardian shield++",
        "description": "The output level of this shield has been boosted to a maximum. Its combat capabilities surpass those of metallic shields, and it can deflect Guardian Scout beams.",
        "common_locations": [
            "Gerudo Highlands",
            "Akkala Highlands"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_shield_iii/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 42
        }
    },
    {
        "id": 383,
        "name": "lynel shield",
        "description": "A sturdy shield favored by Lynels for its defensive and offensive capabilities. First and foremost a shield, but the bladed edges can deal slashing attacks when deflecting.",
        "common_locations": [
            "Lanayru Great Spring",
            "Hyrule Field"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lynel_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 30
        }
    },
    {
        "id": 384,
        "name": "mighty lynel shield",
        "description": "This Lynel-made shield has been reinforced with armor and even more blades. Stronger in both defense and offense, it can tear through basic armor when deflecting.",
        "common_locations": [
            "Hyrule Field",
            "Lanayru Great Spring"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/mighty_lynel_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 44
        }
    },
    {
        "id": 385,
        "name": "savage lynel shield",
        "description": "This ultimate Lynel shield is used only by the white-haired Lynels. It excels at defending against even the most brutal of attacks and cutting down powerful foes when deflecting.",
        "common_locations": [
            "Hyrule Field",
            "Hebra Mountains"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/savage_lynel_shield/image",
        "category": "equipment",
        "dlc": "false",
        "properties": {
            "attack": 0,
            "defense": 62
        }
    }
]

, 'materials' :

[
    {
        "id": 165,
        "name": "apple",
        "description": "A common fruit found on trees all around Hyrule. Eat it fresh, or cook it to increase its effect.",
        "common_locations": [
            "Hyrule Field",
            "East Necluda"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/apple/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 166,
        "name": "palm fruit",
        "description": "Fruit from palm trees that grow near the ocean. It doesn_t offer any special effects but will increase your heart recovery when used as an ingredient.",
        "common_locations": [
            "East Necluda",
            "Gerudo Desert"
        ],
        "hearts_recovered": 1.0,
        "cooking_effect": "",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/palm_fruit/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 167,
        "name": "wildberry",
        "description": "A fruit that grows in cold, snowy regions known for its tangy, sweet flavor. It doesn_t offer any special effects, but it_s a popular cooking ingredient.",
        "common_locations": [
            "Gerudo Highlands",
            "Hebra Mountains"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/wildberry/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 168,
        "name": "hearty durian",
        "description": "This fruit_s mighty odor has earned it the nickname \"king of fruits.\" It offers immense restorative powers; dishes cooked with it will temporarily increase your maximum hearts.",
        "common_locations": [
            "West Necluda",
            "Faron Grasslands"
        ],
        "hearts_recovered": 3.0,
        "cooking_effect": "extra hearts",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/hearty_durian/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 169,
        "name": "hydromelon",
        "description": "This resilient fruit can flourish even in the heat of the desert. The hydrating liquid inside provides a cooling effect that, when cooked, increases your heat resistance.",
        "common_locations": [
            "Gerudo Desert",
            "Faron Grasslands"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "heat resistance",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/hydromelon/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 170,
        "name": "spicy pepper",
        "description": "This pepper is exploding with spice. Cook with it to create dishes that will raise your body temperature and help you withstand the cold.",
        "common_locations": [
            "Gerudo Desert",
            "Tabantha Frontier"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "cold resistance",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/spicy_pepper/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 171,
        "name": "voltfruit",
        "description": "Cacti found in the Gerudo Desert bear this sweet fruit. It_s naturally insulated, so when cooked into a dish, it provides resistance against electricity.",
        "common_locations": [
            "Gerudo Desert",
            "Gerudo Highlands"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "shock resistance",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/voltfruit/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 172,
        "name": "fleet-lotus seeds",
        "description": "The plant that bears these seeds grows near deep water. The roots draw nutrients from the water, which boosts your movement speed when the seeds are cooked into a dish.",
        "common_locations": [
            "Lanayru Wetlands",
            "Lanayru Great Spring"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "speed up",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/fleet-lotus_seeds/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 173,
        "name": "mighty bananas",
        "description": "This fruit grows mainly in tropical forests of the Faron region. When it_s used as an ingredient, the resulting dish will temporarily increase your attack power.",
        "common_locations": [
            "Faron"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "attack up",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/mighty_bananas/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 174,
        "name": "hylian shroom",
        "description": "A common mushroom found near trees around Hyrule. Eat it to restore half a heart.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/hylian_shroom/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 175,
        "name": "endura shroom",
        "description": "A rare yellowish-orange mushroom. Cook it before eating to temporarily increase your stamina limit.",
        "common_locations": [
            "Hyrule Ridge",
            "Hyrule Field"
        ],
        "hearts_recovered": 1.0,
        "cooking_effect": "extra stamina",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/endura_shroom/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 176,
        "name": "stamella shroom",
        "description": "A green mushroom that grows near trees in the forest. It_s chock-full of natural energy. Cook it to release its stamina-restoration properties.",
        "common_locations": [
            "Hyrule Ridge",
            "Hyrule Field"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "stamina recovery",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/stamella_shroom/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 177,
        "name": "hearty truffle",
        "description": "This rare mushroom has a rich scent. Cook it before eating to temporarily increase your maximum hearts.",
        "common_locations": [
            "Great Hyrule Forest",
            "Hyrule Field"
        ],
        "hearts_recovered": 2.0,
        "cooking_effect": "extra hearts",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/hearty_truffle/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 178,
        "name": "big hearty truffle",
        "description": "Years of going unpicked have allowed this hearty truffle to grow quite large. It_s chock- full of nutrients. When cooked into a dish, it temporarily increases your maximum hearts.",
        "common_locations": [
            "Hebra Mountains",
            "Great Hyrule Forest"
        ],
        "hearts_recovered": 3.0,
        "cooking_effect": "extra hearts",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/big_hearty_truffle/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 179,
        "name": "chillshroom",
        "description": "Often found at the base of pine trees in cold climates, these mushrooms are cool to the touch and can be used to cook dishes that allow you to stay cool even in arid regions.",
        "common_locations": [
            "Hebra Mountains",
            "Mount Lanayru"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "heat resistance",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/chillshroom/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 180,
        "name": "sunshroom",
        "description": "A bright red mushroom that grows in hot climates. Imbued with the power of heat, they can be used to cook dishes that will allow you endure the bitter cold.",
        "common_locations": [
            "Eldin Canyon",
            "Gerudo Highlands"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "cold resistance",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/sunshroom/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 181,
        "name": "zapshroom",
        "description": "This mushroom grows wild in the Gerudo region. The cap is naturally insulated, so when used in cooking, it will offer protection against electricity.",
        "common_locations": [
            "Deep Akkala",
            "Gerudo Highlands"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "shock resistance",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/zapshroom/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 182,
        "name": "rushroom",
        "description": "A mushroom that can grow almost anywhere but prefers ceilings and sheer cliffs. Cook it before eating to temporarily increase your movement speed.",
        "common_locations": [
            "Gerudo Highlands",
            "Hyrule Ridge"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "speed up",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/rushroom/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 183,
        "name": "razorshroom",
        "description": "This mushroom is known for the natural slice in its cap. Eating it fosters your competitive spirit. Use it when cooking to prepare a dish that will increase your strength.",
        "common_locations": [
            "Great Hyrule Forest",
            "Tabantha Frontier"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "attack up",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/razorshroom/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 184,
        "name": "ironshroom",
        "description": "The cap of this mushroom is very hard. Use it when cooking to prepare a dish that increases you defense.",
        "common_locations": [
            "West Necluda",
            "East Necluda"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "defense up",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ironshroom/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 185,
        "name": "silent shroom",
        "description": "A strange mushroom that glows softly in the forest at night. Cooking it into a dish unlocks the nutrients in its cap, resulting in a meal that will allow you to move stealthily.",
        "common_locations": [
            "Lanayru Great Spring",
            "West Necluda"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "stealth up",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/silent_shroom/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 186,
        "name": "hyrule herb",
        "description": "This healthy herb grows abundantly in the plains of Hyrule. Cook it before eating to increase the number of hearts it restores.",
        "common_locations": [
            "Hyrule Field",
            "Akkala Highlands"
        ],
        "hearts_recovered": 1.0,
        "cooking_effect": "",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/hyrule_herb/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 187,
        "name": "hearty radish",
        "description": "A rare radish that grows best in sunny plains. Cook it before eating to temporarily increase your maximum hearts.",
        "common_locations": [
            "Hyrule Ridge",
            "East Necluda"
        ],
        "hearts_recovered": 2.5,
        "cooking_effect": "extra hearts",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/hearty_radish/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 188,
        "name": "big hearty radish",
        "description": "This hearty radish has grown much larger than the average radish. It_s rich in analeptic compounds that, when cooked into a dish, temporarily increase your maximum hearts.",
        "common_locations": [
            "Akkala Highlands",
            "Lanayru Great Spring"
        ],
        "hearts_recovered": 4.0,
        "cooking_effect": "extra hearts",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/big_hearty_radish/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 189,
        "name": "cool safflina",
        "description": "This medicinal plant grows in high elevations, such as mountains in the Hebra or Gerudo regions. When cooked into a dish, it will temporarily increase your heat resistance.",
        "common_locations": [
            "Hebra Mountains",
            "Gerudo Highlands"
        ],
        "hearts_recovered": 0.0,
        "cooking_effect": "heat resistance",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/cool_safflina/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 190,
        "name": "warm safflina",
        "description": "This medicinal plant grows in hot regions, such as the Gerudo Desert. It_s warm to the touch and increases your cold resistance when cooked into a dish.",
        "common_locations": [
            "Gerudo Desert",
            "Hyrule Ridge"
        ],
        "hearts_recovered": 0.0,
        "cooking_effect": "cold resistance",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/warm_safflina/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 191,
        "name": "electric safflina",
        "description": "This medicinal plant grows abundantly in the Gerudo Desert. Its peculiar fibers conduct electricity, which will increase your electricity resistance when cooked into a dish.",
        "common_locations": [
            "Gerudo Desert",
            "Hyrule Ridge"
        ],
        "hearts_recovered": 0.0,
        "cooking_effect": "shock resistance",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/electric_safflina/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 192,
        "name": "swift carrot",
        "description": "This carrot is cultivated extensively in Kakariko Village. It strengthens the legs and hips when cooked into a dish, which helps increase your movement speed.",
        "common_locations": [
            "Kakariko Village"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "speed up",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/swift_carrot/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 193,
        "name": "endura carrot",
        "description": "Highly valued as a medicinal plant, this carrot contains large amounts of nourishing energy. When cooked into a dish, it boosts your stamina beyond its maximum limit.",
        "common_locations": [
            "Hyrule Ridge",
            "Faron Grasslands"
        ],
        "hearts_recovered": 2.0,
        "cooking_effect": "extra stamina",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/endura_carrot/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 194,
        "name": "fortified pumpkin",
        "description": "An extremely tough pumpkin raised in village fields. When cooked, that toughness manifests itself by considerably upping defense.",
        "common_locations": [
            "Kakariko Village"
        ],
        "hearts_recovered": 0.5,
        "cooking_effect": "defense up",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/fortified_pumpkin/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 195,
        "name": "swift violet",
        "description": "This vitality-rich flower blooms mainly on cliffsides. When cooked into a dish, the nourishing compounds increase your movement speed.",
        "common_locations": [
            "Gerudo Highlands",
            "Hebra Mountains"
        ],
        "hearts_recovered": 0.0,
        "cooking_effect": "speed up",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/swift_violet/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 196,
        "name": "mighty thistle",
        "description": "This medicinal plant is known for its sharp thorns and for the fruit it bears. The fruit contains a compound that increases attack power when cooked into a dish.",
        "common_locations": [
            "West Necluda",
            "Faron Grasslands"
        ],
        "hearts_recovered": 0.0,
        "cooking_effect": "attack up",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/mighty_thistle/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 197,
        "name": "armoranth",
        "description": "This tough medicinal plant cannot be broken, but it can be cooked. Its durable yet flexible fibers raise your defense when cooked into a dish.",
        "common_locations": [
            "Akkala Highlands",
            "Hyrule Ridge"
        ],
        "hearts_recovered": 0.0,
        "cooking_effect": "defense up",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/armoranth/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 198,
        "name": "blue nightshade",
        "description": "A plant that grows in the quieter areas of Hyrule. At night, it gives off a soft glow. Cook with it to increase your stealth.",
        "common_locations": [
            "West Necluda",
            "Lanayru Great Spring"
        ],
        "hearts_recovered": 0.0,
        "cooking_effect": "stealth up",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/blue_nightshade/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 199,
        "name": "silent princess",
        "description": "This lovely flower was said to have been a favorite of the princess of Hyrule. Once feared to have gone extinct, it_s recently been spotted growing in the wild.",
        "common_locations": [
            "Hyrule Ridge",
            "West Necluda"
        ],
        "hearts_recovered": 0.0,
        "cooking_effect": "stealth up",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/silent_princess/image",
        "category": "materials",
        "dlc": "false"
    },
    {
        "id": 200,
        "name": "courser bee honey",
        "description": "Honey straight from the hive is chock-full of nutrients. Cooking this into a meal unlocks the potential of these nutrients and provides a stamina-recovery effect.",
        "common_locations": [
            "Hyrule Field",
            "Tabantha Frontier"
        ],
        "hearts_recovered": 2.0,
        "cooking_effect": "stamina recovery",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/courser_bee_honey/image",
        "category": "materials",
        "dlc": "false"
    }
]


, 'monsters' :

[
    {
        "id": 84,
        "name": "chuchu",
        "description": "This low-level, gel-based monster can be found all over Hyrule. It tends to spring its attacks on unsuspecting prey from the ground or from trees. Its strength varies by size, and the type of jelly it drops varies depending on whether the Chuchu was heated up, cooled down, or shocked.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "drops": [
            "chuchu jelly"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/chuchu/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 85,
        "name": "fire chuchu",
        "description": "This low-level gel monster is engulfed in flames. Its strength varies depending on its size. It tends to explode if attacked from close range, so the use of spears, arrows, and other ranged weapons is advised.",
        "common_locations": [
            "Eldin Canyon",
            "Eldin Mountains"
        ],
        "drops": [
            "red chuchu jelly"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/fire_chuchu/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 86,
        "name": "ice chuchu",
        "description": "This low-level gel monster is engulfed in freezing-cold air. Its strength varies depending on its size. It tends to explode if attacked from close range, so the use of spears, arrows, and other ranged weapons is advised.",
        "common_locations": [
            "Gerudo Highlands",
            "Hebra Mountains"
        ],
        "drops": [
            "white chuchu jelly"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ice_chuchu/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 87,
        "name": "electric chuchu",
        "description": "This low-level gel monster is engulfed in electricity. Its strength varies depending on its size. It tends to explode if attacked from close range, so the use of spears, arrows, and other ranged weapons is advised.",
        "common_locations": [
            "Gerudo Highlands",
            "East Necluda"
        ],
        "drops": [
            "yellow chuchu jelly"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/electric_chuchu/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 88,
        "name": "keese",
        "description": "The unpredictable flight pattern of this noctoural bat-like species can make fighting them a nuisance, but they_re weak enough to fell with a single strike. Sometimes they_ll attack in packs, but even then, a pack can be sent packing with a single attack.",
        "common_locations": [
            "Hyrule Field",
            "East Necluda"
        ],
        "drops": [
            "keese wing",
            "keese eyeball"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/keese/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 89,
        "name": "fire keese",
        "description": "The fire that engulfs the bodies of these bat-like Keese makes them more dangerous than the standard type. They_re capable of setting fire to anything they touch.",
        "common_locations": [
            "Eldin Canyon",
            "Eldin Mountains"
        ],
        "drops": [
            "fire keese wing",
            "keese eyeball"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/fire_keese/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 90,
        "name": "ice keese",
        "description": "The intense frost that engulfs the bodies of these bat-like Keese makes them more dangerous than the standard type. They_re capable of freezing anything they touch.",
        "common_locations": [
            "Hebra Mountains",
            "Gerudo Highlands"
        ],
        "drops": [
            "ice keese wing",
            "keese eyeball"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ice_keese/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 91,
        "name": "electric keese",
        "description": "The electricity that engulfs the bodies of these bat-like Keese makes them more dangerous than the standard type. They_re capable of shocking anything they touch.",
        "common_locations": [
            "Lanayru Great Spring",
            "East Necluda"
        ],
        "drops": [
            "electric keese wing",
            "keese eyeball"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/electric_keese/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 92,
        "name": "water octorok",
        "description": "Although they spend most of their time in water, the drop in barometric pressure that occurs when it rains causes an air sac within these octopus-like monsters to inflate and lift them into the air. The rocks they spit out can be bounced back with a shield.",
        "common_locations": [
            "West Necluda",
            "Hyrule Field"
        ],
        "drops": [
            "octorok tentacle",
            "octo balloon",
            "octorok eyeball"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/water_octorok/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 93,
        "name": "forest octorok",
        "description": "Although originally an aquatic species, this type has adapted to life in the forest. They hide among the trees, disguising themselves as grass or unassuming shrubbery, and then attack when someone wanders by.",
        "common_locations": [
            "Hyrule Ridge",
            "Deep Akkala"
        ],
        "drops": [
            "octorok tentacle",
            "octo balloon",
            "octorok eyeball"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/forest_octorok/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 94,
        "name": "rock octorok",
        "description": "This octopus-like species of monster lives in volcanic regions. When they inhale, they_re preparing to spit out flaming rocks but have been known to suck up weapons or bombs in the same breath.",
        "common_locations": [
            "Eldin Canyon",
            "Gerudo Highlands"
        ],
        "drops": [
            "octorok tentacle",
            "octo balloon",
            "octorok eyeball"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/rock_octorok/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 95,
        "name": "snow octorok",
        "description": "These octopus-like monsters live in snowy fields and disguise themselves as grass. When someone wanders by, they spring into action and attack by spitting snowballs.",
        "common_locations": [
            "Gerudo Highlands",
            "Tabantha Frontier"
        ],
        "drops": [
            "octorok tentacle",
            "octo balloon",
            "octorok eyeball"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/snow_octorok/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 96,
        "name": "treasure octorok",
        "description": "These particularly clever monsters bury themselves in deep sand or snow and disguise themselves as treasure chests. Anyone who approaches the chests is attacked. The treasures chests are not magnetic, which proves that they are actually a part of these monsters_ bodies.",
        "common_locations": [
            "Gerudo Highlands",
            "Gerudo Desert"
        ],
        "drops": [
            "octorok tentacle",
            "octo balloon",
            "octorok eyeball",
            "green rupee",
            "blue rupee",
            "red rupee",
            "purple rupee",
            "silver rupee"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/treasure_octorok/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 97,
        "name": "fire wizzrobe",
        "description": "These spell-casting monsters can be found all over Hyrule. They use their fire rods to hurl fireballs or to summon flaming monsters and have been known to severely raise the temperature around them. The weather will normalize once the Wizzrobe is defeated.",
        "common_locations": [
            "Hyrule Field",
            "Great Hyrule Forest"
        ],
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/fire_wizzrobe/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 98,
        "name": "ice wizzrobe",
        "description": "These spell-casting monsters can be found all over Hyrule. They use their ice rods to create freezing blasts of air or to summon frozen monsters and have been known to cause blizzards to severely decrease the temperatures around them. The weather will normalize once the Wizzrobe is defeated.",
        "common_locations": [
            "Gerudo Highlands",
            "Hyrule Field"
        ],
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ice_wizzrobe/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 99,
        "name": "electric wizzrobe",
        "description": "These spell-casting monsters can be found all over Hyrule. They use their lightning rods to hurl balls of electricity or to summon monsters surging with electricity and have been known to cause thunderstorms in the area. The weather will normalize once the Wizzrobe has been defeated.",
        "common_locations": [
            "Hyrule Ridge",
            "West Necluda"
        ],
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/electric_wizzrobe/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 100,
        "name": "meteo wizzrobe",
        "description": "These spell-casting monsters can be found all over Hyrule. They use their meteor rods to hurl fireballs or to summon flaming monsters and have been known to severely raise the temperature around them. The weather will normalize once the Wizzrobe is defeated.",
        "common_locations": [
            "Hyrule Field",
            "Eldin Canyon"
        ],
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/meteo_wizzrobe/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 101,
        "name": "blizzrobe",
        "description": "These spell-casting monsters can be found all over Hyrule. They use their blizzard rods to create freezing blasts of air or to summon frozen monsters and have been known to cause blizzards to severely decrease the temperature around them. The weather will normalize once the Blizzrobe is defeated.",
        "common_locations": [
            "Hyrule Field",
            "Hebra Mountains"
        ],
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/blizzrobe/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 102,
        "name": "thunder wizzrobe",
        "description": "These spell-casting monsters can be found all over Hyrule. They use their thunderstorm rods to hurl balls of electricity or to summon monsters surging with electricity and have been known to cause thunderstorms in the area. The weather will normalize once the Wizzrobe is defeated.",
        "common_locations": [
            "Hyrule Field",
            "Tabantha Frontier"
        ],
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/thunder_wizzrobe/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 103,
        "name": "bokoblin",
        "description": "This common species is a nuisance all over Hyrule. Some have unified in the time following the Great Calamity and have formed factions of bandits. While not very clever, they are at least intelligent enough to hunt beasts and grill their meat for food. Though they_re typically ferocious carnivores, they actually enjoy fruit as well.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "drops": [
            "bokoblin horn",
            "bokoblin fang"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/bokoblin/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 104,
        "name": "blue bokoblin",
        "description": "This common species is a nuisance all over Hyrule. They_re tougher and have stronger weapons than the red Bokoblins - and are a little more clever, as well. At the very least, they have figured out that they can simply kick a Remote Bomb out of the way to avoid its blast.",
        "common_locations": [
            "Gerudo Desert",
            "Gerudo Highlands"
        ],
        "drops": [
            "bokoblin horn",
            "bokoblin fang",
            "bokoblin guts"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/blue_bokoblin/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 105,
        "name": "black bokoblin",
        "description": "Although Bokoblins are generally a nuisance, the Black Bokoblins are among the most dangerous type. They_re extremely resilient, and many are armed with more advanced weapons.",
        "common_locations": [
            "Hyrule Field",
            "Gerudo Highlands"
        ],
        "drops": [
            "bokoblin horn",
            "bokoblin fang",
            "bokoblin guts"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/black_bokoblin/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 106,
        "name": "stalkoblin",
        "description": "The remains of Bokoblins appear in the dark of the night. While they_re fragile enough to crumble from a single blow, as long as a skull remains intact, they_ll continue to pull themselves back together and go on fighting. Sometimes the body will pick up the wrong skull, but this doesn_t seem to be a problem...",
        "common_locations": [
            "Hyrule Field",
            "Great Hyrule Forest"
        ],
        "drops": [
            "bokoblin horn",
            "bokoblin fang"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/stalkoblin/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 107,
        "name": "silver bokoblin",
        "description": "You would be foolish to call these Silver Bokoblins a mere nuisance. They have been influenced by Ganon_s fiendish magic, so they are stronger than even the Black Bokoblins. They_re called \"silver\" not only because of their coloring but also to denote their rarity. The purple markings help them to stand out even more.",
        "common_locations": "null",
        "drops": [
            "bokoblin horn",
            "bokoblin fang",
            "bokoblin guts",
            "amber",
            "opal",
            "topaz",
            "ruby",
            "sapphire",
            "diamond"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/silver_bokoblin/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 108,
        "name": "moblin",
        "description": "This heavyweight species of monster can be found all over Hyrule. They_re physically very strong, their legs along strong enough to resist the force of a bomb blast. They_re much more dangerous than the Bokoblins. In fact, Moblins have been known to pick up Bokoblins and throw them as makeshift projectile weapons.",
        "common_locations": [
            "Hyrule Field",
            "East Necluda"
        ],
        "drops": [
            "moblin horn",
            "moblin fang"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/moblin/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 109,
        "name": "blue moblin",
        "description": "These heavyweight monsters can be found all over Hyrule. They_re much tougher than their standard counterparts and often have much stronger weapons equipped.",
        "common_locations": [
            "Hyrule Field",
            "Deep Akkala"
        ],
        "drops": [
            "moblin horn",
            "moblin fang",
            "moblin guts"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/blue_moblin/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 110,
        "name": "black moblin",
        "description": "These heavyweight monsters can be found all over Hyrule and are among the most dangerous types of Moblin. They_re extremely resilient and are often armed with some of the strongest weapons Moblins can carry.",
        "common_locations": [
            "Hyrule Field",
            "Eldin Canyon"
        ],
        "drops": [
            "moblin horn",
            "moblin fang",
            "moblin guts"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/black_moblin/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 111,
        "name": "stalmoblin",
        "description": "The remains of Moblins appear in the dark of the night. Even the toughest Moblins become fragile when they_re little more than a pile of bones, so they_ll crumble after just a few attacks. However, as long as a skull remains intact, they_ll continue to pull themselves back together and go on fighting.",
        "common_locations": [
            "Great Hyrule Forest",
            "Gerudo Highlands"
        ],
        "drops": [
            "moblin horn",
            "moblin fang"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/stalmoblin/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 112,
        "name": "silver moblin",
        "description": "The strongest of all Moblins, Ganon_s fiendish magic has allowed them to surpass even the Black Moblins in strength and resilience. They_re called \"silver\" for both their body color as well as their rarity. The purple patterns on their bodies also help them to stand out.",
        "common_locations": "null",
        "drops": [
            "moblin horn",
            "moblin fang",
            "moblin guts",
            "amber",
            "opal",
            "topaz",
            "ruby",
            "sapphire",
            "diamond"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/silver_moblin/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 113,
        "name": "lizalfos",
        "description": "These quick-witted, lizard-like monsters can be found all over Hyrule. They_re a sly species that lurks underwater or uses camouflage to blend in with the environment to launch ambushes. Moreover, they never sleep. They_re meat eaters by nature but will enjoy the occasional insect or two.",
        "common_locations": [
            "Lanayru Great Spring",
            "Gerudo Desert"
        ],
        "drops": [
            "lizalfos horn",
            "lizalfos talon"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lizalfos/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 114,
        "name": "blue lizalfos",
        "description": "These quick-witted, lizard-like monsters can be found all over Hyrule. Compared to the green Lizalfos, many of these carry much stronger weapons and are generally much tougher.",
        "common_locations": [
            "Tabantha Frontier",
            "Gerudo Desert"
        ],
        "drops": [
            "lizalfos horn",
            "lizalfos talon",
            "lizalfos tail"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/blue_lizalfos/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 115,
        "name": "black lizalfos",
        "description": "These quick-witted, lizard-like monsters can be found all over Hyrule. This particular type tends to carry some pretty strong weapons, so they are among the most dangerous Lizalfos.",
        "common_locations": [
            "Hyrule Field",
            "Hebra Mountains"
        ],
        "drops": [
            "lizalfos horn",
            "lizalfos talon",
            "lizalfos tail"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/black_lizalfos/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 116,
        "name": "stalizalfos",
        "description": "The remains of Lizalfos appear in the dark of night. They_re as sly as ever, even now that they_re just some bones stacked atop each other. However, their bodies are much more fragile, and a single solid hit can reduce them to pieces. If a skull remains intact, they will pull themselves back up and continue to fight. They_ve been known to grab the wrong skull at times, but they never seem to mind...",
        "common_locations": [
            "Gerudo Desert",
            "Hyrule Ridge"
        ],
        "drops": [
            "lizalfos horn",
            "lizalfos talon"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/stalizalfos/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 117,
        "name": "fire-breath lizalfos",
        "description": "These quick-witted, lizard-like monsters can be found all over Hyrule. Their fiery breath makes them pretty dangerous, but exposure to cold will kill them instantly. They mainly make their homes in volcanic areas but have also been sighted in the Akkala region.",
        "common_locations": [
            "Eldin Canyon",
            "Gerudo Desert"
        ],
        "drops": [
            "lizalfos horn",
            "lizalfos talon",
            "red lizalfos tail"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/fire-breath_lizalfos/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 118,
        "name": "ice-breath lizalfos",
        "description": "These quick-witted, lizard-like monsters can be found all over Hyrule. The balls of ice they spit make them particularly troublesome, but exposure to fire will kill them instantly. Their homes are mainly on snowy mountains.",
        "common_locations": [
            "Gerudo Highlands",
            "Hebra Mountains"
        ],
        "drops": [
            "lizalfos horn",
            "lizalfos talon",
            "icy lizalfos tail"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ice-breath_lizalfos/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 119,
        "name": "electric lizalfos",
        "description": "These quick-witted, lizard-like monsters can be found all over Hyrule. The can emit strong electrical currents from their bodies, so don_t get too close. Their horns are brimming with electricity, which will discharge and arc to nearby areas if struck by an arrow. They tend to live in desert climates.",
        "common_locations": [
            "Gerudo Desert",
            "Hyrule Ridge"
        ],
        "drops": [
            "lizalfos horn",
            "lizalfos tail",
            "yellow lizalfos tail"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/electric_lizalfos/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 120,
        "name": "silver lizalfos",
        "description": "These Lizalfos have been influenced by Ganon_s fiendish magic to become the strongest Lizalfos of all. They_re called \"silver\" for their unique coloring and also to denote their rarity. Their purple pattern makes them even more distinct.",
        "common_locations": "null",
        "drops": [
            "lizalfos horn",
            "lizalfos talon",
            "lizalfos tail",
            "amber",
            "opal",
            "topaz",
            "ruby",
            "sapphire",
            "diamond"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/silver_lizalfos/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 121,
        "name": "lynel",
        "description": "These fearsome monsters have lived in Hyrule since ancient times. They possess intense intelligence, resilience, and strength, making them among the most dangerous monsters in all the land. This is compounded by the fact that they have a natural resistance to all elements. You would be wise to challenge a Lynel only if you_re very well prepared.",
        "common_locations": [
            "Lanayru Great Spring",
            "Hyrule Field"
        ],
        "drops": [
            "lynel horn",
            "lynel hoof",
            "lynel guts"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lynel/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 122,
        "name": "blue-maned lynel",
        "description": "These fearsome monsters have lived in Hyrule since ancient times. Compared to the standard Lynel, those with blue manes much tougher and equipped with much stronger weapons. Facing off against a Lynel is ill-advised, but if you must, be sure you_re well prepared.",
        "common_locations": [
            "Hyrule Field",
            "Deep Akkala"
        ],
        "drops": [
            "lynel horn",
            "lynel hoof",
            "lynel guts"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/blue-maned_lynel/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 123,
        "name": "white-maned lynel",
        "description": "These fearsome monsters have lived in Hyrule since  times. Their ability to breathe fire makes White-Maned Lynels among the toughest of the species; each one of their attacks is an invitation to the grave. There are so few eyewitness accounts of this breed because a White-Maned Lynel is not one to let even simple passersby escape with their lives.",
        "common_locations": [
            "Hyrule Field",
            "Hebra Mountains"
        ],
        "drops": [
            "lynel horn",
            "lynel hoof",
            "lynel guts"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/white-maned_lynel/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 124,
        "name": "silver lynel",
        "description": "Silver Lynels are not to be trifled with. They have been influenced by Ganon_s fiendish magic, so they are the strongest among the Lynel species, surpassing even the strength of those with white manes. The term \"silver\" denotes not only their color but also their rarity. The purple stripes help them to stand out even more.",
        "common_locations": "null",
        "drops": [
            "lynel horn",
            "lynel hoof",
            "lynel guts",
            "topaz",
            "ruby",
            "sapphire",
            "diamond",
            "star fragment"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/silver_lynel/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 125,
        "name": "guardian stalker",
        "description": "The Sheikah of ancient Hyrule developed this as a weapon to combat Ganon. Its six legs give it extraordinary mobility compared to most current vehicles, and its powerful laser provides far greater offensive capability than conventional weaponry. Destroying the legs severely reduces its mobility.",
        "common_locations": [
            "Hyrule Field"
        ],
        "drops": [
            "ancient screw",
            "ancient spring",
            "ancient gear",
            "ancient shaft",
            "ancient core",
            "giant ancient core"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_stalker/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 126,
        "name": "guardian skywatcher",
        "description": "The Sheikah of ancient Hyrule developed this as a weapon to combat Ganon. This flying model is an improvement over the walking type, capable of either attacking or surveying from the air. Destroying the propeller will ground it.",
        "common_locations": [
            "Hyrule Field",
            "Akkala Highlands"
        ],
        "drops": [
            "ancient screw",
            "ancient spring",
            "ancient gear",
            "ancient shaft",
            "ancient core",
            "giant ancient core"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_skywatcher/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 127,
        "name": "guardian turret",
        "description": "The Sheikah of ancient Hyrule developed this as a weapon to combat Ganon. This stationary model was used for defending important structures. Its offensive power is on par with other Guardians, and omitting the legs kept the manufacturing costs low.",
        "common_locations": [
            "Hyrule Castle"
        ],
        "drops": [
            "ancient screw",
            "ancient spring",
            "ancient gear",
            "ancient shaft",
            "ancient core",
            "giant ancient core"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_turret/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 128,
        "name": "sentry",
        "description": "These sentries dispatched from Divine Beast Vah Rudania are equipped with searchlights that can spot intruders.",
        "common_locations": [
            "Death Mountain"
        ],
        "drops": [
            "ancient screw",
            "ancient spring",
            "ancient gear",
            "ancient shaft",
            "ancient core"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/sentry/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 129,
        "name": "decayed guardian",
        "description": "The Sheikah of ancient Hyrule developed this as a weapon to combat Ganon, but it was destroyed during the Great Calamity. Ages of weather and neglect have left it in a state of disrepair. Approach with caution; some of the derelict models have been known to awaken from stasis and attack when approached.",
        "common_locations": [
            "Hyrule Field",
            "Hyrule Castle"
        ],
        "drops": [
            "ancient screw",
            "ancient spring",
            "ancient gear",
            "ancient shaft"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/decayed_guardian/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 130,
        "name": "guardian scout i",
        "description": "Guardians were originally designed by an ancient civilization to combat Ganon, but these smaller models were placed inside shrines as part of the trials found within. The multiple legs and beam functionality were scaled down but kept mostly intact.",
        "common_locations": "null",
        "drops": [
            "ancient screw",
            "ancient spring"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_scout_i/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 131,
        "name": "guardian scout ii",
        "description": "Although originally designed by an ancient civilization to combat Ganon, these scaled-down Guardians were placed inside shrines as part of the trials. In additional to the beam functionality, this particular model was designed to handle weaponry as a means of further testing the combat prowess of one undertaking the trials. It takes some serious skill to go toe-to-toe with one of these.",
        "common_locations": "null",
        "drops": [
            "ancient screw",
            "ancient spring",
            "ancient gear",
            "ancient shaft"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_scout_ii/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 132,
        "name": "guardian scout iii",
        "description": "Although originally designed by an ancient civilisation to combat Ganon, these scaled-down Guardians were placed inside shrines as part or the trials. This model is equipped with twin-blade functionality to further test the combat prowess of one undertaking the trials. It takes a nimble fighter to overcome this one.",
        "common_locations": "null",
        "drops": [
            "ancient screw",
            "ancient spring",
            "ancient gear",
            "ancient shaft",
            "ancient core"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_scout_iii/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 133,
        "name": "guardian scout iv",
        "description": "An ancient civilization originally designed Guardians to combat Ganon but then scaled them down to place in shrines as part of the trials. This model is very resilient and has been outfitted with triple-blade functionality, allowing it to wield three weapons. This will put any would-be hero to the test for sure. A great deal of strength and confidence alike are required to contend with one of these.",
        "common_locations": "null",
        "drops": [
            "ancient screw",
            "ancient spring",
            "ancient gear",
            "ancient shaft",
            "ancient core"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/guardian_scout_iv/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 134,
        "name": "yiga footsoldier",
        "description": "The lowest-ranked members of the Yiga Clan. They_ve been dispatched all across Hyrule with a single task: seek out Link and end his life. They_re a crafty bunch, sometimes disguising themselves as simple travelers or villagers to get the jump on you. Be wary of suspicious people you encounter. They_re very agile and carry a bow and one-handed sword.",
        "common_locations": "null",
        "drops": [
            "green rupee",
            "blue rupee",
            "red rupee",
            "purple rupee",
            "mighty bananas"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/yiga_footsoldier/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 135,
        "name": "yiga blademaster",
        "description": "These are the elite soldiers of the Yiga Clan. They favor the windcleaver blade and are extremely agile despite their bulky build. At this Yiga Clan rank, they have mastered a technique that allows them to manipulate the very earth. By striking the ground, they can create stone pillars and blasts of air.",
        "common_locations": "null",
        "drops": [
            "amber",
            "opal",
            "topaz",
            "ruby",
            "sapphire",
            "mighty bananas"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/yiga_blademaster/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 136,
        "name": "master kohga",
        "description": "The leader of the Yiga Clan, a group formed with just a single objective: eliminate Link. He sends his minions all over Hyrule in search of you but tends to spend most of his time napping and generally loafing about. Despite this, his mastery of the esoteric arts has earned him a deep respect. Even if he were to die, his followers would never give up on their one and only task.",
        "common_locations": [
            "Yiga Clan Hideout"
        ],
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/master_kohga/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 137,
        "name": "monk maz koshia",
        "description": "The arbiter of worthiness for the hero who wishes to control a Divine Beast, following a revelation from the Goddess Hylia. As the last part of the final trial, the monk offers a challenge of ancient techniques.",
        "common_locations": "null",
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/monk_maz_koshia/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 138,
        "name": "stone talus",
        "description": "This enormous monster is naturally camouflaged as a rock formation. Neither sword nor arrow can pierce its stony form, but a cunning adventurer knows to scale its body and attack the ore sprouting from its peak.",
        "common_locations": [
            "West Necluda",
            "East Necluda"
        ],
        "drops": [
            "flint",
            "amber",
            "opal",
            "ruby"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/stone_talus/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 139,
        "name": "stone talus (luminous)",
        "description": "This enormous monster is naturally camouflaged as a rock formation. Neither sword nor arrow can pierce its stony form, but a cunning adventurer knows to scale its body and attack the ore sprouting from its peak. Unlike your average Stone Talus, this type_s ore deposit consists mostly of luminous stone.",
        "common_locations": [
            "Gerudo Highlands",
            "Hyrule Field"
        ],
        "drops": [
            "flint",
            "amber",
            "opal",
            "luminous stone",
            "topaz",
            "diamond"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/stone_talus_luminous/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 140,
        "name": "stone talus (rare)",
        "description": "This enormous monster is naturally camouflaged as a rock formation. Neither stone nor arrow can pierce its stony form, but a cunning adventurer knows to scale its body and attack the ore sprouting from its peak. Unlike your average Stone Talus, this type_s ore deposit contains a large amount of precious ore.",
        "common_locations": [
            "Hyrule Field",
            "Tabantha Frontier"
        ],
        "drops": [
            "flint",
            "amber",
            "opal",
            "topaz",
            "ruby",
            "sapphire",
            "diamond"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/stone_talus_rare/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 141,
        "name": "igneo talus",
        "description": "This enormous monster is naturally camouflaged as molten rock. Neither sword nor arrow can pierce its fiery form. Merely touching its magma-hot body can burn you pretty badly, but you may be able to scale it if you can use something to chill its flames.",
        "common_locations": [
            "Eldin Canyon"
        ],
        "drops": [
            "flint",
            "opal",
            "ruby",
            "diamond"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/igneo_talus/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 142,
        "name": "frost talus",
        "description": "This enormous monster is naturally camouflaged as a frozen rock formation. Neither sword nor arrow can pierce its frigid form. Merely touching its frosty body can leave you with severe frostbite, but you may be able to scale it if you use something to thaw its icy exterior.",
        "common_locations": [
            "Hebra Mountains",
            "Gerudo Highlands"
        ],
        "drops": [
            "flint",
            "opal",
            "sapphire",
            "diamond"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/frost_talus/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 143,
        "name": "stone pebblit",
        "description": "A very young Stone Talus. Their bodies toughen as they mature, becoming as tough as boulders by adulthood. As a child, however, their bodies are light enough to be lifted and fragile enough to break when thrown.",
        "common_locations": [
            "Greater Hyrule"
        ],
        "drops": [
            "flint",
            "amber",
            "opal"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/stone_pebblit/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 144,
        "name": "igneo pebblit",
        "description": "A very young Igneo Talus. Their bodies toughen as they mature and convert fully into lava by adulthood. As a child, however, while still covered in fire, their bodies are fragile and light enough to be blown away by a bomb_s blast.",
        "common_locations": [
            "Eldin Canyon",
            "Eldin Mountains"
        ],
        "drops": [
            "flint",
            "amber",
            "ruby"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/igneo_pebblit/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 145,
        "name": "frost pebblit",
        "description": "A very young Frost Talus. Their bodies toughen and frost over as they mature, becoming entirely made of ice by adulthood. As a child, however, their bodies are awfully fragile and are light enough to be blown away by a bomb_s blast.",
        "common_locations": [
            "Hebra Mountains",
            "Gerudo Highlands"
        ],
        "drops": [
            "flint",
            "amber",
            "sapphire"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/frost_pebblit/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 146,
        "name": "igneo talus titan",
        "description": "This monster is an Igneo Talus subspecies that is camouflaged as molten rock. It lives in lava for many years before emerging at an enormous size. It is wildly powerful and emits a tremendous amount of heat, causing a constant updraft in its vicinity. This monster is so fearsome it has earned the title of Titan.",
        "common_locations": "null",
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/igneo_talus_titan/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 147,
        "name": "hinox",
        "description": "The largest monster to make its home in Hyrule, the Hinox lives primarily in forested areas. A keen awareness of your surroundings is paramount when facing one, as Hinox are known for tearing entire trees from the ground and using them as weapons. A deft hand can steal weapons off the necklaces they wear.",
        "common_locations": [
            "East Necluda",
            "West Necluda"
        ],
        "drops": [
            "hinox toenail",
            "hinox tooth",
            "hinox guts",
            "apple",
            "wildberry",
            "palm fruit",
            "voltfruit",
            "mighty bananas",
            "fortified pumpkin",
            "hearty durian"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/hinox/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 148,
        "name": "blue hinox",
        "description": "The largest monster to make its home in Hyrule, the Hinox lives primarily in forested areas. A keen awareness of your surroundings is paramount when facing one, as Hinox are known for tearing entire trees from the ground and using them as weapons. Blue Hinox wear greaves that can be burnt away to expose their feet. A deft hand can steal weapons off the necklaces they wear.",
        "common_locations": [
            "Hyrule Field",
            "Lanayru Great Spring"
        ],
        "drops": [
            "hinox toenail",
            "hinox tooth",
            "hinox guts",
            "roasted bass",
            "roasted hearty bass",
            "roasted hearty salmon",
            "roasted trout",
            "roasted carp",
            "roasted porgy",
            "sneaky river escargot",
            "blueshell escargot",
            "blackened crab"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/blue_hinox/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 149,
        "name": "black hinox",
        "description": "The largest monster to make its home in Hyrule, the Hinox lives primarily in forested areas. A keen awareness of your surroundings is paramount when facing one, as Hinox are known for tearing entire trees from the ground and using them as weapons. Black Hinox wear metal greaves that conduct electricity rather well. A deft hand can steal weapons off the necklaces they wear.",
        "common_locations": [
            "East Necluda",
            "Hyrule Field"
        ],
        "drops": [
            "hinox toenail",
            "hinox tooth",
            "hinox guts",
            "seared steak",
            "seared prime steak",
            "seared gourmet steak",
            "roasted bird drumstick",
            "roasted bird thigh",
            "roasted whole bird"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/black_hinox/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 150,
        "name": "stalnox",
        "description": "The mere remains of what was once a giant monster known as a Hinox. These skeletal beasts appear at nighttime. Much like their living counterparts, the Stalnox will tear entire trees from the ground to use as weapons. Furthermore, even if it appears defeated at first, it will keep coming back for more as long as its eye is left intact.",
        "common_locations": [
            "Hyrule Field",
            "West Necluda"
        ],
        "drops": [
            "hinox tooth"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/stalnox/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 151,
        "name": "molduga",
        "description": "This massive monster swims beneath the desert_s sand. It spends most of its time submerged, but if it senses sound, it will breach the surface to feast on whatever it can grab. Running around carelessly can be dangerous if you suspect there may be one in the area.",
        "common_locations": [
            "Gerudo Desert"
        ],
        "drops": [
            "molduga fin",
            "molduga guts"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/molduga/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 152,
        "name": "molduking",
        "description": "This massive monster swims beneath the desert_s sand. It is a subspecies of Molduga that stored up a great deal of energy by sleeping underground for hundreds of years. Its power is superior to Molduga, as its skin is rich with iron and acts as a protective shield.",
        "common_locations": "null",
        "drops": [
            "treasures"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/molduking/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 153,
        "name": "dinraal",
        "description": "A spirit of fire has taken the form of this giant dragon. Making its home in the Eldin region, it_s said to have served the Spring of Power since ancient times. An old saying goes, \"The dragon ascends to the heavens as the sun begins to set,\" but nobody has witnessed this in the current age. The flames that coat its body make it dangerous to get near, but Dinraal bears no ill will toward people.",
        "common_locations": [
            "Eldin Mountains",
            "Tabantha Frontier"
        ],
        "drops": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/dinraal/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 154,
        "name": "naydra",
        "description": "A spirit of ice has taken the form of this giant dragon. Making its home in the Lanayru region, it_s said to have served the Spring of Wisdom since ancient times. An old saying goes, \"The dragon ascends to the heavens as the sun begins to set,\" but nobody has seen this in the current age. The ice that coats its body makes it dangerous to get near, but Naydra bears no ill will toward people.",
        "common_locations": [
            "Mount Lanayru"
        ],
        "drops": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/naydra/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 155,
        "name": "farosh",
        "description": "A spirit of lightning has taken the form of this giant dragon. Making its home in the Faron region, it_s said to have served the Spring of Courage since ancient times. An old saying goes, \"The dragon ascends to the heavens as the sun begins to set,\" but nobody has seen this in the current age. The electricity that coats its body makes it dangerous to get near, but Farosh bears no ill will toward people.",
        "common_locations": [
            "Lake Hylia",
            "Lake Floria"
        ],
        "drops": "null",
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/farosh/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 156,
        "name": "cursed bokoblin",
        "description": "The Malice has given these Bokoblin skulls a sort of life. Devoid of any intelligence the Bokoblin it once belonged to may have had, these pitiful things now exist only to attack anything that gets too close.",
        "common_locations": "null",
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/cursed_bokoblin/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 157,
        "name": "cursed moblin",
        "description": "The Malice has given these Moblin skulls a pitiful life after death. The only fragment of their former selves they_ve held on to is the ferocity innate to all Moblins, so they will attack anyone that approaches.",
        "common_locations": "null",
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/cursed_moblin/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 158,
        "name": "cursed lizalfos",
        "description": "The Malice has given these Lizalfos skulls a sorry form of life after death. Only the slyness of their former selves remains, making them faster than Bokoblin skulls. They thoughtlessly attack anyone who approaches.",
        "common_locations": "null",
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/cursed_lizalfos/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 159,
        "name": "thunderblight ganon",
        "description": "This phantom of Ganon attacked the Divine Beast Vah Naboris and was responsible for the demise of the Champion Urbosa. It specializes in quick, lightning-based attacks.",
        "common_locations": [
            "Divine Beast Vah Naboris"
        ],
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/thunderblight_ganon/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 160,
        "name": "fireblight ganon",
        "description": "This phantom of Ganon attacked the Divine Beast Vah Rudania and was responsible for the demise of the Champion Daruk. It attacks with a greatsword and fire magic.",
        "common_locations": [
            "Divine Beast Vah Rudania"
        ],
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/fireblight_ganon/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 161,
        "name": "waterblight ganon",
        "description": "This phantom of Ganon attacked the Divine Beast Vah Ruta and was responsible for the demise of the Champion Mipha. It attacks with a spear and ice magic.",
        "common_locations": [
            "Divine Beast Vah Ruta"
        ],
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/waterblight_ganon/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 162,
        "name": "windblight ganon",
        "description": "This phantom of Ganon attacked the Divine Beast Vah Medoh and was responsible for the demise of the Champion Revali. It specializes in long-ranged wind attacks.",
        "common_locations": [
            "Divine Beast Vah Medoh"
        ],
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/windblight_ganon/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 163,
        "name": "calamity ganon",
        "description": "The source of the darkness that has appeared time and again throughout Hyrule_s history. It_s been called many names, from \"Great King of Evil\" to \"Calamity.\" Hibernating within a cocoon, it attempted to regenerate a physical form after Link awoke but was forced to confront him in an incomplete state.",
        "common_locations": [
            "Hyrule Castle"
        ],
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/calamity_ganon/image",
        "category": "monsters",
        "dlc": "false"
    },
    {
        "id": 164,
        "name": "dark beast ganon",
        "description": "After Ganon was defeated by Link, the remaining Malice pulled itself together to form this bestial creature. Its appearance and fiendish magic eared it the name of Dark Beast. This form is considered to be Ganon_s original, although in this state, his awareness has been consumed entirely by Malice, and all he knows is a desire to rampage and destroy.",
        "common_locations": [
            "Hyrule Field"
        ],
        "drops": [""],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/dark_beast_ganon/image",
        "category": "monsters",
        "dlc": "false"
    }
]

, 'treasure' :

[
    {
        "id": 386,
        "name": "treasure chest",
        "description": "Fortunes untold (potentially) await the lucky adventurer who finds one of these. Chests can often be found within shrines or at enemy camps, but there may be some crafty folks who think they_re safer underground.",
        "common_locations": [
            "Greater Hyrule"
        ],
        "drops": [
            "treasures"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/treasure_chest/image",
        "category": "treasure",
        "dlc": "false"
    },
    {
        "id": 387,
        "name": "ore deposit",
        "description": "This deposit contains a good deal of ore. Breaking the rock will yield rock salt, flint, and other minerals of varying value.",
        "common_locations": [
            "Greater Hyrule"
        ],
        "drops": [
            "ruby",
            "diamond",
            "amber",
            "sapphire",
            "topaz",
            "opal",
            "rock salt",
            "flint"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/ore_deposit/image",
        "category": "treasure",
        "dlc": "false"
    },
    {
        "id": 388,
        "name": "rare ore deposit",
        "description": "This deposit contains a good deal of precious ore and the occasional rare mineral, like ruby and sapphire. Break it open to see what it has to offer!",
        "common_locations": [
            "Greater Hyrule"
        ],
        "drops": [
            "ruby",
            "sapphire",
            "diamond",
            "amber",
            "topaz",
            "flint"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/rare_ore_deposit/image",
        "category": "treasure",
        "dlc": "false"
    },
    {
        "id": 389,
        "name": "luminous ore deposit",
        "description": "This deposit contains quite a bit of luminous stone. Crack it open to get at the easily process rocks within.",
        "common_locations": [
            "Greater Hyrule"
        ],
        "drops": [
            "luminous",
            "flint"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/luminous_ore_deposit/image",
        "category": "treasure",
        "dlc": "false"
    }
]

}


def liste_loc(d) :
    list_common_locations = []
    for m in range(len(d['monsters'])) :
        for i in range(len(d['monsters'][m]["common_locations"])) :
            if d['monsters'][m]["common_locations"][i] not in list_common_locations or d['monsters'][m]["common_locations"][i] == "null" :
                list_common_locations.append(d['monsters'][m]["common_locations"][i])
                if list_common_locations[-1] == 'n' or list_common_locations[-1] == 'u' or list_common_locations[-1] == 'l' :
                    del list_common_locations[-1]
    return list_common_locations

print(liste_loc(d))
len(d)

connexion = sqlite3.connect('basededonneesapi.db')
curseur = connexion.cursor()

#TableauRegion
curseur.execute("DROP TABLE Region ;")
curseur.execute("CREATE TABLE IF NOT EXISTS Region(id INTEGER PRIMARY KEY, name TEXT) ;")
def region_info(d) :
    """id et nom des regions"""
    for r in range(len(d['region'])) :
        curseur.execute("INSERT INTO Region VALUES (" + str(r+1) + ", '" + str(d['region'][r]['name']) + "') ;")

#TableauSanctuaire
curseur.execute("DROP TABLE Sanctuaire ;")
curseur.execute("CREATE TABLE IF NOT EXISTS Sanctuaire(id INTEGER PRIMARY KEY, name TEXT, puzzle TEXT, id_Region INTEGER, CONSTRAINT fk_id_Region FOREIGN KEY (id_region) REFERENCES Region(id)) ;")
def sanctuaire_info(d) :
    """id, nom, puzzle et id_region des sanctuaires"""
    id_Sanctuaire = 0
    for r in range(len(d['region'])) :
        for s in range(len(d['region'][r]['shrines'])) :
            id_Sanctuaire += 1
            curseur.execute("INSERT INTO Sanctuaire VALUES (" + str(id_Sanctuaire) + ", '" + str(d['region'][r]['shrines'][s]['name']) + "', '" + str(d['region'][r]['shrines'][s]['puzzle']) + "', " + str(r+1) + " ) ;")
        for s_dlc in range(len(d['region'][r]['dlc_shrines'])) :
            id_Sanctuaire += 1
            curseur.execute("INSERT INTO Sanctuaire VALUES (" + str(id_Sanctuaire) + ", '" + str(d['region'][r]['dlc_shrines'][s_dlc]['name']) + "', '" + str(d['region'][r]['dlc_shrines'][s_dlc]['puzzle']) + "', " + str(r+1) + " ) ;")





#TableauVillages (villages)
curseur.execute("DROP TABLE Village ;")
curseur.execute("CREATE TABLE IF NOT EXISTS Village(id PRIMARY KEY, name, id_region, CONSTRAINT fk_id_Region FOREIGN KEY (id_region) REFERENCES Region(id)); ")
def village_info(d) :
    """id, nom et id_region des villages"""
    id_compteur = 0
    for r in range(len(d['region'])) :
        if d['region'][r]['settlements'] != [] :
            for v in range (len(d['region'][r]['settlements'])) :
                id_compteur += 1
                curseur.execute("INSERT INTO Village VALUES (" + str(id_compteur) + ", '" + str(d['region'][r]["settlements"][v]) + "', " + str(r+1) + ") ;")

#TableauLocalisation
curseur.execute("DROP TABLE Localisation ;")
curseur.execute("CREATE TABLE IF NOT EXISTS Localisation(id PRIMARY KEY, name, id_region, CONSTRAINT fk_id_Region FOREIGN KEY (id_region) REFERENCES Region(id)) ;")
def localisation_info(d) :
    """id, nom et id_region des localisations (ex : Creatures divines, plaines, chateau...)"""
    for l in range(len(d['locations'])) :
        curseur.execute("INSERT INTO Localisation VALUES (" + str(l+1) + ", '" + str(d['locations'][l]['name']) + "', " + str(d['locations'][l]['region']) + ") ;")



#TableauCreature
curseur.execute("DROP TABLE Creature ;")
curseur.execute("CREATE TABLE IF NOT EXISTS Creature(id PRIMARY KEY, name, description, common_location_1, common_location_2, common_location_3, edible)")
def creature_info(d) :
    """id, nom, description, location commune, ils droppent et consommable des creatures"""
    for c in range(len(d['creatures'])) :
        if len(d['creatures'][c]["common_locations"]) == 1 :
            curseur.execute("INSERT INTO Creature VALUES (" + str(c+1) + ", '" + str(d['creatures'][c]["name"]) + "', '" + str(d['creatures'][c]["description"]) + "', '" + str(d['creatures'][c]["common_locations"][0]) + "', 'Null', 'Null', '" + str(d['creatures'][c]["edible"]) + "') ;")
        elif len(d['creatures'][c]["common_locations"]) == 2 :
            curseur.execute("INSERT INTO Creature VALUES (" + str(c+1) + ", '" + str(d['creatures'][c]["name"]) + "', '" + str(d['creatures'][c]["description"]) + "', '" + str(d['creatures'][c]["common_locations"][0]) + "', '" + str(d['creatures'][c]["common_locations"][1]) + "', 'Null', '" + str(d['creatures'][c]["edible"]) + "') ;")
        elif len(d['creatures'][c]["common_locations"]) == 3 :
            curseur.execute("INSERT INTO Creature VALUES (" + str(c+1) + ", '" + str(d['creatures'][c]["name"]) + "', '" + str(d['creatures'][c]["description"]) + "', '" + str(d['creatures'][c]["common_locations"][0]) + "', '" + str(d['creatures'][c]["common_locations"][1]) + "', '" + str(d['creatures'][c]["common_locations"][2]) + "', '" + str(d['creatures'][c]["edible"]) + "') ;")
        else :
            curseur.execute("INSERT INTO Creature VALUES (" + str(c+1) + ", '" + str(d['creatures'][c]["name"]) + "', '" + str(d['creatures'][c]["description"]) + "', 'Null', 'Null', 'Null', '" + str(d['creatures'][c]["edible"]) + "') ;")

#TableauMonstre
curseur.execute("DROP TABLE Monstre ;")
curseur.execute("CREATE TABLE IF NOT EXISTS Monstre(id PRIMARY KEY, name, description, common_location_1, common_location_2, drops) ;")
def monstre_info(d) :
    """id, nom, description, location commune et le drop des monstres"""
    for m in range(len(d['monsters'])) :
        if len(d['monsters'][m]["common_locations"]) == 1 :
            if d['monsters'][m]["drops"] == [] :
                curseur.execute("INSERT INTO Monstre VALUES (" + str(m+1) + ", '" + str(d['monsters'][m]["name"]) + "', '" + str(d['monsters'][m]["description"]) + "', '" + str(d['monsters'][m]["common_locations"][0]) + "', 'Null', 'Null') ;")
            else :
                drops = d['monsters'][m]["drops"]
                string_drops = ''.join(map(str, drops))
                curseur.execute("INSERT INTO Monstre VALUES (" + str(m+1) + ", '" + str(d['monsters'][m]["name"]) + "', '" + str(d['monsters'][m]["description"]) + "', '" + str(d['monsters'][m]["common_locations"][0]) + "', 'Null', '" + str(string_drops) + "') ;")
        elif len(d['monsters'][m]["common_locations"]) == 2 :
            if d['monsters'][m]["drops"] == [] :
                curseur.execute("INSERT INTO Monstre VALUES (" + str(m+1) + ", '" + str(d['monsters'][m]["name"]) + "', '" + str(d['monsters'][m]["description"]) + "', '" + str(d['monsters'][m]["common_locations"][0]) + "', '" + str(d['monsters'][m]["common_locations"][1]) + "', 'Null') ;")
            else :
                drops = d['monsters'][m]["drops"]
                string_drops = ''.join(map(str, drops))
                curseur.execute("INSERT INTO Monstre VALUES (" + str(m+1) + ", '" + str(d['monsters'][m]["name"]) + "', '" + str(d['monsters'][m]["description"]) + "', '" + str(d['monsters'][m]["common_locations"][0]) + "', '" + str(d['monsters'][m]["common_locations"][1]) + "', '" + str(string_drops) + "') ;")
        else :
            if d['monsters'][m]["drops"] == [] :
                curseur.execute("INSERT INTO Monstre VALUES (" + str(m+1) + ", '" + str(d['monsters'][m]["name"]) + "', '" + str(d['monsters'][m]["description"]) + "', 'Null', 'Null', 'Null') ;")
            else :
                drops = d['monsters'][m]["drops"]
                string_drops = ''.join(map(str, drops))
                curseur.execute("INSERT INTO Monstre VALUES (" + str(m+1) + ", '" + str(d['monsters'][m]["name"]) + "', '" + str(d['monsters'][m]["description"]) + "', 'Null', 'Null', '" + str(string_drops) + "') ;")



#TableauMateriel
curseur.execute("DROP TABLE Materiel ;")
curseur.execute("CREATE TABLE IF NOT EXISTS Materiel(id PRIMARY KEY, name, description, common_locations_1, common_locations_2, hearts_recovered, cooking_effect)")
def materiel_info(d) :
    """id, nom, description, location commune, coeurs et effets des matériaux"""
    for m in range(len(d['materials'])) :
        if len(d['materials'][m]["common_locations"]) == 1 :
            curseur.execute("INSERT INTO Materiel VALUES (" + str(m+1) + ", '" + str(d['materials'][m]["name"]) + "', '" + str(d['materials'][m]["description"]) + "', '" + str(d['materials'][m]["common_locations"][0]) + "', 'Null', '" + str(d['materials'][m]["hearts_recovered"]) + "', '" + str(d['materials'][m]["cooking_effect"]) + "') ;")
        elif len(d['materials'][m]["common_locations"]) == 2 :
            curseur.execute("INSERT INTO Materiel VALUES (" + str(m+1) + ", '" + str(d['materials'][m]["name"]) + "', '" + str(d['materials'][m]["description"]) + "', '" + str(d['materials'][m]["common_locations"][0]) + "', '" + str(d['materials'][m]["common_locations"][1]) + "', '" + str(d['materials'][m]["hearts_recovered"]) + "', '" + str(d['materials'][m]["cooking_effect"]) + "') ;")
        else :
            curseur.execute("INSERT INTO Materiel VALUES (" + str(m+1) + ", '" + str(d['materials'][m]["name"]) + "', '" + str(d['materials'][m]["description"]) + "', 'Null', 'Null', '" + str(d['materials'][m]["hearts_recovered"]) + "', '" + str(d['materials'][m]["cooking_effect"]) + "') ;")




#TableauEquipement
curseur.execute("DROP TABLE Equipement ;")
curseur.execute("CREATE TABLE IF NOT EXISTS Equipement(id PRIMARY KEY, name, description, common_location_1, common_location_2, attack, defense)")
def equipement_info(d) :
    """id, nom, description, location commune, attaque et defense des equipements"""
    for e in range(len(d['equipement'])) :
        if d['equipement'][e]["common_locations"] == "null" :
            curseur.execute("INSERT INTO Equipement VALUES (" + str(e+1) + ", '" + str(d['equipement'][e]["name"]) + "', '" + str(d['equipement'][e]["description"]) + "', 'null', 'null', '" + str(d['equipement'][e]["properties"]["attack"]) + "', '" + str(d['equipement'][e]["properties"]["defense"]) + "')")
        elif len(d['equipement'][e]["common_locations"]) == 1 :
            curseur.execute("INSERT INTO Equipement VALUES (" + str(e+1) + ", '" + str(d['equipement'][e]["name"]) + "', '" + str(d['equipement'][e]["description"]) + "', '" + str(d['equipement'][e]["common_locations"][0]) + "', 'null', '" + str(d['equipement'][e]["properties"]["attack"]) + "', '" + str(d['equipement'][e]["properties"]["defense"]) + "')")
        elif len(d['equipement'][e]["common_locations"]) == 2 :
            curseur.execute("INSERT INTO Equipement VALUES (" + str(e+1) + ", '" + str(d['equipement'][e]["name"]) + "', '" + str(d['equipement'][e]["description"]) + "', '" + str(d['equipement'][e]["common_locations"][0]) + "', '" + str(d['equipement'][e]["common_locations"][1]) + "', '"  + str(d['equipement'][e]["properties"]["attack"]) + "', '" + str(d['equipement'][e]["properties"]["defense"]) + "')")

#TableauTresor
curseur.execute("DROP TABLE Tresor ;")
curseur.execute("CREATE TABLE IF NOT EXISTS Tresor(id PRIMARY KEY, name, description, common_locations_1, common_location_2, drops)")
def tresor_info(d) :
    """id, nom, description, location commune et le drop des tresors"""
    for t in range(len(d['treasure'])) :
        if d['treasure'][t]["common_locations"] == "null" :
            if d['treasure'][t]["drops"] == [] :
                curseur.execute("INSERT INTO Tresor VALUES (" + str(t+1) + ", '" + str(d['treasure'][t]["name"]) + "', '" + str(d['treasure'][t]["description"]) + "', 'Null', 'Null', 'Null')")
            else :
                drops = d['treasure'][t]["drops"]
                string_drops = ''.join(map(str, drops))
                curseur.execute("INSERT INTO Tresor VALUES (" + str(t+1) + ", '" + str(d['treasure'][t]["name"]) + "', '" + str(d['treasure'][t]["description"]) + "', 'Null', 'Null', '" + str(string_drops) + "')")
        elif len(d['treasure'][t]["common_locations"]) == 1 :
            if d['treasure'][t]["drops"] == [] :
                curseur.execute("INSERT INTO Tresor VALUES (" + str(t+1) + ", '" + str(d['treasure'][t]["name"]) + "', '" + str(d['treasure'][t]["description"]) + "', '" + str(d['treasure'][t]["common_locations"][0]) + "', 'Null', 'Null')")
            else :
                drops = d['treasure'][t]["drops"]
                string_drops = ''.join(map(str, drops))
                curseur.execute("INSERT INTO Tresor VALUES (" + str(t+1) + ", '" + str(d['treasure'][t]["name"]) + "', '" + str(d['treasure'][t]["description"]) + "', '" + str(d['treasure'][t]["common_locations"][0]) + "', 'Null', '" + str(string_drops) + "')")
        elif len(d['treasure'][t]["common_locations"]) == 2 :
            if d['treasure'][t]["drops"] == [] :
                curseur.execute("INSERT INTO Tresor VALUES (" + str(t+1) + ", '" + str(d['treasure'][t]["name"]) + "', '" + str(d['treasure'][t]["description"]) + "', '" + str(d['treasure'][t]["common_locations"][0]) + "', '" + str(d['treasure'][t]["common_locations"][1]) + "', 'Null')")
            else :
                drops = d['treasure'][t]["drops"]
                string_drops = ''.join(map(str, drops))
                curseur.execute("INSERT INTO Tresor VALUES (" + str(t+1) + ", '" + str(d['treasure'][t]["name"]) + "', '" + str(d['treasure'][t]["description"]) + "', '" + str(d['treasure'][t]["common_locations"][0]) + "', '" + str(d['treasure'][t]["common_locations"][1]) + "', '" + str(string_drops) + "')")





region_info(d)
sanctuaire_info(d)
localisation_info(d)
village_info(d)
creature_info(d)
monstre_info(d)
materiel_info(d)
equipement_info(d)
tresor_info(d)

connexion.commit()
curseur.close()
connexion.close()


###faudra recoder tous les effets je pense ptdr. faire une fonction choix. Faire une fonction de fin de tour qui reinitialise tout a zero