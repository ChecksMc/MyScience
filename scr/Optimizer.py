import dataclasses
@dataclasses.dataclass
class table:
    table: list[list[int]]


import config

class Minimax:
    def __init__(self, weights=None):
        # weights: dict mapping vehicle size to weight
        if weights is None:
            # Default: all weights 1
            self.weights = {k: 1 for k in config.VEHICLE_SIZES.keys()}
        else:
            self.weights = weights

    def decide(self, size_counts: dict) -> bool:
        # Weighted sum, threshold at 0 to decide
        score = sum(self.weights.get(k, 0) * v for k, v in size_counts.items())
        # Example: open if score > threshold (can be parameterized)
        threshold = sum(self.weights.values())  # or set in config
        return score > threshold


class RuleBasedOptimizer:
    def __init__(self, rules=None):
        # rules: dict mapping vehicle size to min count to trigger True
        if rules is None:
            self.rules = {k: 3 for k in config.VEHICLE_SIZES.keys()}  # default: 3 vehicles triggers
        else:
            self.rules = rules

    def decide(self, size_counts: dict) -> bool:
        # If any vehicle size exceeds its rule threshold, return True
        for k, min_count in self.rules.items():
            if size_counts.get(k, 0) >= min_count:
                return True
        return False
    
    
        