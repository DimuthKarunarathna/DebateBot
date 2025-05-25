import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from backend.debate_manager import debate_rounds

# DebateBot - A Streamlit app for debating topics with AI
# This app allows users to engage in debates with AI or with another user.
# It uses the backend debate_manager to handle the debate logic.
st.title("🧠 DebateBot")

mode = st.selectbox("Select Debate Mode", ["🗣️ 1v1 Mode", "🤖 AI vs AI"])
topic = st.text_input("Enter the Debate Topic")
n_rounds = st.slider("Number of Rounds", min_value=1, max_value=10, value=5)

if mode == "🗣️ 1v1 Mode":
    user_stance = st.selectbox("Choose your stance", ["For", "Against"])
    bot_stance = "Against" if user_stance == "For" else "For"
    if st.button("Start Debate"):
        st.subheader("Debate Transcript")
        transcript = debate_rounds(topic, user_stance, bot_stance, n_rounds)
        for i, (speaker, arg) in enumerate(transcript):
            st.markdown(f"**{speaker}** (Round {i+1}): {arg}")

elif mode == "🤖 AI vs AI":
    if st.button("Start Debate"):
        st.subheader("Debate Transcript")
        transcript = debate_rounds(topic, "For", "Against", n_rounds)
        for i, (speaker, arg) in enumerate(transcript):
            st.markdown(f"**{speaker} Bot** (Round {i+1}): {arg}")
