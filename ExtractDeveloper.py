#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib2
import time
import sys

startingUrl = sys.argv[1]
githubString="https://github.com/"

def main():
  #numberOfReposToExtract=int(sys.argv[2]) #This only works in increments of ten
  #numberOfRepoPagesToExtract=numberOfReposToExtract/10
  soup = openPage(startingUrl)
  #for x in range(numberOfRepoPagesToExtract):
  extractRepos(soup)
  #nextUrl = getNextUrl(soup)
  #soup = openPage(nextUrl)
    
  
  #print(nextUrl)
  #print(soup.prettify())

def extractRepos(soup):
  repoListElement = soup.find("a", class_="user-mention")
  output = ""
  #print(repoListElement)
  
  if not repoListElement:
    output+="UnauthenticatedAuthor,UnauthenticatedAuthor,UnauthenticatedAuthor,UnauthenticatedAuthor,\"No Location Data\",UnauthenticatedAuthor"
  else:
    developersUsername = repoListElement.string
    
	#print(developersUsername)
#  for item in repoItems:
#    time.sleep(1)
    developersUrl = githubString+developersUsername
#  print "developersUrl: %s" % developersUrl
    developerSoup  = openPage(developersUrl)
#  lookForRepo="href=\"/"+developersUsername+"?tab=repositories\""
#  print lookForRepo
    tabs = developerSoup.find_all(class_="underline-nav-item")
  #print tabs.descendants
    
    for link in tabs :
#   print(link.contents[0])
      if 'Repositories' in link.contents[0]:
        output+=","+link.contents[1].contents[0].replace(",", "").replace(".", "").replace("k", "000").strip()
      if 'Stars' in link.contents[0]:
        output+=","+link.contents[1].contents[0].replace(",", "").replace(".", "").replace("k", "000").strip()
      if 'Followers' in link.contents[0]:
        output+=","+link.contents[1].contents[0].replace(",", "").replace(".", "").replace("k", "000").strip()
      if 'Following' in link.contents[0]:
        output+=","+link.contents[1].contents[0].replace(",", "").replace(".", "").replace("k", "000").strip()
    loc = developerSoup.find_all(itemprop="homeLocation")
    if not loc: #If there is no location
      output+=",\"No Location Data\"".strip()
    else:
      output+=",\""+loc[0].contents[1].strip()+"\""
    for child in developerSoup.find_all("h2", class_="f4 text-normal mb-2"):
      if not child.string is None:
        output+=","+child.contents[0].string.strip().replace(",", "")[:-37]

  print(output.encode('utf-8').strip())
	  
#  print tabs
#    finalRepoLink = tabs["value"]
#    print finalRepoLink



def openPage(urlString):
  htmlDoc = resolve_redirects(urlString)
  soup = BeautifulSoup(htmlDoc, "html5lib")
  return soup
  
def resolve_redirects(url):
    try:
        return urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        if e.code == 429:
             time.sleep(5);
             return resolve_redirects(url)
        raise

#def getNextUrl(soup):
#  pageLinks = soup.find(class_="pagination")
#  currentPage = pageLinks.find(class_="current")
#  nextPageLink = currentPage.find_next_sibling("a")
#  nextPageUrl = githubString+unicode(nextPageLink["href"])
#  return nextPageUrl


if __name__ == "__main__":
  main()
