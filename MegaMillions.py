#THIS WORKS BEST

from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

page_num = 1
total_pages = 73

with open("MegaMillions.tsv","w") as f:
    fieldnames = ['date', 'numbers', 'moneyball']
    writer = csv.writer(f, delimiter = '\t')
    writer.writerow(fieldnames)

    while page_num <= total_pages:
        page_num = str(page_num)
        soup = BeautifulSoup(urlopen('http://www.usamega.com/mega-millions-history.asp?p='+page_num).read())

        for row in soup('table',{'bgcolor':'white'})[0].findAll('tr'):

            tds = row('td')
            if tds[1].a is not None:
                date = tds[1].a.string.encode("utf-8")
                if tds[3].b is not None:
                    uglynumber = tds[3].b.string.split()
                    betternumber = [int(i) for i in uglynumber if (uglynumber.index(i))%2==0]
                    moneyball = tds[3].strong.string.encode("utf-8")

                    writer.writerow([date, betternumber, moneyball])
        page_num = int(page_num)
        page_num += 1

print 'We\'re done here.'

