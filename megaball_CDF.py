
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import statsmodels.api as sm
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

#plotting CMF

plt.suptitle('Cumulative Distribution Functions of MegaBall Draws', fontsize=20)

ax1 = plt.subplot2grid((3,4), (0,0), colspan=2) 
plt.title('MegaBall Distrib \'96 - \'99')
ecdf = sm.distributions.ECDF(firstperiod.megaball)
x = sorted(list(firstperiod.megaball.value_counts().index))
y = ecdf(x)
ax1.set_xlim(0, max(firstperiod.megaball.value_counts().index))
ax1.step(x,y)
ax1.plot(ax1.get_xlim(), ax1.get_ylim(), ls="--")

ax2 = plt.subplot2grid((3,4), (0,2), colspan=2) 
plt.title('MegaBall Distrib \'99 - \'02')
ecdf = sm.distributions.ECDF(secondperiod.megaball)
x = sorted(list(secondperiod.megaball.value_counts().index))
y = ecdf(x)
ax2.set_xlim(0, max(secondperiod.megaball.value_counts().index))
ax2.step(x,y)
ax2.plot(ax2.get_xlim(), ax2.get_ylim(), ls="--")

ax3 = plt.subplot2grid((3,4), (1,0), colspan=2) 
plt.title('MegaBall Distrib \'02 - \'05')
ecdf = sm.distributions.ECDF(thirdperiod.megaball)
x = sorted(list(thirdperiod.megaball.value_counts().index))
y = ecdf(x)
ax3.set_xlim(0, max(thirdperiod.megaball.value_counts().index))
ax3.step(x,y)
ax3.plot(ax3.get_xlim(), ax3.get_ylim(), ls="--")

ax4 = plt.subplot2grid((3,4), (1,2), colspan=2)
plt.title('MegaBall Distrib \'05 - \'13')
ecdf = sm.distributions.ECDF(fourthperiod.megaball)
x = sorted(list(fourthperiod.megaball.value_counts().index))
y = ecdf(x)
ax4.set_xlim(0, max(fourthperiod.megaball.value_counts().index))
ax4.step(x,y)
ax4.plot(ax4.get_xlim(), ax4.get_ylim(), ls="--")

ax5 = plt.subplot2grid((3,4), (2,1), colspan=2)
plt.title('MegaBall Distrib \'13 - ')
ecdf = sm.distributions.ECDF(fifthperiod.megaball)
x = sorted(list(fifthperiod.megaball.value_counts().index))
y = ecdf(x)
ax5.set_xlim(0, max(fifthperiod.megaball.value_counts().index))
ax5.step(x,y)
ax5.plot(ax5.get_xlim(), ax5.get_ylim(), ls="--")

plt.tight_layout()
plt.subplots_adjust(top=0.85, hspace = 0.75, wspace = 0.5)
plt.savefig("megaball_CDF.png")
plt.show()


# In[ ]:



