# ChatGPT Clone with o1-mini

A Streamlit-based ChatGPT clone that uses OpenAI's o1-mini model with streaming text responses.

## Features

- Real-time streaming responses
- Conversation history management
- Clean, simple interface
- Secure API key handling

## Deployment on Streamlit Cloud

Follow these steps to deploy this app on Streamlit Cloud:

1. Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign up if you haven't already
2. Connect your GitHub account to Streamlit Cloud
3. Create a new GitHub repository and push this code to it
4. In Streamlit Cloud, click "New app" and select your repository
5. Set the main file path as `app.py`
6. In the "Advanced settings" section, add your OpenAI API key as a secret:
   - Key: `OPENAI_API_KEY`
   - Value: Your OpenAI API key
7. Click "Deploy!"

Your app will be deployed and accessible via a Streamlit Cloud URL.

## Local Development

To run this app locally:

1. Install the required packages: `pip install streamlit openai`
2. Set your OpenAI API key as an environment variable or enter it in the app
3. Run the app: `streamlit run app.py`