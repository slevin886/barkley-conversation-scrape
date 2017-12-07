from urllib2 import urlopen
from bs4 import BeautifulSoup

def fetch_barkley():
	my_url = 'https://www.cnbc.com/2016/07/21/cnbc-transcript-nba-hall-of-famer-charles-barkley-speaks-with-cnbcs-susan-li-on-power-lunch-today.html'
	uClient = urlopen(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = BeautifulSoup(page_html, "html.parser")
	containers = page_soup.find_all("div", {"class":"group-container"})
	something = str(containers[0])
	words = something.split("<span>")
	chain = " "
	for letter in words:
		if "BARKLEY" in letter and not "SULLIVAN" in letter:
			letter = letter.replace('BARKLEY', '').replace("<p>", '').replace('</span>', '').replace('</p>', '')
			chain += letter
	return chain

#Creates a list of all of the countries of the world and cleans it a bit
def fetch_countries():
	my_url2 = 'https://www.countries-ofthe-world.com/all-countries.html'
	uClient2 = urlopen(my_url2)
	page_html2 = uClient2.read()
	uClient2.close()
	page_soup2 = BeautifulSoup(page_html2, "html.parser")
	containers2 = page_soup2.find_all("div", {"class":"container list-container"})
	something2 = str(containers2[0])
	countries = something2.split("<li>")
	del countries[0]
	mylist_countries = map(lambda each:each.strip("</li>\n"), countries)
	return mylist_countries