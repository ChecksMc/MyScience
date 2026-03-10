import os
import csv
from typing import List, Dict, Any
import config


class Vehicle:
    def __init__(self, vehicle_id: str, length: float, width: float, speed: float, in_lane: bool):
        self.vehicle_id = vehicle_id
        self.length = length
        self.width = width
        self.speed = speed
        self.in_lane = in_lane
        self.size_category = self.categorize_size()

    def categorize_size(self) -> str:
        for category, (min_len, max_len) in config.VEHICLE_SIZES.items():
            if min_len <= self.length < max_len:
                return category
        return "unknown"



def read_lidar_data(scan_folder: str) -> List[Vehicle]:
    vehicles = []
    csv_path = os.path.join(scan_folder, "GLOBAL_vehicle_dataset.csv")
    if not os.path.exists(csv_path):
        return vehicles
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vehicle_id = row.get("id", "")
            length = float(row.get("length", 0))
            width = float(row.get("width", 0))
            speed = float(row.get("speed", 0))
            # Expecting 'in_lane' column as 0/1 or True/False
            in_lane = row.get("in_lane", "0")
            in_lane = str(in_lane).strip().lower() in ("1", "true", "yes")
            vehicles.append(Vehicle(vehicle_id, length, width, speed, in_lane))
    return vehicles

# Example usage:
# vehicles = read_lidar_data(config.LIDAR_SCAN_PATH)
# for v in vehicles:
#     print(v.vehicle_id, v.size_category, v.in_lane)
