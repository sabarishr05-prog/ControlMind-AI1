from fastapi import APIRouter
from pydantic import BaseModel
from services.gemini_service import ask_gemini

router = APIRouter()

class ArduinoQuestion(BaseModel):
    question: str

@router.post("/arduino")
def arduino_assistant(data: ArduinoQuestion):

    prompt = f"""
You are an Arduino and Embedded Systems Expert.

Format your response using Markdown.

Generate professional Arduino solutions.

Always provide:

1. Objective
2. Components Required
3. Circuit Connections
4. Arduino Code
5. Code Explanation
6. Libraries Used
7. Expected Output
8. Applications
9. Troubleshooting Tips

Question:

{data.question}
"""

    answer = ask_gemini(prompt)

    return {
        "module":"Arduino Assistant",
        "answer":answer
    }