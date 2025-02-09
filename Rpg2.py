# -*- coding: utf-8 -*-

import random

class Inventaire:
    def __init__(self, stock_max):
        self.nb_objet = []  # Initialise nb_objet comme une liste vide par défaut
        self.stock_max = stock_max
        
    def retirer_objet(self, objet): 
        if objet in self.nb_objet: 
            self.nb_objet.remove(objet) 
        
    def contient_objet(self, objet): 
        return objet in self.nb_objet
    
    def __str__(self):
        inventaire_str = f"Inventaire : {len(self.nb_objet)} objet(s) sur {self.stock_max}\n"
        inventaire_str += "\n".join([str(item) for item in self.nb_objet])
        return inventaire_str

    def ajouter_objet(self, objet):
        if len(self.nb_objet) < self.stock_max:
            self.nb_objet.append(objet)
        else:
            print("Inventaire plein, impossible d'ajouter l'objet")

class Personnage:
    def __init__(self, nom, lvl, pv, force, defense, agilite, xp, nb_obj_max, inventaire, tete, corps, brasG, brasD, jambeG, jambeD, pv_max, xp_max): # self.effets = []
        self.nom = nom 
        self.lvl = lvl
        self.pv = pv
        self.force = force
        self.defense = defense
        self.agilite = agilite
        self.xp = xp
        self.nb_obj_max = nb_obj_max
        self.inventaire = inventaire  # Référence à l'objet Inventaire du personnage
        self.tete = tete
        self.corps = corps
        self.brasG = brasG
        self.brasD = brasD
        self.jambeG = jambeG
        self.jambeD = jambeD
        self.all_body = {
            "tete": self.tete, 
            "corps": self.corps,
            "bras_g": self.brasG, 
            "bras_d": self.brasD, 
            "jambe_g": self.jambeG, 
            "jambe_d": self.jambeD 
            }         #Dictinnaire ou list ?
        self.pv_max = pv_max
        self.xp_max = xp_max 
        self.effets = []  # Liste vide pour les effets

    def __str__(self):
        return (f"Nom: {self.nom}, Niveau: {self.lvl}, Force: {self.force}, "
                f"Défense: {self.defense}, XP: {self.xp}, "
                f"Effets: {self.effets}, PV: {self.pv}, "
                f"Tête: {self.tete}, Corps: {self.corps}, "
                f"Bras Gauche: {self.brasG}, Bras Droit: {self.brasD}, "
                f"Jambe Gauche: {self.jambeG}, Jambe Droite: {self.jambeD}")
    
    def afficher_all_body(self):
        print(self.tete.nom, ":", self.corps.nom, ":", self.brasG.nom, ":", self.brasD.nom, ":", self.jambeG.nom, ":", self.jambeD.nom)

    def affiche_inv(self):
        print(self.inventaire)

    def attaquer(self, cible):
        CC = random.randint(0, 100) 
        Touch = random.randint(0, 100) 
        
        if Touch <= 10:
            print("Vous avez manqué votre coup !") 
            return 
        else: 
            if CC <= 50: 
                print("Pas coup critique") 
                print(cible.all_body) 
                print("Quelle partie du corps souhaitez-vous attaquer ?") 
                partie = input()
                if partie in cible.all_body.keys(): 
                    print(self.all_body.keys()) 
                    print("Avec quelle partie de votre corps souhaitez-vous l'attaquer ?") 
                    reponse = input()
                    if reponse in self.all_body.keys(): 
                        degats_sup = self.all_body[reponse].degat #Rajoute les degat de la partie du corps utilisé
                        print("Degat_sup", degats_sup)
                        degats = max(0, (self.force + degats_sup) - cible.defense) 
                        cible.all_body[partie] = max(0, cible.all_body[partie] - degats) 
                        cible.pv = sum(cible.all_body.values()) 
                        if partie in ["tete", "jambeG", "jambeD"]: 
                            print(f"{cible.nom} a subi {degats} dégâts à la {partie}. PV restants: {cible.pv}") 
                        else:
                            print(f"{cible.nom} a subi {degats} dégâts au {partie}. PV restants: {cible.pv}")
                    else: 
                        print("Partie de votre corps non reconnue.")
                else:
                    print("Partie du corps ciblé non reconnue.")
            
            else: 
                print("Coups Critiques") 
                print(cible.afficher_all_body()) 
                print("Quelle partie du corps souhaitez-vous attaquer ?") 
                partie = input()
                if partie in cible.all_body.keys():
                    print(self.all_body.keys())
                    print("Avec quelle partie de votre corps souhaitez-vous l'attaquer ?") 
                    reponse = input()
                    if reponse in self.all_body.keys():
                        degats_sup = self.all_body[reponse].degat
                        print("Degat_sup", degats_sup)
                        degats = max(0, (self.force + degats_sup) - cible.defense) * 2 # Coups Critiques 
                        cible.all_body[partie] = max(0, cible.all_body[partie] - degats) 
                        cible.pv = sum(cible.all_body.values()) 
                        if partie in ["tete", "jambeG", "jambeD"]: 
                            print(f"{cible.nom} a subi {degats} dégâts à la {partie}. PV restants: {cible.pv}")
                        else: 
                            print(f"{cible.nom} a subi {degats} dégâts au {partie}. PV restants: {cible.pv}")
                    else: 
                        print("Partie de votre corps non reconnue.") 
                else: 
                    print("Partie du corps ciblé non reconnue.")

    def Ramasser_objet(self, objet):
        if len(self.inventaire.nb_objet) < self.nb_obj_max:
            self.inventaire.ajouter_objet(objet)
        else:
            print("Vous avez trop d'objets dans votre inventaire")
            print("Voulez-vous jeter un ou plusieurs objets ?")
            reponse = input("Un pour jeter un objet, Plusieurs pour de nombreux objets, Non pour ne pas jeter d'objet ?:\n ")
            if reponse == "Un":
                print(self.inventaire.nb_objet)
                objet_jete = input("Quel objet voulez-vous jeter ?\n")
                if objet_jete in self.inventaire.nb_objet:
                    self.inventaire.nb_objet.remove(objet_jete)
                    self.inventaire.ajouter_objet(objet)
                else:
                    print("Cet objet n'est pas dans votre inventaire !")
            elif reponse == "Plusieurs":
                print(self.inventaire.nb_objet)
                print("Combien d'objets exactement voulez-vous jeter ?")
                reponse2 = int(input("Exemple = 3:\n"))
                for i in range(reponse2):
                    print(self.inventaire.nb_objet)
                    objet_jete = input("Quel objet voulez-vous jeter ?\n")
                    if objet_jete in self.inventaire.nb_objet:
                        self.inventaire.nb_objet.remove(objet_jete)
                print("Vous êtes arrivé au bout du nombre souhaité !")
                self.inventaire.ajouter_objet(objet)
            elif reponse.lower() == "non":
                print("Vous n'avez pas jeté d'objet ! Vous ne pouvez donc pas ramasser l'objet")

    def use_potion(self): 
        self.affiche_inv() 
        print("Quel type de potion souhaitez-vous utiliser ?") 
        type_potion = input("Ex : Soin moyen ?:\n").lower() 
        potions_trouvees = [objet for objet in self.inventaire.nb_objet if objet.type == type_potion] 
        if potions_trouvees: 
            print(f"Êtes-vous sûr de vouloir utiliser une potion de {type_potion} ?")
            reponse2 = input("Oui/Non : ").lower() 
            if reponse2 == "oui": 
                for potion in potions_trouvees: 
                    #Soin
                    if potion.type.lower() == "soin":
                        self._utiliser_potion_soin(potion) 
                        print(f"Une potion de {type_potion} a été utilisée avec succès !")
                        print(f"Vous avez {self.pv} points de vie !")
                    elif potion.type.lower() == "soin":
                        self._utiliser_potion_soin(potion) 
                        print(f"Une potion de {type_potion} a été utilisée avec succès !")
                        print(f"Vous avez {self.pv} points de vie !")
                    elif potion.type.lower() == "soin moyen":
                        self._utiliser_potion_soin(potion) 
                        print(f"Une potion de {type_potion} a été utilisée avec succès !")
                        print(f"Vous avez {self.pv} points de vie !")
                    elif potion.type.lower() == "soin fort":
                        self._utiliser_potion_soin(potion) 
                        print(f"Une potion de {type_potion} a été utilisée avec succès !")
                        print(f"Vous avez {self.pv} points de vie !")
                    #Force
                    elif potion.type.lower() == "force faible": 
                        self._utiliser_potion_force(potion)
                        print(f"Une potion de {type_potion} a été utilisée avec succès !")
                        print(f"Vous avez {self.force} points de force !")
                    elif potion.type.lower() == "force": 
                        self._utiliser_potion_force(potion)
                        print(f"Une potion de {type_potion} a été utilisée avec succès !")
                        print(f"Vous avez {self.force} points de force !")
                    elif potion.type.lower() == "force moyenne":
                        self._utiliser_potion_force(potion)
                        print(f"Une potion de {type_potion} a été utilisée avec succès !")
                        print(f"Vous avez {self.force} points de force !")
                    elif potion.type.lower() == "force puissante":
                        self._utiliser_potion_force(potion)
                        print(f"Une potion de {type_potion} a été utilisée avec succès !")
                        print(f"Vous avez {self.force} points de force !")
                    #Agilite
                    elif potion.type.lower() == "agilite faible": 
                        self._utiliser_potion_agilite(potion) 
                        print(f"Une potion de {type_potion} a été utilisée avec succès !") 
                        print(f"Vous avez gagné {self.agilite} points d'agilité !")
                    elif potion.type.lower() == "agilite moyenne":
                        self._utiliser_potion_agilite(potion) 
                        print(f"Une potion de {type_potion} a été utilisée avec succès !") 
                        print(f"Vous avez gagné {self.agilite} points d'agilité !")
                    elif potion.type.lower() == "agilite puissante":
                        self._utiliser_potion_agilite(potion) 
                        print(f"Une potion de {type_potion} a été utilisée avec succès !") 
                        print(f"Vous avez gagné {self.agilite} points d'agilité !")
                    else: 
                        print("Vous avez annulé l'utilisation de l'objet !") 
            else: 
                print(f"Vous n'avez pas de potion de {type_potion} dans votre inventaire !") 

    def _utiliser_potion_soin(self, potion): 
        if potion.lvl <= 3: 
            self.pv += 50
        elif 4 <= potion.lvl <= 6: 
            self.pv += 130
        elif 7 <= potion.lvl <= 10: 
            self.pv += 200
        else: 
            self.pv += 300
        self.inventaire.retirer_objet(potion) 

    def _utiliser_potion_force(self, potion): 
        if potion.lvl <= 3: 
            self.force += 5 
        elif 4 <= potion.lvl <= 6:
            self.force += 15 
        elif 7 <= potion.lvl <= 10: 
            self.force += 30 
        self.inventaire.retirer_objet(potion) 

    def _utiliser_potion_agilite(self, potion): 
        if potion.lvl <= 3: 
            self.agilite += 5 
        elif 4 <= potion.lvl <= 6: 
            self.agilite += 15 
        elif 7 <= potion.lvl <= 10: 
            self.agilite += 30
        self.inventaire.retirer_objet(potion)

    def monter_niveau(self):
        self.lvl += 1
        print(f"{self.nom} est passé au niveau {self.lvl} !")
        #print("Vous avez x points de compétence à répartir")
        self.force += 2
        self.defense += 2
        self.pv += 10
        self.xp_max = self.xp_max * 1.75

class Potion:
    def __init__(self, name, lvl, type):
        self.name = name
        self.lvl = lvl
        self.type = type 

    def __str__(self):
        return (f"Nom: {self.name}, Niveau: {self.lvl}")


class Arme:
    def __init__(self, nom, lvl, xp, xp_max, degat, defense, agilite):
        self.nom = nom
        self.lvl = lvl
        self.xp = xp
        self.xp_max = xp_max
        self.degat = degat
        self.defense = defense
        self.agilite = agilite

    def __str__(self):
        return f"Nom: {self.nom}, Niveau: {self.lvl}, XP: {self.xp}, XP_max: {self.xp_max}, Dégâts: {self.degat}, Defense: {self.defense}, Agilité : {self.agilite}"
    
    def upgrade(self):
        self.lvl += 1
        self.degat += 6
        self.agilite += 4
        self.defense = 5
        self.xp = 0
        self.xp_max = self.xp_max * 1.25
        print(f"Votre {self.nom} est passé au lvl {self.lvl} !")
        print("Ses dégats augmentent de 6 , la defense de 5 et l'agilité de 4 !")
        print(f"Le prochain niveau sera atteint lorsque l'xp de votre {self.nom} aura atteint {self.xp_max}")


class Ennemi:
    def __init__(self, nom, lvl, pv_tete, pv_corps, pv_brasG, pv_brasD, pv_jambeG, pv_jambeD, degat, defense, agilite):
        self.nom = nom
        self.lvl = lvl
        self.tete = int(pv_tete)
        self.corps = int(pv_corps)
        self.brasG = int(pv_brasG)
        self.brasD = int(pv_brasD)
        self.jambeG = int(pv_jambeG)
        self.jambeD = int(pv_jambeD)
        self.all_body = {
            'tete': self.tete,
            'corps': self.corps,
            'brasG': self.brasG,
            'brasD': self.brasD,
            'jambeG': self.jambeG,
            'jambeD': self.jambeD
        }
        self.pv = self.pv_total()
        self.degat = degat
        self.defense = defense
        self.agilite = agilite

    def __str__(self):
        return (f"Nom: {self.nom}, Niveau: {self.lvl}, PV: {self.pv_total()}, "
                f"Tête: {self.tete}, Corps: {self.corps}, "
                f"Bras Gauche: {self.brasG}, Bras Droit: {self.brasD}, "
                f"Jambe Gauche: {self.jambeG}, Jambe Droite: {self.jambeD}")

    def pv_total(self):
        return sum(self.all_body.values())
    
    def afficher_all_body(self): # Vraiment necessaire ? reference a cette fonction dans la methode de classe attaquer du personnage 
        print(self.all_body.keys()) # Pourquoi la ligne fonctionne correctement mais affiche none a la fin ?

    def attaquer(self, cible):
        CC = random.randint(0, 100)
        Touch = random.randint(0, 100)

        if Touch <= 10:
            print(f"{self.nom} a manqué son coup !")
            return
        else:
            if CC <= 50:
                degats = max(0, self.degat - cible.defense)
                cible.pv = cible.pv - degats # Mise à jour des PV totaux
                print(f"{self.nom} a attaqué {cible.nom} et a infligé {degats} degats ! Il vous reste {cible.pv} point de vie !")
            else:
                degats = max(0, self.degat - cible.defense) * 2
                cible.pv = cible.pv - degats # Mise à jour des PV totaux
                print(f"{self.nom} a attaqué {cible.nom} et a infligé {degats} degats ! Il vous reste {cible.pv} point de vie !")


# Créez un inventaire et ajoutez des potions
sac = Inventaire(10)
potions = [
    Potion("Soin", 5, "soin"), Potion("Soin moyen", 8, "soin moyen"), Potion("Soin faible", 2, "soin faible"), Potion("Soin fort", 12, "soin fort"),
    Potion("Force", 5, "force"), Potion("Force faible", 2, "force faible"), Potion("Force moyen", 7, "force moyenne"), Potion("Force puissante", 9, "force puissante"),
    Potion("Agilite faible", 1, "agilite faible"), Potion("Agilite moyenne", 5, "agilite moyenne"), Potion("Agilite puissante", 8, "agilite puissante")
]

for potion in potions:
    sac.ajouter_objet(potion)




# Fonction de combat
def combat(perso1, perso2):
    print("Le combat commence !")
    print(f"Le nom de votre adversaire est {perso2.nom} et son niveau est de {perso2.lvl}")
    print(f"Il a {perso2.pv} points de vie")
    if perso2.lvl > perso1.lvl:
        print("Il est plus fort que vous , par consequant il arrive a masquer son agilité !")
    else:
        print(f"Ses caracteristiques sont : Force = {perso2.force}, Agilité = {perso2.agilite}, Defense = {perso2.defense}")
    heal_mark = False
    while perso1.pv > 0 and perso2.pv > 0:
        print("Stats adversaire:", perso2.all_body)
        print("Que voulez-vous faire ?")
        print("Attaquer = 1")
        print("Utiliser objet = 2")
        print("Fuir = 3")
        reponse = int(input())
        if reponse == 1:
            for i in perso2.all_body:
                instance_v = perso2.all_body[i]
                if instance_v == 0:
                    print(f"Attention vous ne pouvez plus infliger de degats a un membre que vous avez pulverisé !")
                    print("Vous obstiner sur ce membre ne menera a rien ! ")
            perso1.attaquer(perso2)
            if perso2.pv <= (perso2.pv / 4):
                if perso2.lvl <= 5 and heal_mark == False:
                    perso2.pv += 200
                    heal_mark = True
                else:
                    perso2.attaquer(perso1)
            else:
                perso2.attaquer(perso1)
        elif reponse == 2:
            perso1.use_potion()
            perso2.attaquer(perso1)
        elif reponse == 3:
            print("Vous tentez de fuire ! Serez-vous assez rapide ?")
            if perso1.agilite > perso2.agilite:
                print("Vous avez réussi à fuir !")
                break
            else:
                print("Vous n'avez pas réussi à fuir !")
                perso2.attaquer(perso1)
        else:
            print("Vous n'avez pas choisi une action valide !")
    if perso1.pv > 0 and perso2.pv == 0:
        perso1.xp += 10000
        print("Vous avez gagné 10000 point d'xp !")
        if perso1.xp > perso1.xp_max:
            perso1.monter_niveau()
            surplu_xp = perso1.xp - perso1.xp_max
            perso1.xp = 0
            perso1.xp += surplu_xp
            print(f"Votre experience est de {perso1.xp}")
        else:
            print(f"Votre experience est de {perso1.xp}")
    print("Le combat est terminé !")



# Instances des armes basiques
epee = Arme("Épée", 1, 0, 100, 15, 5, 10)
sceptre = Arme("Sceptre", 1, 0, 100, 10, 5, 10) 
dague = Arme("Dague", 1, 0, 100, 8, 5, 10) 
marteau = Arme("Marteau", 1, 0, 100, 20, 5, 10)
arc = Arme("Arc", 1, 0, 100, 12, 5, 10)
katana = Arme("Katana", 1, 0, 100, 18, 5, 10)
nunchaku = Arme("Nunchaku", 1, 0, 100, 14, 5, 10)
lance = Arme("Lance", 1, 0, 100, 16, 5, 10)
hache = Arme("Hache", 1, 0, 100, 22, 5, 10) 
fouet = Arme("Fouet", 1, 0, 100, 11, 5, 10)
# Armes et Equipements légendaires
bouclier_mystique = Arme("Bouclier Mystique", 1, 0, 100, 18, 5, 10)
armure_celeste = Arme("Armure Céleste", 1, 0, 100, 28, 5, 10) 
casque_ombre = Arme("Casque de l'Ombre", 1, 0, 100, 7, 5, 10) 
#Epées
epee_dragon = Arme("Épée du Dragon", 1, 0, 100, 25, 5, 10) 
epee_phoenix = Arme("Épée du Phénix", 1, 0, 100, 27, 5, 10) 
epee_titan = Arme("Épée du Titan", 1, 0, 100, 30, 5, 10) 
epee_vortex = Arme("Épée du Vortex", 1, 0, 100, 29, 5, 10)
epee_gardien = Arme("Épée du Gardien", 1, 0, 100, 28, 5, 10) 
epee_etoile = Arme("Épée de l'Étoile", 1, 0, 100, 26, 5, 10)
epee_lune = Arme("Épée de la Lune", 1, 0, 100, 25, 5, 10) 
epee_solstice = Arme("Épée du Solstice", 1, 0, 100, 29, 5, 10) 
epee_cendre = Arme("Épée de la Cendre", 1, 0, 100, 27, 5, 10) 
epee_mer = Arme("Épée de la Mer", 1, 0, 100, 28, 5, 10)
#Marteaux
marteau_dragon = Arme("Marteau du Dragon", 1, 0, 100, 35, 5, 10) 
marteau_phoenix = Arme("Marteau du Phénix", 1, 0, 100, 37, 5, 10)
marteau_titan = Arme("Marteau du Titan", 1, 0, 100, 40, 5, 10)
marteau_vortex = Arme("Marteau du Vortex", 1, 0, 100, 39, 5, 10)
marteau_gardien = Arme("Marteau du Gardien", 1, 0, 100, 38, 5, 10)
marteau_etoile = Arme("Marteau de l'Étoile", 1, 0, 100, 36, 5, 10)
marteau_lune = Arme("Marteau de la Lune", 1, 0, 100, 35, 5, 10)
marteau_solstice = Arme("Marteau du Solstice", 1, 0, 100, 39, 5, 10) 
marteau_cendre = Arme("Marteau de la Cendre", 1, 0, 100, 37, 5, 10)
marteau_mer = Arme("Marteau de la Mer", 1, 0, 100, 38, 5, 10) 
#Haches
hache_dragon = Arme("Hache du Dragon", 1, 0, 100, 33, 5, 10)
hache_phoenix = Arme("Hache du Phénix", 1, 0, 100, 35, 5, 10) 
hache_titan = Arme("Hache du Titan", 1, 0, 100, 38, 5, 10) 
hache_vortex = Arme("Hache du Vortex", 1, 0, 100, 37, 5, 10) 
hache_gardien = Arme("Hache du Gardien", 1, 0, 100, 36, 5, 10) 
hache_etoile = Arme("Hache de l'Étoile", 1, 0, 100, 34, 5, 10) 
hache_lune = Arme("Hache de la Lune", 1, 0, 100, 33, 5, 10) 
hache_solstice = Arme("Hache du Solstice", 1, 0, 100, 37, 5, 10)
hache_cendre = Arme("Hache de la Cendre", 1, 0, 100, 35, 5, 10) 
hache_mer = Arme("Hache de la Mer", 1, 0, 100, 36, 5, 10) 
#Lances
lance_dragon = Arme("Lance du Dragon", 1, 0, 100, 28, 5, 10) 
lance_phoenix = Arme("Lance du Phénix", 1, 0, 100, 30, 5, 10)
lance_titan = Arme("Lance du Titan", 1, 0, 100, 33, 5, 10) 
lance_vortex = Arme("Lance du Vortex", 1, 0, 100, 32, 5, 10) 
lance_gardien = Arme("Lance du Gardien", 1, 0, 100, 31, 5, 10)
lance_etoile = Arme("Lance de l'Étoile", 1, 0, 100, 29, 5, 10)
lance_lune = Arme("Lance de la Lune", 1, 0, 100, 28, 5, 10) 
lance_solstice = Arme("Lance du Solstice", 1, 0, 100, 32, 5, 10)
lance_cendre = Arme("Lance de la Cendre", 1, 0, 100, 30, 5, 10) 
lance_mer = Arme("Lance de la Mer", 1, 0, 100, 31, 5, 10) 
#Dagues
dague_dragon = Arme("Dague du Dragon", 1, 0, 100, 18, 5, 10) 
dague_phoenix = Arme("Dague du Phénix", 1, 0, 100, 20, 5, 10) 
dague_titan = Arme("Dague du Titan", 1, 0, 100, 23, 5, 10) 
dague_vortex = Arme("Dague du Vortex", 1, 0, 100, 22, 5, 10) 
dague_gardien = Arme("Dague du Gardien", 1, 0, 100, 21, 5, 10) 
dague_etoile = Arme("Dague de l'Étoile", 1, 0, 100, 19, 5, 10)
dague_lune = Arme("Dague de la Lune", 1, 0, 100, 18, 5, 10)
dague_solstice = Arme("Dague du Solstice", 1, 0, 100, 22, 5, 10) 
dague_cendre = Arme("Dague de la Cendre", 1, 0, 100, 20, 5, 10) 
dague_mer = Arme("Dague de la Mer", 1, 0, 100, 21, 5, 10)
#Boucliers
bouclier_dragon = Arme("Bouclier du Dragon", 1, 0, 100, 10, 5, 10)
bouclier_phoenix = Arme("Bouclier du Phénix", 1, 0, 100, 12, 5, 10)
bouclier_titan = Arme("Bouclier du Titan", 1, 0, 100, 15, 5, 10) 
bouclier_vortex = Arme("Bouclier du Vortex", 1, 0, 100, 14, 5, 10) 
bouclier_gardien = Arme("Bouclier du Gardien", 1, 0, 100, 13, 5, 10)
bouclier_etoile = Arme("Bouclier de l'Étoile", 1, 0, 100, 11, 5, 10)
bouclier_lune = Arme("Bouclier de la Lune", 1, 0, 100, 10, 5, 10) 
bouclier_solstice = Arme("Bouclier du Solstice", 1, 0, 100, 14, 5, 10) 
bouclier_cendre = Arme("Bouclier de la Cendre", 1, 0, 100, 12, 5, 10)
bouclier_mer = Arme("Bouclier de la Mer", 1, 0, 100, 13, 5, 10)
# Armures 
armure_dragon = Arme("Armure du Dragon", 1, 0, 100, 20, 5, 10) 
armure_phoenix = Arme("Armure du Phénix", 1, 0, 100, 22, 5, 10) 
armure_titan = Arme("Armure du Titan", 1, 0, 100, 25, 5, 10) 
armure_vortex = Arme("Armure du Vortex", 1, 0, 100, 24, 5, 10) 
armure_gardien = Arme("Armure du Gardien", 1, 0, 100, 23, 5, 10) 
armure_etoile = Arme("Armure de l'Étoile", 1, 0, 100, 21, 5, 10) 
armure_lune = Arme("Armure de la Lune", 1, 0, 100, 20, 5, 10) 
armure_solstice = Arme("Armure du Solstice", 1, 0, 100, 24, 5, 10) 
armure_cendre = Arme("Armure de la Cendre", 1, 0, 100, 22, 5, 10) 
armure_mer = Arme("Armure de la Mer", 1, 0, 100, 23, 5, 10) 
# Casques 
casque_dragon = Arme("Casque du Dragon", 1, 0, 100, 5, 5, 10)
casque_phoenix = Arme("Casque du Phénix", 1, 0, 100, 6, 5, 10)
casque_titan = Arme("Casque du Titan", 1, 0, 100, 7, 5, 10)
casque_vortex = Arme("Casque du Vortex", 1, 0, 100, 6, 5, 10) 
casque_gardien = Arme("Casque du Gardien", 1, 0, 100, 6, 5, 10)
casque_etoile = Arme("Casque de l'Étoile", 1, 0, 100, 5, 5, 10)
casque_lune = Arme("Casque de la Lune", 1, 0, 100, 5, 5, 10) 
casque_solstice = Arme("Casque du Solstice", 1, 0, 100, 6, 5, 10)
casque_cendre = Arme("Casque de la Cendre", 1, 0, 100, 6, 5, 10)
casque_mer = Arme("Casque de la Mer", 1, 0, 100, 6, 5, 10) 
couronne_roi = Arme("Couronne du Roi des Rois sur Terre", 1, 0, 100, 8, 5, 10) 
# Jambières 
jambières_dragon = Arme("Jambières du Dragon", 1, 0, 100, 3, 5, 10) 
jambières_phoenix = Arme("Jambières du Phénix", 1, 0, 100, 4, 5, 10) 
jambières_titan = Arme("Jambières du Titan", 1, 0, 100, 4, 5, 10) 
jambières_vortex = Arme("Jambières du Vortex", 1, 0, 100, 4, 5, 10) 
jambières_gardien = Arme("Jambières du Gardien", 1, 0, 100, 4, 5, 10) 
jambières_etoile = Arme("Jambières de l'Étoile", 1, 0, 100, 3, 5, 10) 
jambières_lune = Arme("Jambières de la Lune", 1, 0, 100, 3, 5, 10) 
jambières_solstice = Arme("Jambières du Solstice", 1, 0, 100, 4, 5, 10) 
jambières_cendre = Arme("Jambières de la Cendre", 1, 0, 100, 4, 5, 10) 
jambières_mer = Arme("Jambières de la Mer", 1, 0, 100, 4, 5, 10)

# Affichage des instances
#print(epee)
#print(sceptre)
#print(dague)
#print(marteau)
#print(arc)
#print(katana)
#print(nunchaku)
#print(lance)
#print(hache)
#print(fouet)
#p Affichage d'exemples plus complet
#print(epee)
#print(sceptre)
#print(dague)
#print(marteau)
#print(arc)
#print(katana)
#print(nunchaku)
#print(lance)
#print(hache)
#print(fouet)
#print(bouclier_dragon)
#print(bouclier_phoenix)
#print(bouclier_titan)
#print(bouclier_vortex)
#print(bouclier_gardien)
#print(bouclier_etoile)
#print(bouclier_lune)
#print(bouclier_solstice)
#print(bouclier_cendre)
#print(bouclier_mer)
#print(armure_dragon)
#print(armure_phoenix)
#print(armure_titan)
#print(armure_vortex)
#print(armure_gardien)
#print(armure_etoile)
#print(armure_lune)
#print(armure_solstice)
#print(armure_cendre)
#print(armure_mer)
#print(casque_dragon)
#print(casque_phoenix)
#print(casque_titan)
#print(casque_vortex)
#print(casque_gardien)
#print(casque_etoile)
#print(casque_lune)
#print(casque_solstice)
#print(casque_cendre)
#print(casque_mer)
#print(couronne_roi)
#print(jambières_dragon)
#print(jambières_phoenix)
#print(jambières_titan)
#print(jambières_vortex)
#print(jambières_gardien)
#print(jambières_etoile)
#print(jambières_lune)
#print(jambières_solstice)
#print(jambières_cendre)
#print(jambières_mer)
#print(bouclier_mystique)
#print(armure_celeste)
#print(casque_ombre)


# Créez un personnage et assignez-lui l'inventaire
Bob = Personnage("Bob", 1, 1000, 20, 10, 0, 10, 10, sac, casque_dragon, armure_dragon, epee_dragon, bouclier_dragon, jambières_dragon, jambières_dragon, 1500, 3000)
#Bob3 = Personnage("Bob3", 1, 100, 10, 5, 10, 0 , 10)  #Attention, si vous oubliez d'ajouter un inventaire meme vide, vous obtiendrez une erreur #Erreur !
monstre = Ennemi("Cypher", 20, 100, 100, 100, 100, 100, 100, 25, 0, 35)


# Affichez l'inventaire de Bob
#Bob.affiche_inv()
#combat(Bob, monstre)
#Définir GameOver ()
#Definir main() La boucle générale 


#def Quete()#jeu des mains et de l'objet cachée
#def Quete2()#Entrainemet
#potiion defense 
class Pnj(Personnage):
    def __init__(self, nom, lvl, pv, force, defense, agilite, xp,b_obj_max, inventaire, tete, corps, brasG, brasD, jambeG, jambeD, pv_max, xp_max, role, genre):
        super().__init__(nom, lvl, pv, force, defense, agilite, xp,b_obj_max, inventaire, tete, corps, brasG, brasD, jambeG, jambeD, pv_max, xp_max)
        self.role = role
        self.genre = genre
    
    def se_presenter(self):
        if self.genre == "Feminin":
            print(f"Je m'appelle {self.nom} et je suis ton {self.role}")
        else:
            print(f"Je m'appel {self.nom} et je suis ton {self.role}")
        
Thessa = Pnj("Thessa", 50, 10000, 100, 100, 100, 10000, 30, sac, casque_phoenix, armure_phoenix, epee_phoenix, epee_phoenix, jambières_phoenix, jambières_phoenix, 100000, 2000, "Entraineur", "Feminin") 
#combat(Thessa, Bob)
Thessa.se_presenter()

#Element réél du jeu 

#nom, lvl, pv_tete, pv_corps, pv_brasG, pv_brasD, pv_jambeG, pv_jambeD, degat, defense, agilite)
Theo = Ennemi("Théo", 1, 10, 10, 10, 10, 10, 10, 10, 0, 5)
Liana = Ennemi("Liana", 3, 15, 15, 15, 15, 15, 15, 15, 10, 10)
Diego = Ennemi("Diego", 5, 20, 20, 20, 20, 20, 20, 20, 12, 15)
Xavier = Ennemi("Xavier", 7, 25, 25, 25, 25, 25, 25, 25, 14, 20)
Boss = Ennemi("ZK", 10, 100, 100, 100, 100, 100, 100, 35, 20, 40)

print(Theo.__str__())
print(Liana.__str__())
print(Diego.__str__())
print(Xavier.__str__())
print(Boss.__str__())




def Entrainement3(perso1, perso2):
    perso2.se_presenter()
    print("A mon niveau, je suis capable d'anticiper tes mouvements ")
    print("Veux-tu t'entraîner avec moi dans dans le but de faire de toi un autre Homme ?")
    reponse = input().lower().strip()
    
    if reponse == "oui":
        points = 0
        actions = ["attaque rapide", "défense", "attaque puissante"]
        
        while points < 1:
            print("\nChoisis ton action (attaque rapide, défense, attaque puissante):")
            action_perso1 = input().lower().strip()
            action_perso2 = random.choice(actions)
            
            print(f"{perso2.nom} a choisi : {action_perso2}")
            
            if (action_perso1 == "attaque rapide" and action_perso2 == "attaque puissante") or \
               (action_perso1 == "défense" and action_perso2 == "attaque rapide") or \
               (action_perso1 == "attaque puissante" and action_perso2 == "défense"):
                print("Bravo ! Vous avez gagné ce tour.")
                points += 1
            else:
                print("Dommage, essayez encore.")
        
        print("Entraînement terminé !")
        if points == 1:
            perso1.xp += 1000000000000000000000
            xp_loop = True
            while xp_loop:
                 if perso1.xp > perso1.xp_max:
                    perso1.monter_niveau()
                    surplus_xp = perso1.xp - perso1.xp_max
                    perso1.xp = 0
                    perso1.xp += surplus_xp
                 else:
                    print(f"Votre expérience est de {perso1.xp}")
                    xp_loop = False
               
            xpprint = perso1.xp
            print(f"Votre expérience est de {xpprint}")
            print("Tu est un autre Homme ! !")
            print("Va valereux Héro")
Entrainement3(Bob, Thessa)

#Seul les class personnage et pnj
def Entrainement(perso1, perso2):
    perso2.se_presenter()
    print("Veux tu t'entrainer avec moi ?")
    reponse = input().lower()
    if reponse == "oui":
        point = 0
        while point < 1:
            list = ["tete", "corps", "bras_G", "bras_D", "jambe_G", "jambe_D"]
            choix = random.choice(list)
            choix2 = random.choice(list)
            if choix == "tete" or choix == "jambe_G" or choix == "jambe_D":
                print(f"Vise la {choix} !")
                if choix2  == "tete" or choix2 == "jambe_G" or choix2 == "jambe_D":
                    print(f"Avec ta {choix2} !")
                else:
                    print(f"Avec ton {choix2}")
            else:
                print(f"Vise le {choix} !")
                if choix2  == "tete" or choix2 == "jambe_G" or choix2 == "jambe_D":
                    print(f"Avec ta {choix2} !")
                else:
                    print(f"Avec ton {choix2}")
            print(perso2.all_body.keys()) 
            print("Quelle partie du corps souhaitez-vous cibler ?") 
            partie = input()
            if partie in perso2.all_body.keys(): 
                print(perso1.all_body.keys()) 
                print("Avec quelle partie de votre corps souhaitez-vous l'attaquer ?") 
                reponse = input()
                if reponse in perso1.all_body.keys(): 
                    print("Bravo")
                    point += 1
                else:
                    print("Tu n'as pas reussi !")
            else:
                print("Tu n'as pas assez de dexterité !")
        print("Entrainement terminé !")
        if point == 1:
            perso1.xp += 1000000000000
            print("Vous avez gagné 10000... point d'xp !")
            xp_loop = True
            while xp_loop:
                if perso1.xp > perso1.xp_max:
                   perso1.monter_niveau()
                   surplus_xp = perso1.xp - perso1.xp_max
                   perso1.xp = 0
                   perso1.xp += surplus_xp
                   print(f"Votre expérience est de {perso1.xp}")
                else:
                   print(f"Votre expérience est de {perso1.xp}")
                   xp_loop = False
            
            
Entrainement(Bob, Thessa)



def Entrainement2(perso1, perso2):
    perso2.se_presenter()
    print("Veux-tu t'entraîner avec moi ?")
    reponse = input().lower().strip()
    
    if reponse == "oui":
        point = 0
        while point < 1:
            print("Prépare-toi pour le prochain défi !")
            puzzle_type = random.choice(["math", "trivia", "riddle"])
            
            if puzzle_type == "math":
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)
                correct_answer = num1 + num2
                print(f"Résous ce problème mathématique : {num1} + {num2} = ?")
                answer = int(input())
                
                if answer == correct_answer:
                    print("Bravo ! Bonne réponse.")
                    point += 1
                else:
                    print("Dommage, mauvaise réponse.")
            
            elif puzzle_type == "trivia":
                trivia_questions = {
                    "Quelle est la capitale de la France ?": "paris",
                    "Qui a écrit 'Les Misérables' ?": "victor hugo",
                    "En quelle année a eu lieu la Révolution française ?": "1789"
                }
                question, correct_answer = random.choice(list(trivia_questions.items()))
                print(f"Question de culture générale : {question}")
                answer = input().lower().strip()
                
                if answer == correct_answer:
                    print("Bien joué ! Bonne réponse.")
                    point += 1
                else:
                    print("Mauvaise réponse.")
            
            elif puzzle_type == "riddle":
                riddles = {
                    "Je suis petit en hiver et grand en été. Qui suis-je ?": "jour",
                    "Plus je sèche, plus je suis mouillé. Qui suis-je ?": "serviette",
                    "Je suis une maison sans portes ni fenêtres, je contiens de l'or et de l'argent. Qui suis-je ?": "oeuf"
                }
                riddle, correct_answer = random.choice(list(riddles.items()))
                print(f"Devine l'énigme : {riddle}")
                answer = input().lower().strip()
                
                if answer == correct_answer:
                    print("Exactement ! Bonne réponse.")
                    point += 1
                else:
                    print("Réponse incorrecte.")
            
            print(f"Points actuels : {point}")
        
        print("Entraînement terminé !")
        if point == 3:
            perso1.xp += 10000
            print("Vous avez gagné 10000 points d'XP !")
            xp_loop = True
            while xp_loop:
                if perso1.xp > perso1.xp_max:
                   perso1.monter_niveau()
                   surplus_xp = perso1.xp - perso1.xp_max
                   perso1.xp = 0
                   perso1.xp += surplus_xp
                   print(f"Votre expérience est de {perso1.xp}")
                else:
                   print(f"Votre expérience est de {perso1.xp}")
                   xp_loop = False

# Assuming perso1 and perso2 are instances of a class with the required methods and attributes
Entrainement2(Bob, Thessa)
print("Tu es prêt à découvrir le monde et sauver Symphonie du châteaux de l'infini. ")
            