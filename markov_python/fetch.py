import urllib2
from bs4 import BeautifulSoup

def fetch_song():
	url = raw_input("Enter or paste the song url from www.azlyrics.com: ")
	doc = urllib2.urlopen(url)
	soup = BeautifulSoup(doc, "html.parser")
	for text in soup.find_all("div", class_= None):
		raw_song = text.get_text()
	return raw_song