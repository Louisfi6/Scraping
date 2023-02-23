import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

from Lawyer import Lawyer

baseUrl = "https://www.barreaudenice.com"
uri = "/annuaire/avocats/?fwp_paged="
nbPg = 107

#fonction pour parser le site
def swoup(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
    else:
        print("ERROR: Failed Connect on :" + str(url))
        return False


#fonction qui va retourner toutes les pages qui nous interessent en incrémentant de 1 pour l'id des pages
def getLinks(url, nbPg):
    urls = []
    for page in range(nbPg):
        urls.append(url + str(page))
    return urls

#fonctione pour nettoyer nos éléments du htlm
def getCleanText(text):
    return re.sub(' +', ' ', text.get_text(strip=True))

#fonction qui nous retourne toutes les informations dont nous avons besoin - apres le clean - gestion des erreurs
def getLawyer(card):
    try:
        name = getCleanText(card.find("h3", class_="nom-prenom"))
        swornDate = getCleanText(card.find("span", class_="date"))
        address = getCleanText(card.find("span", class_="adresse"))
        phoneNumber = getCleanText(card.find("span", class_="telephone")).replace("T . ", "")
        cases = getCleanText(card.find("span", class_="num-case")).replace("N° de Case : ", "")
        email = getCleanText(card.find("span", class_="email")).replace("Email :", "")

        if name or address or (phoneNumber and email) is None:
            pass

        if swornDate is None:
            swornDate = ""

        if cases is None:
            cases = ""

        return Lawyer(name, phoneNumber, email, address, cases, swornDate)
    except AttributeError:
        return None

#fonction principale qui va placer les liens dans links puis qui va à partir de ces liens éxecuter la fonction
#getLawyer qui va placer les infos de chaque lien dans le tableau lawyers. Puis qui va créer un dataframe avec nos infos
#pour l'envoyer sur un csv
def main():
    links = getLinks(baseUrl + uri, nbPg + 1)
    lawyers = []
    for link in links:
        soup = swoup(link)
        cards = soup.findAll("div", class_="callout secondary annuaire-single")
        for card in cards:
            lawyers.append(getLawyer(card))
    lawyers = formatLawyers(lawyers)
    dataFrame = pd.DataFrame(lawyers)
    dataFrame.to_csv("Louis.csv")

#fonction qui verifie si nos éléments existent et qui rend plus lisible le code en sorti pour le mettre en csv
def formatLawyers(lawyersArray):
    lawyersData = []
    for lawyer in lawyersArray:
        if lawyer:
            lawyer_dict = {
                'Name': lawyer.getName(),
                'Address': lawyer.getAddress(),
                'Email': lawyer.getEmail(),
                'Phone': lawyer.getPhone(),
                'Cases': lawyer.getCases(),
                'Sworn Date': lawyer.getSwornDate(),
            }
            lawyersData.append(lawyer_dict)

    return lawyersData

main()
