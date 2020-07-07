import requests, bs4

sites = [
['https://news.ycombinator.com/','https://techcrunch.com/','https://sidebar.io/'], 
['Hacker news', 'TechCrunch', 'Sidebar']
]
i = 1
for x in sites[1]:
  print('Site '+ str(i) + ': ' + x)
  i += 1
siteNumber = int(input('Choose site: '))
siteNumber -= 1
if siteNumber > len(sites[0]):
	print("That site doesn't exist!")
	quit()
print('Site: ' + sites[0][siteNumber])

res = requests.get(sites[0][siteNumber])
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(' ')

i = 0

# Hacker news
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

# TechCrunch
elif siteNumber == 1:
	title = soup.find_all(class_='post-block__title__link')
	#link = soup.find_all()
	g = len(title)
	while i < g:
		print(title[i].text.strip())
		print(' ')
		i += 1

# Sidebar.io
elif siteNumber == 2:
	title = soup.find_all(class_='post-link')
	description = soup.find_all(class_='post-body')
	link = [a['href'] for a in soup.find_all('a', class_='post-link', href=True) if a.text]
	g = len(title)
	while i < g:
		print(title[i].text.strip())
		print(description[i].text.strip())
		print(link[i])
		print(' ')
		i += 1