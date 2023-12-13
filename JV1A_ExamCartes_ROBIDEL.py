class Mage:
    def __init__(self, name, deck):
        self.__nom = name
        self.__pv = 30
        self.__total_mana = 10
        self.__mana_actuel = 1
        self.__main = deck
        self.__defausse = []
        self.__zone_de_jeu = []
    
    def getPv(self):
        return self.__pv
    def getNom(self):
        return self.__nom
    def getMana(self):
        return self.__mana_actuel
    def getJeu(self):
        return self.__zone_de_jeu
    
    def jouer_carte(self, carte, typeCristal, typeSort):
        self.__mana_actuel -= carte.getMana()
        for i in range(len(typeCristal)):
            if carte == typeCristal[i]:
                self.__mana_actuel += carte.getValeur()
                return self.__mana_actuel
        for i in range(len(typeSort)):
            if carte == typeSort:
                return carte.getValeur()    
        self.__zone_de_jeu.append(carte)
        return self.__zone_de_jeu
    def recup_mana(self):
        self.__total_mana += 1
        self.__mana_actuel += self.__total_mana 
        return self.__mana_actuel
    def attaque(self, creature):
        for i in range(len(self.__zone_de_jeu)):
            if creature == self.__zone_de_jeu[i]:
                return creature.getAttaque()
        return "Cette creature ne peut pas attaquer"

class Carte:
    def __init__(self, coutMana, name, desc):
        self.__cout_mana = coutMana
        self.__nom = name
        self.__description = desc
    def getNom(self):
        return self.__nom
    def getDesc(self):
        return self.__description
    def getMana(self):
        return self.__cout_mana

class Cristal(Carte):
    def __init__(self, coutMana, name, desc, value):
        super().__init__(coutMana, name, desc)
        self.__valeur = value
    def getValeur(self):
        return self.__valeur


class Creature(Carte):
    def __init__(self, coutMana, name, desc, hp, atk):
        super().__init__(coutMana, name, desc)
        self.__pv = hp
        self.__pts_atk = atk
  
    def getPv(self):
        return self.__pv
    
    def getAttaque(self):
        return self.__pts_atk
    
    def deplacerDefausse(self):
        if self.__pv <= 0:
            return True
        return False

class Blast(Carte):
    def __init__(self, coutMana, name, desc, value):
        super().__init__(coutMana, name, desc)
        self.__valeur = value

    def getValeur(self):
        return self.__valeur


cartesCristal = [Cristal(0,"Souffme des dieux", "Vous donne 1 de mana en plus pendant ce tour", 1), Cristal(0,"Prière des dieux", "Vous donne 2 de mana en plus pendant ce tour", 2), Cristal(0,"Sang des dieux", "Vous donne 3 de mana en plus pendant ce tour", 3)]
cartesSort = [Blast(2, "Profanation des dieux", "inlige 3 de dégat a votre cible", 3), Blast(3, "Foudre des dieux", "inlige 4 de dégat a votre cible", 4), Blast(5, "Colère des dieux", "inlige 6 de dégat a votre cible", 6)]
cartesCreature = [Creature(1, "Âme Errante", "faible creature de ce monde, possède 2 pv et 1 pt d'attaque", 2, 1), Creature(3, "Minotaure", "mi-homme, mi-taureau, il possède 5pv et 2pts d'attaque", 5, 2), Creature(6, "Kratos", "fils de Zeus et nouveau dieu de la guerre, il est la creature la plus puissante après les dieux. Il possède 8pv et 5pts d'attaque", 8, 5)]
cartemage1 = [cartesCristal[1], cartesSort(0), cartesCreature(2)]
cartemage2 = [cartesCristal[2], cartesSort(1), cartesCreature(0)]
mage1 = Mage("Dumbledore", cartemage1)
mage2 = Mage("Gandalf", cartemage2)

def victoire(mage1:Mage, mage2:Mage):
    if mage1.getPv() or mage2.getPv():
        return True
    return False

while not victoire():
    mage1.jouer_carte()
    mage2.jouer_carte()

