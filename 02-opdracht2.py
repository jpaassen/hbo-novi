'''
Project onderdeel van opdracht 2 uit de module Software Security

Opdracht: 
Maak een webscraping utility. Web scraping (informatie van het internet afhalen) is
een bijzonder handige tool bij security engagements, van het maken van woordenlijsten
of het doorworstelen van veel data, je kan het altijd gebruiken. In deze opdracht
gaan we van de URL https://www.keycollectorcomics.com/series/
3
spawn,6696/ alle Spawn comics waar een “1st Appearence” in voor komt laten
zien.
Hieronder een basaal stappenplan:
• Selecteer een web scraping bibliotheek
• Haal de pagina op
• Selecteer een HTML scanning bibliotheek
• Vind alle issues die voldoen aan de criteria
• Print het volgnummer uit
'''

#Importeren van modules die gebruikt worden in het script
import bs4
from selenium import webdriver

#URL waarop de informatie te vinden is over de comics
URL = "https://www.keycollectorcomics.com/series/spawn,6696/"

#Gebruik maken van FireFox om de pagina juist/compleet geladen te krijgen
ff = webdriver.Firefox()
ff.get(URL)

#Beautiful Soup object aanmaken en laden met de informatie welke in firefox is opgevraagd
doc = bs4.BeautifulSoup(ff.page_source, 'html.parser')

#Firefox afsluiten
ff.quit()

#Resultaten filteren, op basis van page source bepaald dat de informatie in een <div> zit met de class "row"
results = doc.find_all(class_="row")

#List aanmaken waarin de comics opgenomen worden die voldoen aan de zoek criteria
editions = list()

#Door de rijen heen bladeren op zoek naar de opgegeven zoek string
for result in results:

    #Controleren of de zoek string in de rij zit
    if "1st appearance of" in result.text:

        #wanneer de zoek string voorkomt dan zoeken naar het html object waarin de titel staat
        title = result.find("h2", class_="issue-title")

        #Controleren of het gevonden element wel informatie gevat
        if isinstance(title,bs4.element.Tag):

            #Wanneer de titel nog niet opgenomen is in de lijst met editions dan toevoegen
            if title.text not in editions:
                editions.append(title.text)


#Door alle resultaten heen gaan en stuk voor stuk alleen de nummers tonen.
for x in editions:
    print(x.split("#")[1])