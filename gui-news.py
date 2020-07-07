import requests, tkinter as tk, bs4, webbrowser

window = tk.Tk()

res = requests.get('https://news.ycombinator.com/')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

title = soup.find_all("a", class_="storylink")
link = [a['href'] for a in soup.find_all('a', class_="storylink", href=True) if a.text]
rank = soup.find_all("span", class_="rank")

g = len(title)
i = 0
def openArticle(num): 
	print(num)
	#webbrowser.open(link[num])

while i < g:
	article = tk.Label(text=rank[i].text.strip() + ' ' + title[i].text.strip())
	linkButton = tk.Button(text=link[i], command=lambda: openArticle(linkButton['text']))
	article.pack()
	linkButton.pack()
	i += 1
window.mainloop()