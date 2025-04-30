import streamlit as st
import openai
import os
from openai import OpenAI

# Page configuration
st.set_page_config(
    page_title="vhs GPT Heilbronn",
    page_icon="💬",
    layout="wide"
)

# Initialize session states
if "messages" not in st.session_state:
    st.session_state.messages = []

if "openai_client" not in st.session_state:
    # Get API key from environment variable or prompt user
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        st.session_state.openai_client = OpenAI(api_key=api_key)
        st.session_state.api_key_provided = True
    else:
        st.session_state.api_key_provided = False
        st.session_state.openai_client = None

# Main UI
st.title("ChatGPT Clone (o1-mini)")

# API Key input if not provided via environment variable
if not st.session_state.api_key_provided:
    api_key = st.text_input("Enter your OpenAI API key:", type="password")
    if api_key:
        try:
            st.session_state.openai_client = OpenAI(api_key=api_key)
            st.session_state.api_key_provided = True
            st.success("API key set successfully!")
            st.rerun()
        except Exception as e:
            st.error(f"Error setting API key: {str(e)}")

# Only show chat interface if API key is provided
if st.session_state.api_key_provided:
    # Button to start a new conversation
    if st.button("Neue Unterhaltung"):
        st.session_state.messages = []
        st.rerun()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Was möchtest du besprechen?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message in chat
        with st.chat_message("user"):
            st.write(prompt)
        
        # Display assistant response with streaming
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                # Create a streaming completion
                stream = st.session_state.openai_client.chat.completions.create(
                    model="gpt-4.1-mini-2025-04-14",
                    messages=[
                        {"role": m["role"], "content": m["content"]} 
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
                
                # Process the streaming response
                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        message_placeholder.write(full_response + "▌")
                
                # Final update without the cursor
                message_placeholder.write(full_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                error_message = f"Error: {str(e)}"
                message_placeholder.error(error_message)
                st.error("There was an error processing your request. Please try again or check your API key.")
else:
    # Display message if API key is not provided
    st.info("Please provide your OpenAI API key to start chatting.")
    st.write("This application uses OpenAI's o1-mini model to generate responses.")
    st.write("Your API key is required to access the OpenAI API.")

