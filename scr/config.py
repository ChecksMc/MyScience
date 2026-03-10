# config.py
# All configuration parameters for the traffic optimizer

# LiDAR parameters
LIDAR_SCAN_PATH = "LiDAR Scan ergebnisse/solution/"
LIDAR_SCAN_FREQ_HZ = 2  # Scan frequency in Hz

# Vehicle size thresholds (in meters)
VEHICLE_SIZES = {
    "motorcycle": (0, 2.0),
    "car": (2.0, 5.0),
    "van": (5.0, 7.0),
    "truck": (7.0, 12.0),
    "bus": (12.0, 20.0)
}

# SUMO integration
SUMO_VEHICLE_NUMBER_KEY = "vehicle_number"
SUMO_CONFIG_PATH = "Simulation/Kreuzung1.net.xml"

# Optimization parameters
OPTIMIZER_TYPE = "minimax"
TRAFFIC_LIGHT_CYCLE = 30  # seconds

# Add more parameters as needed

MAX_WAIT = 120
