#!/usr/bin/python
import os
from genderComputer import GenderComputer
import sys
sys.path.append('../collectCountryInfo/countryNameManager')
sys.path.append('../collectCountryInfo/unicodeManager')
from countryGuesser import CountryGuesser

from bs4 import BeautifulSoup
import urllib2
import time
import sys

class DummyFile(object):
  def write(self, x): pass

githubString="https://github.com/"
gc = GenderComputer(os.path.abspath('./nameLists'))

def main():
  with open('../travisTorrent3ParamsNoRepeat.csv','r') as fin:
    with open('NCGDataSet.csv','w') as fout:
      cg = CountryGuesser()
      for line in fin:
        lineItems = line.strip().split(',')
        startingUrl = 'https://github.com/{0}/commit/{1}'.format(lineItems[0], lineItems[1])
        soup = openPage(startingUrl)
        extractRepos(soup, fout, cg)
  #print(nextUrl)
  #print(soup.prettify())

def extractRepos(soup, fout, cg):
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
      cleanCountry=cleanCountryName(uncleanedCountry, cg)
     # print("FullName:"+fullName+" Country:"+cleanCountry)
      output+=",\""+cleanCountry+"\""
  gender=gc.resolveGender(unicode(fullName), unicode(cleanCountry))
  if not gender:
    output+=",?"
  else:
    output+=","+gender
  #print(output.encode('utf-8').strip())
  result = output.encode('utf-8').strip()
  fout.write('{0}\n'.format(result))
  fout.flush()

addedDict = {'DTX': 'united states', '94110': 'united states', '60605': 'united states', 'Zug': 'switzerland', 'Chicagoland': 'united states', 'NYC': 'united states'}

#DO YOUR MAGIC HERE ZACK
def cleanCountryName(uncleanedCountry, cg):
  country = cg.guess(uncleanedCountry)
  if country[0] is None:
    if location in addedDict:
      country = [addedDict[location]]
    else:
      if 'DTX' in location:
        country = [addedDict['DTX']]
      else:
        country = ['?']
  return country[0]

def openPage(urlString):
  htmlDoc = resolve_redirects(urlString)
  soup = BeautifulSoup(htmlDoc, "html.parser")
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
