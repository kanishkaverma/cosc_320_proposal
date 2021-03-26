#%% 

import pandas as pd


#%% 

df = pd.read_csv('./data/flight_data.csv', parse_dates=[['FlightDate', 'DepTime']])
# df.set_index(['FlightDate', 'DepTime'], drop=False)

df.head()
df.isnull().sum()
#%%

df['FlightDate_DepTime'] =  pd.to_datetime(df['FlightDate_DepTime'],format="%m/%d/%Y %H%M", errors='coerce')
# df.dropna(axis=0,how='any',inplace=True)
df = df[['FlightDate_DepTime','OriginAirportID','OriginStateName', 'DestAirportID', 'DestCityName','DestStateName','AirTime','Distance']]
# df['FlightDate_DepTime'].dtypes
df.dtypes


# df[''] =  pd.to_datetime(df['FlightDate_DepTime'],format="%m/%d/%Y %H%M", errors='coerce')
# print(df['FlightDate_DepTime'].dt.time)
#%% 

df.dropna(axis=0,how='any',inplace=True)


df.head()

# df.dtypes
#%% 
# df.isnull().sum()

# df.dropna(axis=0,how='any',inplace=True)


#%% 

# bad_timezone_flights =  df[(df['CRSArrTime']== df['CRSDepTime'])].index
# df.drop( bad_timezone_flights, inplace=True)
# df[df['CRSArrTime'] == df['CRSDepTime']]
df.to_csv('./data/flight_data_cleaned.csv',index=True)

#%% 

# bad_timezone_flights_2 =  df[(df['CRSArrTime'] <df['CRSDepTime'])].index
# # print(len(bad_timezone_flights_2))
# dg = df.loc[bad_timezone_flights_2]
# dg.head()


dg = df[['FlightDate_DepTime','OriginAirportID','OriginStateName', 'DestAirportID' ,'DestStateName','AirTime','Distance']]
#%%

dg.to_csv('./data/flight_data_cleaned_final.csv',index=True)