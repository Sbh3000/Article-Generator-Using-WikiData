# Code to extract the label from link and breaking the chane of directed links
from urllib.request import urlopen
from bs4 import BeautifulSoup

import pprint
import requests
# Defined a function to convert links to labels to put in text 
def ConverterFxn(input_Values):
  input_Values = input_Values.replace('entity','wiki')
  html = urlopen(input_Values)
  bsh = BeautifulSoup(html.read(), 'html.parser')
  x = bsh.h1
  x = str(x)
  # Converting link to usable form as extracted links are nested <Label type> and cant be used to web scrape
  Lidx = x.find('</span>')
  Iidx = x.find('wikibase-title-label') + 22
  New_string = ""
  for i in range(Iidx,Lidx):
    New_string = New_string + x[i]
  return(New_string)
# Note its just a function