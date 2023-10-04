
import bs4
from selenium import webdriver

URL = "https://www.keycollectorcomics.com/series/spawn,6696/"

ff = webdriver.Firefox()
ff.get(URL)
doc = bs4.BeautifulSoup(ff.page_source, 'html.parser')
ff.quit()

results = doc.find_all(class_="row")

editions = list()

for result in results:

    if "1st appearance of" in result.text:
        title = result.find("h2", class_="issue-title")

        if isinstance(title,bs4.element.Tag):
            if title.text not in editions:
                editions.append(title.text)

for x in editions:
    print(x.split("#")[1])