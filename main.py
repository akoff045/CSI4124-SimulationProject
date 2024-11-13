import numpy as np
from simulation import QueueNetwork

def main():
    # Define random test parameters
    num_stations = 5  # Number of charging stations
    capacities = np.random.randint(3, 10, size=num_stations)  # Random capacities for each station
    base_prices = np.round(np.random.uniform(0.5, 1.5, size=num_stations), 2)  # Random base prices

    # Initialize the charging network with random parameters
    network = QueueNetwork(num_stations=num_stations, capacities=capacities, base_prices=base_prices)

    # Define simulation parameters
    num_pevs = 100  # Number of PEVs to simulate
    arrival_rate = np.random.uniform(0.1, 0.5)  # Random arrival rate
    price_sensitivity = np.random.uniform(0.2, 1.0)  # Random price sensitivity level
    time_steps = 100  # Duration of the simulation in time steps

    # Print configuration for reference
    print("Charging Station Configuration:")
    for i, (capacity, price) in enumerate(zip(capacities, base_prices)):
        print(f"Station {i + 1} - Capacity: {capacity}, Base Price: ${price}")

    print("\nSimulation Parameters:")
    print(f"Total PEVs: {num_pevs}")
    print(f"Arrival Rate: {arrival_rate:.2f}")
    print(f"Price Sensitivity: {price_sensitivity:.2f}")
    print(f"Simulation Time Steps: {time_steps}\n")

    # Run the demand simulation
    network.simulate_demand(num_pevs=num_pevs, arrival_rate=arrival_rate, price_sensitivity=price_sensitivity, time_steps=time_steps)

    # Collect and print results
    print("Simulation Results:")
    for i, station in enumerate(network.stations):
        print(f"Station {i + 1} - Number of PEVs in queue: {len(station.queue)} / Capacity: {station.capacity}")

if __name__ == "__main__":
    main()
