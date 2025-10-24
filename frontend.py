import requests
import pandas as pd
import altair as alt
import streamlit as st

API_URL = "http://127.0.0.1:8000/top_crops"

def get_top_crops(state_name):
    try:
        response = requests.get(f"{API_URL}/{state_name}")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API returned {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

st.title("Agriculture Chatbot & Multi-State Crop Comparison")

# Input box
user_input = st.text_input("You: Type states separated by commas (e.g., Maharashtra, Karnataka, Tamil Nadu)")

if user_input:
    # Parse states from input
    states = [s.strip().title() for s in user_input.split(",") if s.strip()]
    if not states:
        st.text("Please enter at least one state.")
        st.stop()

    all_data = []
    text_outputs = []

    for state in states:
        data = get_top_crops(state)
        if "top_crops" in data:
            text = ", ".join([f"{c['crop']}: {c['production_']}" for c in data["top_crops"]])
            text_outputs.append(f"Top crops in {state}: {text}")
            df = pd.DataFrame(data["top_crops"])
            df["state"] = state
            all_data.append(df)
        else:
            text_outputs.append(f"{state}: {data.get('error', 'No data')}")

    # Show textual output
    st.text_area("Bot:", value="\n".join(text_outputs), height=150)

    # Show comparison chart if any valid data
    if all_data:
        df_compare = pd.concat(all_data, ignore_index=True)
        chart = alt.Chart(df_compare).mark_bar().encode(
            x=alt.X('crop:N', title='Crop'),
            y=alt.Y('production_:Q', title='Production'),
            color='state:N',
            column='state:N',
            tooltip=['crop', 'production_']
        )
        st.altair_chart(chart, use_container_width=True)
