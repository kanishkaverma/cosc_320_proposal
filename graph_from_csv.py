
#%%
from airport_graph import Flight, Graph
import pandas as pd

#%%
def makeGraph(path_to_csv,n): 
    df = pd.read_csv(path_to_csv, parse_dates=['FlightDate_DepTime'])

    dg = df.sample( n, axis=0)
    flight_graph = Graph()
    
    for index, row in dg.iterrows():
        flight_graph.addAirport(row['OriginAirportID'])
        flight_graph.addAirport(row['DestAirportID'])
        fli = Flight(row['OriginAirportID'],row['DestAirportID'],row['FlightDate_DepTime'].timestamp(),row['AirTime'],row['Distance']) 
        flight_graph.addFlight(fli)
# makeGraph("./data/flight_data_cleaned_final.csv", 10)


