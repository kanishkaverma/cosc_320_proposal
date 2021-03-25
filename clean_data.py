#%% 

import pandas as pd


#%% 

df = pd.read_csv('./data/flight_data.csv')
df.head()


#%% 
df = df[['FlightDate','OriginAirportID','OriginStateName', 'DestAirportID', 'DestCityName','DestStateName','CRSDepTime','DepTime','CRSArrTime','ArrTime','AirTime','Distance']]
df.head() 

#%% 
df.isnull().sum()

#%% 

df.dropna(axis=0,how='any',inplace=True)
df.isnull().sum()
#%% 


df.head()

#%%
df.to_csv('./data/flight_data_cleaned.csv',index=True)