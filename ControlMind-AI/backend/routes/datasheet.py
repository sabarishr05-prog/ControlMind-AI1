from fastapi import APIRouter, UploadFile, File
import os

from services.pdf_service import extract_text_from_pdf
from services.gemini_service import ask_gemini

router = APIRouter()

UPLOAD_FOLDER = "uploads"

@router.post("/datasheet")
async def analyze_datasheet(file: UploadFile = File(...)):

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as f:
        f.write(await file.read())

    pdf_text = extract_text_from_pdf(filepath)

    prompt = f"""
You are an Instrumentation Engineer.

Analyze this datasheet.

Return ONLY these headings:

1. Device Name
2. Manufacturer
3. Working Principle
4. Measurement Range
5. Accuracy
6. Supply Voltage
7. Output Type
8. Pin Configuration
9. Applications
10. Advantages
11. Limitations
12. Important Specifications
13. Summary

Datasheet:

{pdf_text}
"""

    answer = ask_gemini(prompt)

    return {
        "module": "Datasheet Analyzer",
        "answer": answer
    }