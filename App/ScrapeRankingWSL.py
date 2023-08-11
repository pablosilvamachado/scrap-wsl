import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

ranking = requests.get('https://www.worldsurfleague.com/athletes/tour/mct?year=2023', headers=headers)

Heats = requests.get('https://www.worldsurfleague.com/events/2023/ct/75/shiseido-tahiti-pro/results', headers=headers)


rankingsoup = BeautifulSoup(ranking.text, 'html.parser')
quotesranking = []
quote_elementsranking = rankingsoup.find_all('tbody')

Heatssoup = BeautifulSoup(Heats.text, 'html.parser')
quotesHeats = []
quote_elementsHeats = Heatssoup.find_all('div', class_='post-event-watch-heat-grid__heat')

todosTRs = rankingsoup.find_all('tr')
for TRs in todosTRs:
    texto = TRs.text.replace("\n","")
    quotesranking.append(texto)

for quote_element in quote_elementsHeats:
    texto = quote_element.text
    quotesHeats.append(texto)

print(quotesranking)
print(quotesHeats)