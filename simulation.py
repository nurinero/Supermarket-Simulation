import argparse
import pandas as pd
import numpy as np
import market
## args pars 
#load class module
#inventory is dic
id = 1 
timestamp = pd.Timestamp('2017-01-01T12')
transimatrix = pd.read_csv("/Users/max/spiced/binomial-baharat-student-code/week_08/tm.csv",index_col=0)

print (transimatrix.head())
startprobability = [0.        , 0.28757555, 0.15352586, 0.37743452, 0.18146407]

inventory = {"dairy":100,"drinks":100,"fruit":100,"spices":100}

print(inventory)



opening = pd.Timestamp('2017-01-01T12')
closing = pd.Timestamp('2017-01-01T13')
Supersupermarket = market.Supermarket(opening=opening,closing=closing,prob_customers=10,inventory=inventory,transition_matrix=transimatrix,start_proba=startprobability)


Supersupermarket.simulation_movement_market()
print(Supersupermarket.create_costumer_dataframe())
