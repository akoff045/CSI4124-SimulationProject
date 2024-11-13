import numpy as np
import matplotlib.pyplot as plt

# Define a ChargingStation class representing a single charging station
class ChargingStation:
    def __init__(self, station_id, capacity, base_price):
        """
        Initialize a charging station.
        Arguments:
            station_id (int): Unique identifier for the station
            capacity (int): Max number of PEVs that can charge simultaneously
            base_price (float): Base price per unit of charging at this station
        """
        self.station_id = station_id
        self.capacity = capacity
        self.base_price = base_price
        self.queue = []  # Queue to hold PEVs waiting for a charger

    def arrive(self, pev_id):
        """
        Add a PEV to the charging queue.
        Arguments:
            pev_id (int): Unique identifier for the PEV
        """
        if len(self.queue) < self.capacity:
            self.queue.append(pev_id)  # Add PEV if capacity allows
            return True  # PEV successfully joined the queue
        else:
            return False  # Station is full

    def leave(self, pev_id):
        """
        Remove a PEV from the charging queue.
        Arguments:
            pev_id (int): Unique identifier for the PEV
        """
        if pev_id in self.queue:
            self.queue.remove(pev_id)

# Define a QueueNetwork class representing the entire charging network
class QueueNetwork:
    def __init__(self, num_stations, capacities, base_prices):
        """
        Initialize a network of charging stations.
        Arguments:
            num_stations (int): Number of charging stations
            capacities (list of int): List of capacities for each station
            base_prices (list of float): List of base prices for each station
        """
        self.stations = [
            ChargingStation(station_id=i, capacity=capacities[i], base_price=base_prices[i])
            for i in range(num_stations)
        ]

    def simulate_demand(self, num_pevs, arrival_rate, price_sensitivity, time_steps=100):
        """
        Simulate the charging demand over a period.
        Arguments:
            num_pevs (int): Total number of PEVs in the system
            arrival_rate (float): Average arrival rate of PEVs at stations
            price_sensitivity (float): Sensitivity of PEVs to price when selecting a station
            time_steps (int): Number of time steps for the simulation
        """
        for t in range(time_steps):
            for pev_id in range(num_pevs):
                # Randomly determine if a PEV arrives based on the arrival rate
                if np.random.rand() < arrival_rate:
                    # Select a station based on price sensitivity and capacity
                    selected_station = self.select_station(price_sensitivity)
                    if selected_station:
                        selected_station.arrive(pev_id)

    def select_station(self, price_sensitivity):
        """
        Select a station for a PEV based on price and congestion level.
        Arguments:
            price_sensitivity (float): Influence of price on station selection
        Returns:
            ChargingStation or None: The selected station, or None if all are full
        """
        station_scores = [
            station.base_price * price_sensitivity + len(station.queue) / station.capacity
            for station in self.stations
        ]
        min_score_idx = np.argmin(station_scores)
        return self.stations[min_score_idx]





