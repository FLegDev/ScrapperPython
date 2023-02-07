import requests
from bs4 import BeautifulSoup

def get_all_pages():
    page_number = 1
    for i in range (104) :
        i = f"https://www.barreaudenice.com/annuaire/avocats/?fwp_paged={page_number}"
        page_number += 1
        urls.append(i)

        return urls

def parse_attorney():
    r = requests.get("https://www.barreaudenice.com/annuaire/avocats/?fwp_paged=1")
    soup = BeautifulSoup(r.content,"html.parser")
    print(soup)

#def scrape_title(url):
 #   r = requests.get(url)
 #   bs = BeautifulSoup(r.content, "html.parser")
  #  titre = bs.h1
   # return(titre)

#title = scrape_title("https://corak.fr/secteurs magasin/portiques")
#print(title)