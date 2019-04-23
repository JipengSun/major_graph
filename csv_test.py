import pandas as pd
import csv
#import synonyms
import re

DATAPATH = '/Users/mac/major_graph/neo4j-community/import'
#data = pd.read_csv(DATAPATH+'/1to2.csv')

#print(data.loc[2])

#print(synonyms.compare('第十一章','第章',seg=True))

a = re.match(r'.*第..章|.*第.章','我们第十十章').end()
print(len('我们第十十章'))
print(a)