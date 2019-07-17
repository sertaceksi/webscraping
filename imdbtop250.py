import requests
from bs4 import BeautifulSoup

imdbUrl = "https://www.imdb.com/chart/top"

r = requests.get(imdbUrl)
soup = BeautifulSoup(r.content, "html.parser")

table = soup.find("table", {"data-caller-name": "chart-top250movie"})

t_body = table.find('tbody')

rows = t_body.find_all('tr')
for row in rows[:]:
    title = row.find_all("td", {"class": "titleColumn"})[0].text.replace('\n','').replace('      ','')
    rating = row.find("td", {"class":"ratingColumn imdbRating"}).text.replace('\n','')
    print(title,rating)


