from urllib2 import urlopen
from bs4 import BeautifulSoup

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
		
	
