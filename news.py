import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')

title = soup.find_all("a", class_="storylink")
link = [a['href'] for a in soup.find_all('a', class_="storylink", href=True) if a.text]
rank = soup.find_all("span", class_="rank")
g = len(title)
i = 0
while i < g:
  print(rank[i].text.strip() + ' ' + title[i].text.strip())
  print(link[i])
  print(' ')
  i += 1