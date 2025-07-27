import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langrgraph_agenticai_app():
    """
    Loads and runs LangGraph AgentiAI app using Streamlit.

    """

    # loading UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load to user input from UI")
        return
    
    user_message = st.chat_input("Enter you message: ")