
# coding: utf-8

# In[48]:
import pandas as pd
import numpy as np
import datetime
from __future__ import division
from collections import OrderedDict

#the data input is in the form period.megaball (i.e. 'firstperiod.megaball')

class HypothesisTest(object):
    def __init__(self,data):
        self.data = data
        self.MakeModel()
        self.actual = self.TestStatistic(data)
    def PValue(self, iters = 1000, repeat = 10):
        pvaluelist = []
        for i in range(repeat):
            self.test_stats = [self.TestStatistic(self.RunModel()) for _ in range(iters)]
            count = sum(1 for x in self.test_stats if x>= self.actual)
            pvaluelist.append(count/iters)
        return sum(pvaluelist)/repeat
    def TestStatistic(self,data):
        raise UnimplementedMethodException()
    def MakeModel(self):
        pass
    def RunModel(self):
        raise UnimplementedMethodException()

def pmfconverter(period):
    return period.value_counts().sort_index()/len(period)
def findav(period):
    return 1/float(len(period.value_counts()))   

class MegaballTestChi(HypothesisTest):
    def TestStatistic(self, data):
        observedprob = pmfconverter(data)
        expectedprob = findav(data)
        test_stat = sum((observedprob-expectedprob)**2/expectedprob)
        return test_stat
    def RunModel(self):
        n = len(self.data)
        values = sorted(self.data.value_counts().index)
        simulation = pd.Series(np.random.choice(values, n, replace=True))
        return simulation
        
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


keys = ['First period', 'Second period', 'Third period', 'Fourth period', 'Fifth period']
values = [firstperiod, secondperiod, thirdperiod, fourthperiod, fifthperiod]
d = OrderedDict(zip(keys,values))

for k, v in d.items():
    pvalue = MegaballTestChi(v.megaball).PValue()
    print k, 'has a p-value of', pvalue

