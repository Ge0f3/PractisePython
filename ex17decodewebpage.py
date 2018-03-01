import urllib.request
from bs4 import BeautifulSoup
def getaccess(url):
	html_content=urllib.request.urlopen(url)
	return html_content
def retrv_article(parsed_data):
	articles=parsed_data.find_all(class_="story-heading")
	article_title=list()
	for article in articles:
		title=article.find('a')
		if title is None:
			continue
		else:
			title=title.text.replace("\n"," ").strip()
			
			article_title.append(title)
	return article_title
def main():
	url=input("Enter the url you wanted to scrape : ")
	html_content=getaccess(url)
	parsed_data=BeautifulSoup(html_content,"html.parser")
	article_title = retrv_article(parsed_data)
	print('The html content after Beautify \n  ')
	count=1
	for title in article_title:
		print("Title {} is {} \n".format(count,title))
		count = count + 1 
if __name__ == '__main__':
	main()

	