'''
Hieronder een basaal stappenplan:
• Selecteer een web scraping bibliotheek
    Beautiful Soup
• Haal de pagina op
    Requests
• Selecteer een HTML scanning bibliotheek
• Vind alle issues die voldoen aan de criteria
• Print het volgnummer uit

'''

import bs4
from selenium import webdriver


URL = "https://www.keycollectorcomics.com/series/spawn,6696/"
#r = requests.get(URL)
# print("request uitgevoerd")

ff = webdriver.Firefox()
ff.get(URL)


#with open("spawn-6696.html") as content:
doc = bs4.BeautifulSoup(ff.page_source, 'html.parser')
print("Soup gevuld")
ff.quit()
results = doc.find_all(class_="row")

editions = list()

for result in results:
    if "1st appearance of" in result.text:
#        print("Succes!")

        title = result.find("h2", class_="issue-title")

 #       print(type(title))
        if isinstance(title,bs4.element.Tag):
#            print(title.text)
            if title.text not in editions:
                editions.append(title.text)


#print(editions)
for x in editions:
    print(x.split("#")[1])