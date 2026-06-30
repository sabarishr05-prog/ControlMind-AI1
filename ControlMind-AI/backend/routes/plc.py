from fastapi import APIRouter
from pydantic import BaseModel
from services.gemini_service import ask_gemini

router = APIRouter()

class PLCQuestion(BaseModel):
    question: str

@router.post("/plc")
def plc_assistant(data: PLCQuestion):

    prompt = f"""
You are ControlMind AI.

You are an expert PLC Programmer and Industrial Automation Engineer.

Answer ONLY PLC and industrial automation questions.

Your response must always contain the following sections:

1. Problem Understanding
2. PLC Logic Explanation
3. Inputs Required
4. Outputs Required
5. Ladder Logic (Text Representation)
6. Industrial Applications
7. Safety Considerations

Question:
{data.question}

If the user asks to generate ladder logic, provide a clear text-based ladder logic representation.
"""

    answer = ask_gemini(prompt)

    return {
        "module": "PLC Assistant",
        "answer": answer
    }