import urllib.request
from bs4 import BeautifulSoup

def request(url):
	html_Data=urllib.request.urlopen(url)
	paresed_data=BeautifulSoup(html_Data,"html.parser")
	return paresed_data

def getarticle(paresed_data):
	article=paresed_data.find(class_='content drop-cap')
	article = article.find_all('p')
	return article

def main():
	url=input("Enter the url: ")
	paresed_data=request(url)
	#print(paresed_data)
	#print(getarticle(paresed_data))
	articles = getarticle(paresed_data)
	print("The Article  \n\n")
	for article in articles:
		print("{} \n".format(article.text))

if __name__ == '__main__':
	main()