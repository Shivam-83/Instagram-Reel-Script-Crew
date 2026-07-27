import streamlit as st
from crew_reel import generate_reel

st.set_page_config(
    page_title="Instagram Reel Generator",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 AI Instagram Reel Generator")

st.write(
    "Generate viral Instagram Reel ideas, scripts and captions using CrewAI + Gemini."
)

theme = st.text_input(
    "Enter Reel Theme",
    placeholder="Example: A day in the life of a CSE student during placement season"
)

generate = st.button("🚀 Generate Reel")

if generate:

    if theme.strip() == "":
        st.warning("Please enter a reel theme.")
        st.stop()

    with st.spinner("Generating Reel..."):

        result = generate_reel(theme)

    st.success("Done!")

    st.markdown(result)