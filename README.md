# PMA Chatbot

A Streamlit chatbot that answers questions about Pakistan Military Academy using Google Gemini. A system prompt keeps answers on topic, short and polite.

## Files

- `app.py` - Streamlit chat UI
- `chatbot.py` - Gemini call
- `prompts.py` - system prompt and rules
- `config.py` - loads settings from `.env`

## Setup

```bash
pip install -r requirements.txt
```n
Copy `.env.example` to `.env` and add your key, then:

```bash
streamlit run app.py
```n
## Tech stack

Python, Streamlit, Google Gemini
