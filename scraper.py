import requests
from bs4 import BeautifulSoup

def get_citations_needed_count():
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Find all <a> elements with href="https://en.wikipedia.org/wiki/Wikipedia:Citation_needed"
    citation_links = soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")
    count = 0

    for link in citation_links:
            if link:
                count+=1
    return count   





def get_citations_needed_report():
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find all <p> elements with <a> tags containing the text "citation needed"
    paragraphs = soup.find_all('p')
    paragraphs_with_citations_needed = []

    for p in paragraphs:
        if p.find('a', string='citation needed'):
            paragraphs_with_citations_needed.append(p)

    # Find the nearest titles of the paragraphs with citations needed
    titles = []
    for p in paragraphs_with_citations_needed:
        title = p.find_previous('span', class_='mw-headline')
        if title:
            titles.append(title.text.strip())

    return titles

print("The number of citation needed is :  " , get_citations_needed_count())
print("The topics that needed citation :" )
t = get_citations_needed_report()
for element in t : 
     print(element)










