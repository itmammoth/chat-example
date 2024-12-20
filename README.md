# Chat Example

A ChatGPT-like example with [LangChain](https://www.langchain.com/) and [Streamlit](https://streamlit.io/) in just 45 lines of code.

![Chatting Example](images/chatting.gif)

## Requirements

- [OpenAI](https://openai.com/) API key
- [Tavily](https://tavily.com/) API key

## Setup

```bash
# Virtual environment (if necessary)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Edit your API keys
cp .streamlit/secrets_sample.toml .streamlit/secrets.toml
vi .streamlit/secrets.toml

# Run the app
streamlit run app.py
```