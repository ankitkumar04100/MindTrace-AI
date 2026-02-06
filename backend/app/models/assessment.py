from pydantic import BaseModel

class Assessment(BaseModel):
    response_time: float
    error_rate: float
    consistency: float
