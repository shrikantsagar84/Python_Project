import urllib.request
from bs4 import BeautifulSoup
import csv

# url address
url_address = 'https://www.babynamesdirect.com/blender/indian/girl/rahul-manisha-d'

#opening and reading url 
url_open = urllib.request.urlopen(url_address)
snippet = url_open.read()
url_open.close()

# parsing html webpage with BeautifulSoup module
soup = BeautifulSoup(snippet, 'html.parser')

#  creating csv file with headers
filename = "baby_names.csv"
file = open(filename, "w")
headers = "Name, Gender/n"
file.write(headers)

# scraping web contents and write to csv file
for sp in soup.findAll("u", attrs={"class":"m"}):
    sp1 = sp.contents[0]
    print(sp1)
for sp in soup.findAll("u", attrs={"class":"f"}):
    sp2 = sp.contents[0]
    print(sp2)
    file.write(sp1 + "," +sp2)
file.close()

    
    


