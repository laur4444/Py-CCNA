"""
Vream sa scrapam un site web pentru a obtine date, in cadrul acestui exercitiu incercam sa mergem pe un numar de
link-uri pe care le expune in html pentru a crawla toate datele. Mai jos aveti un exemplu de cum puteti face
acest lucru.

Ce probleme pot aparea cu URL-urile gasite?
Cum ati rezolva aceste probleme?
"""


import requests
import re
from bs4 import BeautifulSoup

visited = []
websites = ["http://soc.rosedu.org/2018/"]
N = 40
found_htmls = 1

while found_htmls < N:
    current_website = websites[0]
    visited.append(current_website)
    del websites[0]
    page = requests.get(current_website)
    html_page = page.content
    soup = BeautifulSoup(html_page, "html.parser")
    for link in soup.findAll('a', attrs={'href' : re.compile("^http://")}):
        url = link.get('href')
        if url not in visited:
            websites.append(link.get('href'))
            found_htmls += 1
            if found_htmls == N:
                break

print(websites)
print(visited)