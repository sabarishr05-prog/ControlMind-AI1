from fastapi import APIRouter
from pydantic import BaseModel
from services.gemini_service import ask_gemini

router = APIRouter()

class TroubleRequest(BaseModel):
    issue: str


@router.post("/troubleshoot")
def troubleshoot(data: TroubleRequest):

    prompt = f"""
You are an Industrial Troubleshooting Expert.

Analyze the following problem:

{data.issue}

Provide:

1. Problem Summary
2. Possible Causes
3. Diagnostic Procedure
4. Recommended Solutions
5. Prevention Tips

Format in markdown.
"""

    answer = ask_gemini(prompt)

    return {
        "module":"Troubleshooting Assistant",
        "answer": answer
    }