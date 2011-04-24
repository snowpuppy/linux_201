#!/usr/bin/env python

"""
grab.py
  Downloads all of the files from a given github page.

Usage: grab.py https://github.com/snowpuppy/linux_201/tree/master/perl_examples ./output/
"""

#First, we import a bunch of things.
#Beautiful soup for screen parsing.
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from urllib import urlretrieve #this function will download things
import string, sys, os

#As before, this will check to be sure we have the right number of arguments.
if (len(sys.argv) != 3):
	print "Usage: " + sys.argv[0] + " <list_page> <directory>"
	exit(1)

#This is our main function. Notice it takes two parameters, and one of them has a default incase it's not given.
def main(url, output="./test/"):
	dlCount = 1 #We need some base vars
	exists = 0

	page = urlopen(url) #First, we open the given Github URL
	soup = BeautifulSoup(page) #Then we parse it with Beautiful Soup to make it easy to traverse.
	links = soup.findAll(attrs={'class':"js-slide-to"}) #We will find all of links with this class. This was found by scouring through the source (or the beautiful soup
		#version, if the source is too hard to read) and finding something that all of the links had in common, but other links did not.
	links.pop(0) #Finally, we remove the first link, which isn't something we need to download (it just goes up a folder).

	for link in links: #Here's our for loop construct again. For each item in a list of items.
		nextPage = str(link).encode('ascii', 'ignore').split("\"")[1] #Ok, so a lot is going on here. Step by step:
			#First, we make sure python reads the current link as a string with str(). Without this, it's a nonetype object because of
			#how the findAll method works.
			#Second, we encode it as ascii to make it easy to work with for the next part.
			#Third, we split the item on each double quote. So we'll get a list of 3 items in the anchor tag (<a href="url">item</a>).
			#Finally, the actual link is the second item. Since the list is 0-based, we want item 1.
		subPage = urlopen("https://github.com" + nextPage) #Here, we open the URL we just found above.
		subSoup = BeautifulSoup(subPage) #And we soupify it again.
		subLink = subSoup.findAll(attrs={'id':'raw-url'})[0] #Once again, we find the link we want, but we only want the first one, hence the [0].
		item = str(subLink).encode('ascii', 'ignore').split("\"")[1] #And we do the same bit as above (nextPage line) again.
		filename = item.split("/").pop() #Here, we get the items actual filename by splitting the above URL on /'s, and taking the last item (pop).
		for curItem in os.listdir(output):
			#In order to prevent downloading the same item multiple times, this for loop exists. It retrieves a list of items in the output directory,
			#and iterates through them to be sure that this item hasn't already been downloaded.
			if curItem == filename:
				exists = 1
				print "Skipping item " + curItem + ", as it already exists!"
		if exists == 0: #Assuming it hasn't been downloaded...
			urlretrieve("https://github.com" + item, output + "/" + filename) #This actually downloads the item to the output directory.
			print "Downloaded item " + str(dlCount) + ": " + item #And we will just output the item number and the item, so the user isn't lost...
		dlCount = dlCount + 1 #Increase our download counter...
		exists = 0 #reset this variable...
	print "*****Download complete!*****" #And when the for loop is done, let the user know.

def _usage(): #Just in case this program is called with inproper arguments, this function is called to correct the user.
	print "This is the github downloader.\nUSAGE:" + sys.argv[0] + "<github list URL> <download folder>"

if __name__ == "__main__": #This is our main function. When the program is called, this is what runs. (Well...kinda.)
	url = sys.argv[1] #Grab arguments from the user...
	output = sys.argv[2]
	if not url.lower().startswith("http"): #Check to be sure the url is correct, if not, maybe they put the arguments in backwards...
		output = sys.argv[1]
		url = sys.argv[2]
		if not url.lower().startwith("http"): #And if it's still screwed up, we correct them and GTFO.
			_usage()
			sys.exit(1)
	main(url, output) #If we get this far, then run the main function.
