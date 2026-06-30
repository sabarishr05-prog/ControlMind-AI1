from fastapi import APIRouter
from pydantic import BaseModel
from services.gemini_service import ask_gemini

router = APIRouter()

class SensorQuestion(BaseModel):
    question: str

@router.post("/sensor")
def sensor_assistant(data: SensorQuestion):

    prompt = f"""
You are ControlMind AI.

You are an expert Instrumentation and Control Engineer.

Answer ONLY sensor-related questions.

Explain in simple engineering language.

Always provide:

1. Working Principle
2. Construction
3. Applications
4. Advantages
5. Disadvantages
6. Industrial Examples

Question:
{data.question}
"""

    answer = ask_gemini(prompt)

    return {
        "module": "Sensor Assistant",
        "answer": answer
    }