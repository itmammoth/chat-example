# Chat Example

A ChatGPT-like example with Streamlit. 

![Chatting Example](images/chatting.gif)

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
