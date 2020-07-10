import requests, bs4

sites = [
['https://news.ycombinator.com/rss','https://www.theverge.com/rss/front-page/index.xml','https://sidebar.io/feed.xml','https://www.producthunt.com/feed'], 
['Hacker news', 'The verge', 'Sidebar','ProductHunt']
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
		print(' ')
		try: 
			print(str(i) + '. '+ title[i].text.strip())
			print(link[i].text.strip())
			print('Comments: '+commentsLink[i].text.strip())
		except:
  			print("Couldn't fetch content")
		i += 1

# The verge
elif siteNumber == 1:
	i = 1
	soup = bs4.BeautifulSoup(res.text, 'xml')

	title = soup.find_all('title')
	#description = soup.find_all('content')
	link = soup.find_all('id')

	while i < len(title):
		print(' ')
		try: 
			print(str(i) + '. '+ title[i].text.strip())
			#print(description[i].text.strip())
			print(link[i].text.strip())
		except:
  			print("Couldn't fetch content")
		i += 1

# Sidebar.io
elif siteNumber == 2:
	soup = bs4.BeautifulSoup(res.text, 'xml')

	title = soup.find_all('title')
	description = soup.find_all('description')
	link = soup.find_all('link')

	while i < len(title):
		print(' ')
		try: 
			print(str(i) + '. '+ title[i].text.strip())
			print(description[i].text.strip())
			print(link[i].text.strip())
		except:
  			print("Couldn't fetch content")
		i += 1
		
# ProductHunt
elif siteNumber == 3:
	soup = bs4.BeautifulSoup(res.text, 'xml')

	title = soup.find_all('title')
	link = soup.find_all('link')

	while i < len(title):
		print(' ')
		try: 
			print(str(i) + '. '+ title[i].text.strip())
			print(link[i].get('href'))
		except:
  			print("Couldn't fetch content")
		i += 1