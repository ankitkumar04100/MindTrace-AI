from fastapi import APIRouter

router = APIRouter()

@router.get("/result")
def get_insights(score: float):
    if score < 0.4:
        level = "Low Stress"
        recommendation = "Maintain healthy habits"
    elif score < 0.7:
        level = "Moderate Stress"
        recommendation = "Consider short breaks and mindfulness"
    else:
        level = "High Burnout Risk"
        recommendation = "Seek rest, support, and professional guidance"

    return {
        "risk_level": level,
        "recommendation": recommendation
    }
