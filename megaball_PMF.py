
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

def pmfconverter(period):
    return period.megaball.value_counts().sort_index()/len(period.megaball)

def findav(period):
    return 1/float(len(period.megaball.value_counts()))

#plotting PMF
fig = plt.figure()
fig.suptitle('Probability Mass Function of MegaBall Draws', fontsize=20)

ax1 = plt.subplot2grid((3,4), (0,0), colspan=2) 
pmfconverter(firstperiod).plot(kind="bar")
plt.axhline(y=findav(firstperiod))
plt.xticks(range(0,26,5), range(0,26,5), rotation="horizontal")
plt.title('MegaBall Distrib \'96 - \'99')
plt.ylabel("Probability of draws", fontsize = 10)

textstr = 'Exp.Freq = {0:.2f}'.format(findav(firstperiod))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
ax1.text(17.5, 0.08, textstr, fontsize=7.25,
        verticalalignment='top', color="blue", bbox=props)


ax2 = plt.subplot2grid((3,4), (0,2), colspan=2) 
pmfconverter(secondperiod).plot(kind="bar")
plt.axhline(y=findav(secondperiod))
plt.xticks(range(0,36,5), range(0,41,5), rotation="horizontal")
plt.title('MegaBall Distrib \'99 - \'02')
plt.ylabel("Probability of draws", fontsize = 10)

textstr = 'Exp.Freq = {0:.3f}'.format(findav(secondperiod))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
ax2.text(24.25, 0.04, textstr, fontsize=7.25,
        verticalalignment='top', color="blue", bbox=props)


ax3 = plt.subplot2grid((3,4), (1,0), colspan=2) 
pmfconverter(thirdperiod).plot(kind="bar")
plt.axhline(y=findav(thirdperiod))
plt.xticks(range(0,55,5), range(0,55,5), rotation="horizontal")
plt.title('MegaBall Distrib \'02 - \'05')
plt.ylabel("Probability of draws", fontsize = 10)

textstr = 'Exp.Freq = {0:.3f}'.format(findav(thirdperiod))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
ax3.text(35, 0.04, textstr, fontsize=7.25,
        verticalalignment='top', color="blue", bbox=props)


ax4 = plt.subplot2grid((3,4), (1,2), colspan=2)
pmfconverter(fourthperiod).plot(kind="bar")
plt.axhline(y=findav(fourthperiod))
plt.xticks(range(0,50,5), range(0,50,5),rotation="horizontal")
plt.title('MegaBall Distrib \'05 - \'13')
plt.ylabel("Probability of draws", fontsize = 10)

textstr = 'Exp.Freq = {0:.3f}'.format(findav(fourthperiod))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
ax4.text(31, 0.0315, textstr, fontsize=7.25,
        verticalalignment='top', color="blue", bbox=props)


ax5 = plt.subplot2grid((3,4), (2,1), colspan=2)
pmfconverter(fifthperiod).plot(kind="bar")
plt.axhline(y=findav(fifthperiod))
plt.xticks(rotation="horizontal")
plt.title('MegaBall Distrib \'13 - ')
plt.ylabel("Probability of draws", fontsize = 10)

textstr = 'Exp.Freq = {0:.3f}'.format(findav(fifthperiod))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
ax5.text(9.75, 0.105, textstr, fontsize=7.25,
        verticalalignment='top', color="blue", bbox=props)


plt.tight_layout(w_pad = 2, h_pad = 2)

plt.subplots_adjust(top = 0.85, wspace = 0.75, hspace = 0.5)

plt.savefig("megaball_PMF.png")
plt.show()


