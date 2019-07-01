"""
Acum vrem ca din toate website-urile VIZITATE sa extragem text-ul human readable (cel care poate fi citit si de pe site).
Dupa parsarea acelui text vrem sa obtinem toate liniile care contin ani (incercati sa fiti inventivi, nu trebuie sa fie un
rezultat perfect), sa le salvam si sa le printam la final.

HINT:
    Work smart, not hard, cititi documentatia de la BeautifulSoup si vedeti cum puteti obtine text-ul, cand il aveti
    folositi functiile pe string-uri pe care le stiti deja + regex!

Plecati de la codul inteles la exercitiul anterior!
"""


import requests
import re
from bs4 import BeautifulSoup

visited = []
searched_lines = []
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
        if link.get('href') not in visited:
            websites.append(link.get('href'))
            found_htmls += 1
            if found_htmls == N:
                break
