import random
import requests
from bs4 import BeautifulSoup
import csv



def displayErreur (msg):
    """
    Cette fonction affiche un msg d'erreur
    """
    print("Erreur : ", msg)


def findNb ():
    """
    Cette fonction est le fameux jeu pour trouver un nb entre 1 et 100 
    """
    nb = random.randint(1, 100)
    nbChoisi = 0
    cpt = 0

    while nb != nbChoisi:
        nbChoisi = int(input("choisi un nombre entre 1 et 100 :"))
        cpt += 1
        
        if nbChoisi > nb :
            print ("trop grand !")
        elif nbChoisi < nb:
            print ("trop petit")
        else:
            print ("trouvé en ", cpt, "coups !")


def extract (elements):
    res = []
    for elt in elements:
        res.append(elt.string)
    return res


def transform (elements):
    res = []
    cpt = 0

    for elt in elements:
        cpt += 1
        res.append("Elt " + str(cpt) + ", " + elt.string + "\n")
    return res


def load (nomFichier, elements):
    with open (nomFichier, 'w+') as fichier:
        fichier.writelines("idt, description\n")
        for elt in elements:
            fichier.writelines(elt)
            
            

def ETL():
    # Lien de lapage à scrapper
    url = "https://www.gov.uk/search/news-and-communications"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')   # parse le contenu du code html
    #print(soup)

    # EXTRACT
    # On extrait les balises qui nous interesse 
    source_liste = soup.find_all('p', class_ = "gem-c-document-list__item-description")

    # On les met dans une liste
    liste = extract(source_liste)

    # TRANSFORM
    # On les tranforme si besoin
    liste2 = transform(liste)

    # LOAD
    # On les charge dans un fichier
    load ("Documents/Projets/Tests en Python/news.csv", liste2)



ETL()


