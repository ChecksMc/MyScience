
import time
import sys
import config
from lidar_reader import read_lidar_data
from Optimizer import Minimax, RuleBasedOptimizer

# Placeholder for SUMO vehicle number interface
def get_sumo_vehicle_number():
    # TODO: Implement actual SUMO interface
    return 0


def main_loop(algorithm="minimax"):
    if algorithm == "minimax":
        optimizer = Minimax()
    elif algorithm == "rule":
        optimizer = RuleBasedOptimizer()
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")
    iteration = 0
    curlane = 1
    while True:
        vehicles = read_lidar_data(config.LIDAR_SCAN_PATH)
        size_counts = {k: 0 for k in config.VEHICLE_SIZES.keys()}
        for v in vehicles:
            if v.size_category in size_counts:
                size_counts[v.size_category] += 1
        decision = optimizer.decide(size_counts)
        print(f"Iteration {iteration}: Vehicle counts: {size_counts}, {algorithm} decision: {decision}")
        sumo_vehicle_number = get_sumo_vehicle_number()
        print(f"SUMO vehicle number: {sumo_vehicle_number}")
        curtime = 1.0 / config.LIDAR_SCAN_FREQ_HZ
        
        iteration += curtime
        if iteration >= config.MAX_WAIT and vehicle(vehicles, curlane):
            decision = True
            iteration = 0
        time.sleep(curtime)

def vehicle(vehicles, curlane):
    for v in vehicles:
        if curlane == v.in_lane:
            return True
if __name__ == "__main__":
    # Usage: python traffic_optimizer.py [minimax|rule]
    algo = sys.argv[1] if len(sys.argv) > 1 else config.OPTIMIZER_TYPE
    main_loop(algo)
