import requests, bs4

sites = [
['https://news.ycombinator.com/','https://techcrunch.com/'], 
['Hacker news', 'TechCrunch']
]
i = 0
for x in sites[1]:
  print('Site '+ str(i) + ': ' + x)
  i += 1
siteNumber = int(input('Choose site: '))
if siteNumber > len(sites[0]):
	print("That site doesn't exist!")
	quit()
print(sites[0][siteNumber])

res = requests.get(sites[0][siteNumber])
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(' ')

i = 0

if siteNumber == 0:
	points = soup.find_all('', class_='score')
	commentLink = [a['href'] for a in soup.select('td.subtext > a:nth-child(6)', class_='subtext') if a.text]
	commentNumber = soup.select('td.subtext > a:nth-child(6)', class_='subtext')

	title = soup.find_all('a', class_='storylink')
	link = [a['href'] for a in soup.find_all('a', class_='storylink', href=True) if a.text]
	rank = soup.find_all('span', class_='rank')
	g = len(title)
	while i < g:
		print(rank[i].text.strip() + ' ' + title[i].text.strip())
		print(link[i])
		print(points[i].text.strip() + ' | '+ commentNumber[i].text.strip()+ ': https://news.ycombinator.com/' + commentLink[i])
		print(' ')
		i += 1
elif siteNumber == 1:
	title = soup.find_all('#tc-main-content > div:nth-child(1) > div > div.feature-island > div.mini-view > article:nth-child(1) > h3 > a')
	#link = soup.find_all()
	g = len(title)
	while i < g:
		print(title[i].text.strip())
		print(' ')
		i += 1
