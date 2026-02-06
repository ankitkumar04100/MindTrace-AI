def extract_features(response_time, error_rate, consistency):
    fatigue_index = (response_time * 0.4) + (error_rate * 0.4) + ((1 - consistency) * 0.2)

    return {
        "response_time": response_time,
        "error_rate": error_rate,
        "consistency": consistency,
        "fatigue_index": round(fatigue_index, 3)
    }
