from fastapi import APIRouter
from app.services.feature_engine import extract_features
from app.services.ml_service import predict_stress

router = APIRouter()

@router.post("/submit")
def submit_assessment(response_time: float, error_rate: float, consistency: float):
    features = extract_features(response_time, error_rate, consistency)
    prediction = predict_stress(features)

    return {
        "features": features,
        "stress_prediction": prediction
    }
