import pandas as pd
import csv

DATAPATH = '/Users/mac/major_graph/neo4j-community/import'
data = pd.read_csv(DATAPATH+'/1to2.csv')

print(data.loc[2])