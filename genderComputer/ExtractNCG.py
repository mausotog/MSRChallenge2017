#!/usr/bin/python
import os
from genderComputer import GenderComputer

from bs4 import BeautifulSoup
import urllib2
import time
import sys

startingUrl = sys.argv[1]
githubString="https://github.com/"
gc = GenderComputer(os.path.abspath('./nameLists'))

def main():
  soup = openPage(startingUrl)
  extractRepos(soup)
  #print(nextUrl)
  #print(soup.prettify())

def extractRepos(soup):
  userName = soup.find("a", class_="user-mention")
  output = "" #fullName, location, gender
  fullName=""
  #print(repoListElement)  
  #if it doesnt have a user name
  if not userName:
    fullNameStruc=soup.find("span", class_="user-mention")
    #if it doesnt have the name
    if not fullNameStruc:
      #we cannot determine country nor gender
      output+="?,?,?"
    #if it doesnt have user name but does have name
    else:
      fullName=fullNameStruc.string
      cleanCountry="?"
      output+=fullName+","+cleanCountry
  #if it does have a user name
  else:
    developersUsername = userName.string
    developersUrl = githubString+developersUsername
    developerSoup  = openPage(developersUrl)
    fullNameStruc = developerSoup.find("span", itemprop="name")
    fullName = fullNameStruc.string
    output+=fullName
    #Uncleaned Country
    loc = developerSoup.find_all(itemprop="homeLocation")
    cleanCountry=""
    #Didnt find a country
    if not loc: #If there is no location
      cleanedCountry="?"
      output+=","+cleanedCountry
    #Found a country
    else:
      uncleanedCountry=loc[0].contents[1].strip()
      cleanCountry=cleanCountryName(uncleanedCountry)
     # print("FullName:"+fullName+" Country:"+cleanCountry)
      output+=",\""+cleanCountry+"\""
  gender=gc.resolveGender(unicode(fullName), unicode(cleanCountry))
  if not gender:
    output+=",?"
  else:
    output+=","+gender
  print(output.encode('utf-8').strip())

#DO YOUR MAGIC HERE ZACK
def cleanCountryName(uncleanedCountry):
  cleanCountry = uncleanedCountry  
  return cleanCountry

def openPage(urlString):
  htmlDoc = resolve_redirects(urlString)
  soup = BeautifulSoup(htmlDoc, "html5lib")
  return soup

def resolve_redirects(url):
  try:
    return urllib2.urlopen(url)
  except urllib2.HTTPError as e:
    if e.code == 429:
      time.sleep(5)
      return resolve_redirects(url)
    else:
      print("?")
    raise

if __name__ == "__main__":
  main()
