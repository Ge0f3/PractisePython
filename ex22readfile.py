import urllib.request
from bs4 import BeautifulSoup
def connect(url):
	html_content =urllib.request.urlopen(url)
	html_content=BeautifulSoup(html_content,"html.parser")
	return html_content

def insert2Dic(html_content):
	names=dict()
	html_content = str(html_content).split()
	for content in html_content:
		names[content]=names.get(content,0)+1
		# count=names.get(content,0)
		# if count < 0:
		# 	names[content]=1
		# else:
		# 	names[content] = count +1

	for key,value in names.items():
		print("The key is {} and the value is {}".format(key,value))
		

def main():
	url=str(input("Enter the url: "))
	html_content=connect(url)
	insert2Dic(html_content)

if __name__ == '__main__':
	main()