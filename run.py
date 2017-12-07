from markov_python.cc_markov import MarkovChain
from fetch import *
from random import *

mc = MarkovChain()

def talk_barkley():
	print "Hey there, I'm Charles Barkley"
	rand_num = randint(0, 160)
	mylist_countries = fetch_countries()
	print "You know, I love %s" % mylist_countries[rand_num]
	chain = fetch_barkley()
	mc.add_string(chain)
	speech = mc.generate_text(40)
	g = ''
	for a in speech:
		g = g + ' ' + a 
	print "Also, I should say " + g + "."

talk_barkley()