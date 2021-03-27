from queue import PriorityQueue
from graph_from_csv import makeGraph
import airport_graph as ag

graph = makeGraph('./flight_data_cleaned_final.csv', 10)
# add to currentime by flight time. when checking the weighting time, get difference between currenttime
#current time = deptime + air time
# def solution(flights, src, dst, s):
# 	pq = PriorityQueue()
# 	initState = State(src, s)
# 	pq.add(initState)
# 	visitedStates = []
# 	while pq not empty:
# 		currentState = pq.pop()
#         if currentState.currentAirport == dst:
#             return currentState.prevFlights
#         for flight in flights[currentState.currentAirport]:
#             if flight.startTime > currentState.currentTime and flight.dest not in currentState.prevFlights
#               newState = State(flight, currentState)
# If newState not in visitedStates
# pq.add(newState)
# 	visitedStates.append(new State)
# return null // In the event all possible states were checked and there was no possible flight


def solution(graph, flights, src, dst, s):
    pq = PriorityQueue()
    initState = [] #State(src, flights, )
    pq.add(initState)
    visitedStates = []
    while pq.empty()== False: 
        currentState = pq.pop()
        if currentState.currentAirport == dst:
            return currentState.prevFlights 

def realSolution(G: ag.Graph, src: int, dst: int, startTime: s):
    if src not in G.airports or dst not in G.airports:
        print("The src and destination are not both in the graph")
        return []
    else:
        