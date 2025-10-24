# Agriculture Chatbot & Multi-State Crop Comparison

An interactive **Streamlit** app to explore and compare top crop production across multiple Indian states. The app fetches real-time data from a **FastAPI** backend using government datasets and displays both textual summaries and interactive **Altair** bar charts.

## Features

- Input multiple states separated by commas (e.g., Maharashtra, Karnataka, Tamil Nadu).  
- Fetches top crops and production data via FastAPI backend.  
- Displays textual summaries of top crops per state.  
- Visualizes multi-state crop comparison with interactive Altair bar charts.  

## Backend

- Built with **FastAPI**.  
- Endpoint: `/top_crops/{state}` returns top 3 crops by production for the given state.  
- Fetches live crop data from [Data.gov.in API](https://data.gov.in/resource/35be999b-0208-4354-b557-f6ca9a5355de).  

## Frontend

- Built with **Streamlit**.  
- User-friendly input for multiple states.  
- Chatbot-style interface showing state-wise crop data.  
- Dynamic bar charts for comparing crop production across states.  
-----------------------------------------------------------------------------------------------------
## Installation

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd <repo_folder>
   
2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


3. Install dependencies:

py -m pip install -r requirements.txt


4. Start the backend:

uvicorn backend:app --reload


5. Start the frontend:

streamlit run frontend.py
-----------------------------------------------------------------------------------
Usage

Open the Streamlit app in your browser.

Type states separated by commas in the input box.

View top crops in text and charts for comparison.
