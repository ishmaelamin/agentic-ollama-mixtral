import streamlit as st
import requests

st.title("Mixtral Agent Chat")

# Define the FastAPI endpoint
FASTAPI_URL = "http://127.0.0.1:8000/ask/"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask Mixtral anything..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send request to FastAPI backend
    with st.chat_message("assistant"):
        with st.spinner("Waiting for agent..."):
            payload = {"prompt": prompt}
            try:
                response = requests.post(FASTAPI_URL, json=payload, timeout=120)
                response.raise_for_status()
                message_placeholder = st.empty()
                assistant_response = response.json().get("response", "Error: Could not get response from agent.")
                message_placeholder.markdown(assistant_response)
            except requests.exceptions.RequestException as e:
                st.error(f"Error communicating with the backend: {e}")
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
