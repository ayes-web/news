import requests, bs4

sites = [
['https://news.ycombinator.com/rss','https://techcrunch.com/','https://sidebar.io/feed.xml'], 
['Hacker news', 'TechCrunch', 'Sidebar']
]

i = 1
t = 0
while t == 0:
	try: 
		for x in sites[1]:
  			print('Site '+ str(i) + ': ' + x)
  			i += 1
		siteNumber = int(input('Choose site: ')) - 1
		print('Site: ' + sites[0][siteNumber])	
		res = requests.get(sites[0][siteNumber])
		res.raise_for_status()
		t += 1
	except:
		i = 1
		print(' ')
		print('Not a valid site!')
		print(' ')

i = 0

# Hacker news
if siteNumber == 0:

	soup = bs4.BeautifulSoup(res.text, 'xml')

	title = soup.find_all('title')
	link = soup.find_all('link')
	commentsLink = soup.find_all('comments')

	while i < len(title):
		try: 
			print(str(i) + '. '+ title[i].text.strip())
			print(link[i].text.strip())
			print('Comments: '+commentsLink[i].text.strip())
		except:
  			print("Couldn't fetch content")
		print(' ')
		i += 1

# TechCrunch
elif siteNumber == 1:
	soup = bs4.BeautifulSoup(res.text, 'html.parser')

	title = soup.find_all(class_='post-block__title__link')
	#link = soup.find_all()

	while i < len(title):
		print(title[i].text.strip())
		print(' ')
		i += 1

# Sidebar.io
elif siteNumber == 2:
	soup = bs4.BeautifulSoup(res.text, 'xml')

	title = soup.find_all('title')
	description = soup.find_all('description')
	link = soup.find_all('link')

	while i < len(title):
		try: 
			print(str(i) + '. '+ title[i].text.strip())
			print(description[i].text.strip())
			print(link[i].text.strip())
		except:
  			print("Couldn't fetch content")
		print(' ')
		i += 1