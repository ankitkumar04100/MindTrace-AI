import pickle
import numpy as np


def test_model_prediction():
    with open("ml/model/stress_model.pkl", "rb") as f:
        model = pickle.load(f)

    sample_input = np.array([[6, 5, 42, 3]])
    prediction = model.predict(sample_input)

    assert prediction is not None
