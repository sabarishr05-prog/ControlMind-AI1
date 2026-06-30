import streamlit as st
import requests
BACKEND_URL= "https://controlmind-ai-backend.onrender.com"
# Page configuration
st.set_page_config(
    page_title="ControlMind AI",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
st.sidebar.title("🤖 ControlMind AI")
st.sidebar.markdown("### AI Copilot for Automation Engineers")

st.sidebar.markdown("""
### Available Modules
- 🔧 Sensor Assistant
- ⚙️ PLC Assistant
- 🎯 PID Assistant
- 📄 Datasheet Analyzer
- 💻 Arduino Assistant
- 🛠️ Troubleshooting Assistant
""")

# Main title
st.title("🤖 ControlMind AI")
st.subheader("AI Copilot for Automation and Embedded Systems")

# Assistant selection
assistant = st.selectbox(
    "Select Assistant",
    [
        "Sensor Assistant",
        "PLC Assistant",
        "PID Assistant",
        "Datasheet Analyzer",
        "Arduino Assistant",
        "Troubleshooting Assistant"
    ]
)

# User input
if assistant == "Datasheet Analyzer":
    uploaded_file = st.file_uploader(
        "Upload Datasheet PDF",
        type=["pdf"]
    )

    query = st.text_area(
        "Ask a question about the datasheet",
        height=150
    )

elif assistant == "Troubleshooting Assistant":
    query = st.text_area(
        "Describe the issue you are facing",
        height=200
    )

else:
    query = st.text_area(
        "Enter your query",
        height=200
    )

# API endpoint mapping
api_map = {
    "Sensor Assistant": "sensor",
    "PLC Assistant": "plc",
    "PID Assistant": "pid",
    "Datasheet Analyzer": "datasheet",
    "Arduino Assistant": "arduino",
    "Troubleshooting Assistant": "troubleshoot"
}

# Submit button
if st.button("🚀 Ask ControlMind AI"):

    if query.strip() == "":
        st.warning("Please enter a query.")
    else:

        endpoint = api_map[assistant]

        # Troubleshooting assistant uses "issue"
        if assistant == "Troubleshooting Assistant":
            payload = {
                "issue": query
            }
        else:
            payload = {
                "question": query
            }

        try:
            with st.spinner("Generating response..."):

                if assistant == "Datasheet Analyzer" and uploaded_file is None:
                     st.warning("Please upload a PDF.")
                     st.stop()

                     files = {
                         "file": (
                         uploaded_file.name,
                         uploaded_file,
                         "application/pdf"
                         )
                      }

                     response = requests.post(
        "{BACKEND_URL}/datasheet",
        files=files
                      )

                else:
                     response = requests.post(
        f"{BACKEND_URL}/{endpoint}",
        json=payload
                     )

            if response.status_code == 200:

                result = response.json()

                st.success("Response Generated Successfully")

                # Display module name
                st.subheader(result["module"])

                # Display Gemini response
                st.chat_message("assistant").markdown(
                    result["answer"]
                )

            else:
                st.error(
                    f"Backend returned error: {response.status_code}"
                )

        except Exception as e:
            st.error(
                f"Unable to connect to backend.\n\n{e}"
            )
