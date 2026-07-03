# 🤖 ControlMind AI

**AI Copilot for Automation and Embedded Systems**

ControlMind AI is an AI-powered engineering assistant designed for students, engineers, and automation professionals.
It provides specialized assistance in PLC programming, PID tuning, sensor selection, Arduino development, industrial datasheet analysis, and industrial troubleshooting using Google's Gemini AI.

---

## 🚀 Features

### 🔹 Sensor Assistant
- Explain industrial sensors
- Compare sensors
- Sensor selection guidance
- Industrial applications

### 🔹 PLC Assistant
- PLC programming guidance
- Ladder logic generation
- PLC troubleshooting
- Industrial automation examples

### 🔹 PID Assistant
- PID controller explanation
- Controller tuning
- Overshoot and steady-state error analysis
- Practical control engineering tips

### 🔹 Datasheet Analyzer
- Upload PDF datasheets
- Extract technical specifications
- Summarize engineering documents
- Explain pin configurations and applications

### 🔹 Arduino Assistant
- Generate Arduino code
- Circuit connections
- Component recommendations
- Code explanation
- Troubleshooting tips

### 🔹 Troubleshooting Assistant
- Diagnose industrial automation problems
- PLC fault analysis
- Sensor fault diagnosis
- Arduino debugging
- Step-by-step solutions
- Preventive maintenance recommendations

---

## 🏗️ Tech Stack

### Backend
- Python
- FastAPI
- Google Gemini API
- PyMuPDF
- Uvicorn

### Frontend
- Streamlit

### Deployment
- Render

---

## 📂 Project Structure

```
ControlMind-AI/
│
├── backend/
│   ├── routes/
│   │   ├── sensor.py
│   │   ├── plc.py
│   │   ├── pid.py
│   │   ├── datasheet.py
│   │   ├── arduino.py
│   │   └── troubleshooting.py
│   │
│   ├── services/
│   │   ├── gemini_service.py
│   │   └── pdf_service.py
│   │
│   ├── uploads/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   └── app.py
│
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/sabarishr05-prog/ControlMind-AI.git
```

### Navigate to the backend

```bash
cd ControlMind-AI/backend
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### Start the backend

```bash
python -m uvicorn main:app --reload
```

### Run the Streamlit frontend

```bash
cd ../frontend
streamlit run app.py
```
## 🎯 Future Improvements

- Voice Assistant
- Authentication
- Chat History
- Report Generation
- Ladder Diagram Visualization
- PLC Simulator Integration
- Industrial Dashboard
- Multi-language Support

---

## 👨‍💻 Author

**Sabarish R**

Instrumentation and Control Systems Engineering

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, consider giving it a star!
