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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
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
        "dlc": "true"
    }

]

, 'ame_bonus' :
[
    {
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
    }

]


, 'tresor' :

[
    {
        "id": 1,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 2,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 3,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 4,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 5,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 6,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 7,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 8,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 9,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 10,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 11,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 12,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 13,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 14,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 15,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 16,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 17,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 18,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 19,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 20,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 21,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 22,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 23,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 24,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 25,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 26,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 27,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 28,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 29,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 30,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 31,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 32,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 33,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 34,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 35,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 36,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 37,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 38,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 39,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 40,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 41,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 42,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 43,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 44,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 45,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 46,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 47,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 48,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 49,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 50,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 51,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 52,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 53,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 54,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 55,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 56,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 57,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 58,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 59,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 60,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 61,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 62,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 63,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 64,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 65,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 66,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 67,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 68,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 69,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 70,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 71,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 72,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 73,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 74,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 75,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 76,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 77,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 78,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 79,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 80,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 81,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 82,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 83,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 84,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 85,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 86,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 87,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 88,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 89,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 90,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 91,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 92,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 93,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 94,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 95,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 96,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 97,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 98,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 99,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 100,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 101,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 102,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 103,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 104,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 105,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 106,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 107,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 108,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 109,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 110,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 111,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 112,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 113,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 114,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 115,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 116,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 117,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 118,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 119,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 120,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 121,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 122,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 123,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 124,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 125,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 126,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 127,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 128,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 129,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 130,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 131,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 132,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 133,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 134,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 135,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 136,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 137,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 138,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 139,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 140,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 141,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 142,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 143,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 144,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 145,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 146,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 147,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 148,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 149,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 150,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 151,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 152,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 153,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 154,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 155,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 156,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 157,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    },
    {
        "id": 158,
        "name": "",
        "engagement": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "tresor",
        "dlc": "false"
    }
]

, 'butin' :
[{
        "id": 1,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 2,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 3,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 4,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 5,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 6,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 7,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 8,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 9,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 10,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 11,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 12,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 13,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 14,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 15,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 16,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 17,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 18,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 19,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 20,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 21,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 22,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 23,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 24,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 25,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 26,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 27,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 28,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 29,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 30,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 31,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 32,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 33,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 34,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 35,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 36,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 37,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 38,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 39,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 40,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 41,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 42,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 43,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 44,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 45,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 46,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 47,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 48,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 49,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 50,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
     {
        "id": 51,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 52,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 53,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 54,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 55,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 56,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 57,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 58,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 59,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 60,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 61,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 62,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 63,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 64,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 65,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 66,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 67,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 68,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 69,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 70,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 71,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 72,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 73,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 74,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 75,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 76,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 77,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 78,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 79,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 80,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 81,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 82,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 83,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 84,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 85,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 86,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 87,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 88,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 89,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 90,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 91,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 92,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 93,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 94,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 95,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 96,
        "name": "",
        "defausse": "Y/N",
        "effects": [
            ""
        ],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 97,
        "name": "",
        "defausse": "Y/N",
        "effects": [""],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 98,
        "name": "",
        "defausse": "Y/N",
        "effects": [""],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 99,
        "name": "",
        "defausse": "Y/N",
        "effects": [""],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 100,
        "name": "",
        "defausse": "Y/N",
        "effects": [""],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 101,
        "name": "",
        "defausse": "Y/N",
        "effects": [""],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 102,
        "name": "",
        "defausse": "Y/N",
        "effects": [""],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    },
    {
        "id": 103,
        "name": "",
        "defausse": "Y/N",
        "effects": [""],
        "image": "x",
        "category": "butin",
        "dlc": "false"
    }
]

, 'personnage' :

[{
        "id": 1,
        "name": "Blue Baby",
        "pv": 2,
        "atk": 1,
        "eternel": 1,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "false"
    },
    {
        "id": 2,
        "name": "Cain",
        "pv": 2,
        "atk": 1,
        "eternel": 2,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "false"
    },
    {
        "id": 3,
        "name": "Eve",
        "pv": 2,
        "atk": 1,
        "eternel": 3,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "false"
    },
    {
        "id": 4,
        "name": "Isaac",
        "pv": 2,
        "atk": 1,
        "eternel": 4,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "false"
    },
    {
        "id": 5,
        "name": "Judas",
        "pv": 2,
        "atk": 1,
        "eternel": 5,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "false"
    },
    {
        "id": 6,
        "name": "Lazarus",
        "pv": 2,
        "atk": 1,
        "eternel": 6,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "false"
    },
    {
        "id": 7,
        "name": "Lilith",
        "pv": 2,
        "atk": 1,
        "eternel": 7,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "false"
    },
    {
        "id": 8,
        "name": "Maggy",
        "pv": 2,
        "atk": 1,
        "eternel": 8,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "false"
    },
    {
        "id": 9,
        "name": "Samson",
        "pv": 2,
        "atk": 1,
        "eternel": 9,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "false"
    },
    {
        "id": 10,
        "name": "The Forgotten ",
        "pv": 2,
        "atk": 1,
        "eternel": 10,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "false"
    },
    {
        "id": 11,
        "name": "The Lost",
        "pv": 2,
        "atk": 1,
        "eternel": 11,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "true"
    },
    {
        "id": 12,
        "name": "The Keeper",
        "pv": 2,
        "atk": 1,
        "eternel": 12,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "true"
    },
    {
        "id": 13,
        "name": "Azazel",
        "pv": 2,
        "atk": 1,
        "eternel": 13,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "true"
    },
    {
        "id": 14,
        "name": "Apollyon",
        "pv": 2,
        "atk": 1,
        "eternel": 14,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "true"
    },
    {
        "id": 15,
        "name": "Bum-Bo",
        "pv": 2,
        "atk": 1,
        "eternel": 15,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "true"
    },
    {
        "id": 16,
        "name": "Dark Judas",
        "pv": 2,
        "atk": 1,
        "eternel": 16,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "true"
    },
    {
        "id": 17,
        "name": "Guppy",
        "pv": 2,
        "atk": 1,
        "eternel": 17,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "true"
    },
    {
        "id": 18,
        "name": "Whore of Babylon",
        "pv": 2,
        "atk": 1,
        "eternel": 18,
        "main": [""],
        "tresor": [""],
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "true"
    },
    {
        "id": 19,
        "name": "Eden",
        "pv": 2,
        "atk": 1,
        "eternel": "piocher trois tresor et faites l'un d'eux votre eternel", ###a recoder
        "main": [""],
        "tresor": "",
        "action_tour": 1,
        "action_engagement": 1,
        "combat": 1,
        "image": "x",
        "category": "personnage",
        "dlc": "false"
    }
]


, 'eternel' :

[
    {
        "id": 1,
        "name": "Forever Alone",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "false"
    },
    {
        "id": 2,
        "name": "Sleight of Hand ",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "false"
    },
    {
        "id": 3,
        "name": "The Curse",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "false"
    },
    {
        "id": 4,
        "name": "D6",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "false"
    },
    {
        "id": 5,
        "name": "Book of Belial",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "false"
    },
    {
        "id": 6,
        "name": "Lazarus' Rags",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "false"
    },
    {
        "id": 7,
        "name": "Incubus",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "false"
    },
    {
        "id": 8,
        "name": "Yum Heart",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "false"
    },
    {
        "id": 9,
        "name": "Blood Lust",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "false"
    },
    {
        "id": 10,
        "name": "The Bone",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "false"
    },
    {
        "id": 11,
        "name": "Holy Mantle",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "true"
    },
    {
        "id": 12,
        "name": "Wooden Nickel",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "true"
    },
    {
        "id": 13,
        "name": "Lord of the Pit",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "true"
    },
    {
        "id": 14,
        "name": "Void",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "true"
    },
    {
        "id": 15,
        "name": "Bag-o-Trash",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "true"
    },
    {
        "id": 16,
        "name": "Dark Arts",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "true"
    },
    {
        "id": 17,
        "name": "Infested",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "true"
    },
    {
        "id": 18,
        "name": "Gimpy",
        "engagement": "Y/N",
        "effects" : [""],
        "image": "x",
        "category": "eternel",
        "dlc": "true"
    }
]

}




conn = sqlite3.connect('test1_isaac.db')
cursor = conn.cursor()

#TableauRegion
cursor.execute("DROP TABLE Region ;")
cursor.execute("CREATE TABLE IF NOT EXISTS Region(id INTEGER PRIMARY KEY, name TEXT) ;")
def region_info(d) :
    """id et nom des regions"""
    for r in range(len(d['region'])) :
        cursor.execute("INSERT INTO Region VALUES (" + str(r+1) + ", '" + str(d['region'][r]['name']) + "') ;")

#TableauSanctuaire
cursor.execute("DROP TABLE Sanctuaire ;")
cursor.execute("CREATE TABLE IF NOT EXISTS Sanctuaire(id INTEGER PRIMARY KEY, name TEXT, puzzle TEXT, id_Region INTEGER, CONSTRAINT fk_id_Region FOREIGN KEY (id_region) REFERENCES Region(id)) ;")
def sanctuaire_info(d) :
    """id, nom, puzzle et id_region des sanctuaires"""
    id_Sanctuaire = 0
    for r in range(len(d['region'])) :
        for s in range(len(d['region'][r]['shrines'])) :
            id_Sanctuaire += 1
            cursor.execute("INSERT INTO Sanctuaire VALUES (" + str(id_Sanctuaire) + ", '" + str(d['region'][r]['shrines'][s]['name']) + "', '" + str(d['region'][r]['shrines'][s]['puzzle']) + "', " + str(r+1) + " ) ;")
        for s_dlc in range(len(d['region'][r]['dlc_shrines'])) :
            id_Sanctuaire += 1
            cursor.execute("INSERT INTO Sanctuaire VALUES (" + str(id_Sanctuaire) + ", '" + str(d['region'][r]['dlc_shrines'][s_dlc]['name']) + "', '" + str(d['region'][r]['dlc_shrines'][s_dlc]['puzzle']) + "', " + str(r+1) + " ) ;")





#TableauVillages (villages)
cursor.execute("DROP TABLE Village ;")
cursor.execute("CREATE TABLE IF NOT EXISTS Village(id PRIMARY KEY, name, id_region, CONSTRAINT fk_id_Region FOREIGN KEY (id_region) REFERENCES Region(id)); ")
def village_info(d) :
    """id, nom et id_region des villages"""
    id_compteur = 0
    for r in range(len(d['region'])) :
        if d['region'][r]['settlements'] != [] :
            for v in range (len(d['region'][r]['settlements'])) :
                id_compteur += 1
                cursor.execute("INSERT INTO Village VALUES (" + str(id_compteur) + ", '" + str(d['region'][r]["settlements"][v]) + "', " + str(r+1) + ") ;")

#TableauLocalisation
cursor.execute("DROP TABLE Localisation ;")
cursor.execute("CREATE TABLE IF NOT EXISTS Localisation(id PRIMARY KEY, name, id_region, CONSTRAINT fk_id_Region FOREIGN KEY (id_region) REFERENCES Region(id)) ;")
def localisation_info(d) :
    """id, nom et id_region des localisations (ex : Creatures divines, plaines, chateau...)"""
    for l in range(len(d['locations'])) :
        cursor.execute("INSERT INTO Localisation VALUES (" + str(l+1) + ", '" + str(d['locations'][l]['name']) + "', " + str(d['locations'][l]['region']) + ") ;")



#TableauCreature
cursor.execute("DROP TABLE Creature ;")
cursor.execute("CREATE TABLE IF NOT EXISTS Creature(id PRIMARY KEY, name, description, common_location_1, common_location_2, common_location_3, edible)")
def creature_info(d) :
    """id, nom, description, location commune, ils droppent et consommable des creatures"""
    for c in range(len(d['creatures'])) :
        if len(d['creatures'][c]["common_locations"]) == 1 :
            cursor.execute("INSERT INTO Creature VALUES (" + str(c+1) + ", '" + str(d['creatures'][c]["name"]) + "', '" + str(d['creatures'][c]["description"]) + "', '" + str(d['creatures'][c]["common_locations"][0]) + "', 'Null', 'Null', '" + str(d['creatures'][c]["edible"]) + "') ;")
        elif len(d['creatures'][c]["common_locations"]) == 2 :
            cursor.execute("INSERT INTO Creature VALUES (" + str(c+1) + ", '" + str(d['creatures'][c]["name"]) + "', '" + str(d['creatures'][c]["description"]) + "', '" + str(d['creatures'][c]["common_locations"][0]) + "', '" + str(d['creatures'][c]["common_locations"][1]) + "', 'Null', '" + str(d['creatures'][c]["edible"]) + "') ;")
        elif len(d['creatures'][c]["common_locations"]) == 3 :
            cursor.execute("INSERT INTO Creature VALUES (" + str(c+1) + ", '" + str(d['creatures'][c]["name"]) + "', '" + str(d['creatures'][c]["description"]) + "', '" + str(d['creatures'][c]["common_locations"][0]) + "', '" + str(d['creatures'][c]["common_locations"][1]) + "', '" + str(d['creatures'][c]["common_locations"][2]) + "', '" + str(d['creatures'][c]["edible"]) + "') ;")
        else :
            cursor.execute("INSERT INTO Creature VALUES (" + str(c+1) + ", '" + str(d['creatures'][c]["name"]) + "', '" + str(d['creatures'][c]["description"]) + "', 'Null', 'Null', 'Null', '" + str(d['creatures'][c]["edible"]) + "') ;")

#TableauMonstre
cursor.execute("DROP TABLE Monstre ;")
cursor.execute("CREATE TABLE IF NOT EXISTS Monstre(id PRIMARY KEY, name, description, common_location_1, common_location_2, drops) ;")
def monstre_info(d) :
    """id, nom, description, location commune et le drop des monstres"""
    for m in range(len(d['monsters'])) :
        if len(d['monsters'][m]["common_locations"]) == 1 :
            if d['monsters'][m]["drops"] == [] :
                cursor.execute("INSERT INTO Monstre VALUES (" + str(m+1) + ", '" + str(d['monsters'][m]["name"]) + "', '" + str(d['monsters'][m]["description"]) + "', '" + str(d['monsters'][m]["common_locations"][0]) + "', 'Null', 'Null') ;")
            else :
                drops = d['monsters'][m]["drops"]
                string_drops = ''.join(map(str, drops))
                cursor.execute("INSERT INTO Monstre VALUES (" + str(m+1) + ", '" + str(d['monsters'][m]["name"]) + "', '" + str(d['monsters'][m]["description"]) + "', '" + str(d['monsters'][m]["common_locations"][0]) + "', 'Null', '" + str(string_drops) + "') ;")
        elif len(d['monsters'][m]["common_locations"]) == 2 :
            if d['monsters'][m]["drops"] == [] :
                cursor.execute("INSERT INTO Monstre VALUES (" + str(m+1) + ", '" + str(d['monsters'][m]["name"]) + "', '" + str(d['monsters'][m]["description"]) + "', '" + str(d['monsters'][m]["common_locations"][0]) + "', '" + str(d['monsters'][m]["common_locations"][1]) + "', 'Null') ;")
            else :
                drops = d['monsters'][m]["drops"]
                string_drops = ''.join(map(str, drops))
                cursor.execute("INSERT INTO Monstre VALUES (" + str(m+1) + ", '" + str(d['monsters'][m]["name"]) + "', '" + str(d['monsters'][m]["description"]) + "', '" + str(d['monsters'][m]["common_locations"][0]) + "', '" + str(d['monsters'][m]["common_locations"][1]) + "', '" + str(string_drops) + "') ;")
        else :
            if d['monsters'][m]["drops"] == [] :
                cursor.execute("INSERT INTO Monstre VALUES (" + str(m+1) + ", '" + str(d['monsters'][m]["name"]) + "', '" + str(d['monsters'][m]["description"]) + "', 'Null', 'Null', 'Null') ;")
            else :
                drops = d['monsters'][m]["drops"]
                string_drops = ''.join(map(str, drops))
                cursor.execute("INSERT INTO Monstre VALUES (" + str(m+1) + ", '" + str(d['monsters'][m]["name"]) + "', '" + str(d['monsters'][m]["description"]) + "', 'Null', 'Null', '" + str(string_drops) + "') ;")



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