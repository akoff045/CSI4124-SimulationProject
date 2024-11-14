# Parameters Observed
This simulation specifically observes:
1. **Arrival Rates**: How frequently PEVs show up at each charging station.
2. **Charging Demand**: The number of PEVs at each station over time.
3. **Impact of Charging Prices**: How different prices at stations affect which ones drivers choose.
4. **Congestion Levels**: How busy each station gets based on its capacity to serve cars.
5. **Station Utilization and Traffic Flow**: The relationship between the number of PEVs a station serves and the flow of cars across the network.

# How It Works in python

1. **ChargingStation Class**: 
   - This part of the code creates the structure for each charging station.
   - Each station has a few key properties, like:
     - **Capacity**: The number of cars it can charge at the same time.
     - **Base Price**: The cost for charging at that station, which might impact a driver’s choice.

2. **QueueNetwork Class**:
   - This part of the code creates a network of multiple charging stations.
   The class does: 
     - **Network Initialization**: We set up each station’s capacity and price.
     - **Simulation of Demand**: The code then runs a virtual experiment where PEVs randomly arrive at the stations.
     - **Station Selection**: Each car “decides” which station to go to, based on price and how busy each station is.

3. **Simulation Process**:
   - The simulation generates PEV arrivals and monitors their behavior at each station over a set time period (for example, over 100 steps of time).
   - Each car arrives at a random station, waits if the station is busy, or starts charging if a spot is available. 
   - This process helps us observe how charging demand builds up and how congestion (busy stations) affects the overall system.
