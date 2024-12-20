import streamlit as st
from langchain_community.tools.openai_dalle_image_generation import OpenAIDALLEImageGenerationTool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

config = {"configurable": {"thread_id": "abc123"}}


def yield_content(app_stream):
    for chunk, metadata in app_stream:
        if isinstance(chunk, AIMessage):
            yield chunk.content


if "app" not in st.session_state:
    model = ChatOpenAI(model="gpt-4o")
    tools = [
        OpenAIDALLEImageGenerationTool(api_wrapper=DallEAPIWrapper(model="dall-e-3")),
        TavilySearchResults(max_results=3),
    ]
    agent_executor = create_react_agent(model, tools, checkpointer=MemorySaver())
    st.session_state.app = agent_executor

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Chat Example")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What's up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = st.session_state.app.stream({"messages": [HumanMessage(prompt)]}, config, stream_mode="messages")
        content = st.write_stream(yield_content(stream))
        st.session_state.messages.append({"role": "assistant", "content": content})
