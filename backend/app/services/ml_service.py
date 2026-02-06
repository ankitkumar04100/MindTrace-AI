import random

def predict_stress(features: dict):
    # Simulated ML inference (Random Forest placeholder)
    base_score = features["fatigue_index"]
    noise = random.uniform(-0.05, 0.05)
    score = min(max(base_score + noise, 0), 1)

    return round(score, 2)
