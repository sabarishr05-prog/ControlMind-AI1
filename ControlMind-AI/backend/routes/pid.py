from fastapi import APIRouter
from pydantic import BaseModel
from services.gemini_service import ask_gemini

router = APIRouter()

class PIDQuestion(BaseModel):
    question: str

@router.post("/pid")
def pid_assistant(data: PIDQuestion):

    prompt = f"""
You are ControlMind AI, an expert Control Systems Engineer.

Answer only PID and Control Engineering questions.

IMPORTANT:
- If the user asks a simple definition (e.g., "What is PID?"), give a direct explanation first. Do NOT include "Problem Analysis".
- If the user asks for troubleshooting, tuning, or design help, then use the following sections:
  1. Problem Analysis
  2. Theory
  3. PID Tuning Recommendation
  4. Expected Effect on System
  5. Industrial Applications
  6. Common Mistakes
  7. Practical Tips

Question:
{data.question}

If tuning is requested, explain how Kp, Ki and Kd should be adjusted and why.
"""

    answer = ask_gemini(prompt)

    return {
        "module": "PID Assistant",
        "answer": answer
    }