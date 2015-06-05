
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib
matplotlib.style.use('ggplot')

cols = ["date", "numbers", "moneyball"]
firstreadin = pd.read_csv("MegaMillions1.tsv", sep = "\t", skiprows=1, names = cols)
firstreadin.columns = ['date','numbers','megaball']

#firstreadin.date = firstreadin.date.apply(lambda d: datetime.datetime.strptime(d, "%A, %B %d, %Y"))
firstreadin.date = pd.to_datetime(firstreadin.date, "%A, %B %d, %Y")

firsttime = datetime.datetime.strptime('1/13/99', '%m/%d/%y')
secondtime = datetime.datetime.strptime('5/15/02', '%m/%d/%y')
thirdtime = datetime.datetime.strptime('6/22/05', '%m/%d/%y')
fourthtime = datetime.datetime.strptime('10/19/13', '%m/%d/%y')

firstperiod = firstreadin[firstreadin.date < firsttime].reset_index(drop=True)
#moneyball range was 1-25
secondperiod = firstreadin[np.logical_and(firstreadin.date >= firsttime, firstreadin.date < secondtime)].reset_index(drop=True)
#moneyball range was 1-36
thirdperiod = firstreadin[np.logical_and(firstreadin.date >= secondtime, firstreadin.date < thirdtime)].reset_index(drop=True)
#moneyball range was 1-52
fourthperiod = firstreadin[np.logical_and(firstreadin.date >= thirdtime, firstreadin.date < fourthtime)].reset_index(drop=True)
#moneyball range was 1-46
fifthperiod = firstreadin[firstreadin.date > fourthtime]
#moneyball range is 1-15

#print fifthperiod.megaball.value_counts().sort_index()


#plotting distribution

fig = plt.figure()
fig.suptitle('Distribution of MegaBall Draws', fontsize=20)

ax1 = plt.subplot2grid((3,4), (0,0), colspan=2) 
firstperiod.megaball.plot(kind='hist', bins = 25)
plt.xticks(range(0,26,5), range(0,26,5), rotation="horizontal")
plt.title('MegaBall Distrib \'96 - \'99')
plt.ylabel("# of draws", fontsize = 10)

textstr = 'Total Draws = {0}'.format(len(firstperiod))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
ax1.text(18, 15, textstr, fontsize=7.25,
        verticalalignment='top', color="blue", bbox=props)


ax2 = plt.subplot2grid((3,4), (0,2), colspan=2) 
secondperiod.megaball.plot(kind='hist', bins = 36)
ax2.set_xlim(0, 36)
plt.xticks(range(0,36,5), range(0,41,5), rotation="horizontal")
plt.title('MegaBall Distrib \'99 - \'02')
plt.ylabel("# of draws", fontsize = 10)

textstr = 'Total Draws = {0}'.format(len(secondperiod))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
ax2.text(26, 15, textstr, fontsize=7.25,
        verticalalignment='top', color="blue", bbox=props)



ax3 = plt.subplot2grid((3,4), (1,0), colspan=2) 
thirdperiod.megaball.plot(kind='hist', bins = 52)
ax3.set_xlim(0, 52)
plt.xticks(range(0,55,5), range(0,55,5), rotation="horizontal")
plt.title('MegaBall Distrib \'02 - \'05')
plt.ylabel("# of draws", fontsize = 10)

textstr = 'Total Draws = {0}'.format(len(thirdperiod))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
ax3.text(37.5, 13, textstr, fontsize=7.25,
        verticalalignment='top', color="blue", bbox=props)


ax4 = plt.subplot2grid((3,4), (1,2), colspan=2)
fourthperiod.megaball.plot(kind='hist', bins = 46)
ax4.set_xlim(0, 46)
plt.xticks(range(0,50,5), range(0,50,5),rotation="horizontal")
plt.title('MegaBall Distrib \'05 - \'13')
plt.ylabel("# of draws", fontsize = 10)

textstr = 'Total Draws = {0}'.format(len(fourthperiod))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
ax4.text(33, 28, textstr, fontsize=7.25,
        verticalalignment='top', color="blue", bbox=props)


ax5 = plt.subplot2grid((3,4), (2,1), colspan=2)
fifthperiod.megaball.plot(kind='hist', bins = 15)
plt.xticks(rotation="horizontal")
plt.title('MegaBall Distrib \'13 - ')
plt.ylabel("# of draws", fontsize = 10)

textstr = 'Total Draws = {0}'.format(len(fifthperiod))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
ax5.text(11.5, 16, textstr, fontsize=7.25,
        verticalalignment='top', color="blue", bbox=props)



plt.tight_layout(w_pad = 2, h_pad = 2)

plt.subplots_adjust(top = 0.85, wspace = 0.75, hspace = 0.5)

plt.savefig("megaball_Distribs.png")
plt.show()


