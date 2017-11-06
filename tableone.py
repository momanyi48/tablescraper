import urllib
import urllib.request
import os
from bs4 import BeautifulSoup

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

financialdata=financialdatasaved=""
soup = make_soup("https://municipalities.co.za/metropolitans/view/8/Mangaung-Metropolitan-Municipality")
for table in soup.findAll('table', {"class": "financial"}):
    # rows = list()
    # for row in table.findAll("tr"):
    #     print(row.text)
    for record in table.findAll('tr'):
        financialdata = ""
        for data in record.findAll('td'):
            financialdata=financialdata+","+data.text
        financialdatasaved = financialdatasaved + "\n" + financialdata[1:]
header="All values: R'000,2016/17,2015/16,2014/15,2013/14"+"\n"
file= open(os.path.expanduser('financial-Mangaung-Metropolitan-Municipality.csv'),'wb')
file.write(bytes(header, encoding="ascii", errors="ignore"))
file.write(bytes(financialdatasaved, encoding="ascii", errors="ignore"))