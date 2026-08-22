"""
agent.py
--------
JARVISxSalim with Agno + DuckDuckGo Web Search
"""

import streamlit as st
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.groq import Groq
from datetime import datetime


def _get_api_key() -> str:
    api_key = st.secrets.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY not found. Add it to .streamlit/secrets.toml "
            'as: GROQ_API_KEY = "gsk_..."'
        )
    return api_key


def get_memory():
    """Simple session memory stored in st.session_state."""
    if "agent_memory" not in st.session_state:
        st.session_state.agent_memory = []
    return st.session_state.agent_memory


def reset_memory() -> None:
    """Clear stored memory."""
    st.session_state.pop("agent_memory", None)
    st.session_state.pop("messages", None)


def stream_agent_reply(user_input: str, placeholder) -> str:
    """
    Send user_input through Agno agent with DuckDuckGo web search.
    """
    memory = get_memory()
    
    # Build conversation history for context
    history = ""
    if memory:
        recent = memory[-6:]  # Last 6 messages for context
        for msg in recent:
            role = "User" if msg["role"] == "user" else "JARVIS"
            history += f"{role}: {msg['content']}\n"
    
    # Current date/time
    current_datetime = datetime.now().strftime("%A, %B %d, %Y at %I:%M %p")
    
    # ---------- CREATE AGNO AGENT ----------
    agent = Agent(
        model=Groq(
            id="openai/gpt-oss-120b",
            api_key=_get_api_key(),
        ),
        tools=[DuckDuckGoTools()],
        instructions=(
            f"You are JARVISxSalim, a witty, sharp personal AI assistant. "
            f"Today's date and time is: {current_datetime}. "
            f"Address the user as 'sir' occasionally. "
            f"Keep answers concise and helpful. "
            f"Use DuckDuckGo search when you need current information, dates, times, news, or real-time data. "
            f"Always cite sources in your answers. "
            f"Be conversational and engaging. "
            f"Previous conversation: {history}"
        ),
        markdown=True,
    )
    
    # ---------- RUN AGENT ----------
    try:
        # 🔥 FIXED: Properly handle streaming response
        response = agent.run(user_input, stream=True)
        
        full_response = ""
        
        # 🔥 FIXED: Iterate through response chunks correctly
        for chunk in response:
            if hasattr(chunk, 'content'):
                # If chunk has content attribute
                content = chunk.content
                if content:
                    full_response += content
                    placeholder.markdown(full_response + "▌")
            elif isinstance(chunk, str):
                # If chunk is directly string
                full_response += chunk
                placeholder.markdown(full_response + "▌")
            else:
                # 🔥 FIXED: Handle RunResponse objects
                try:
                    if hasattr(chunk, 'output'):
                        content = str(chunk.output)
                        if content:
                            full_response += content
                            placeholder.markdown(full_response + "▌")
                    elif hasattr(chunk, 'message'):
                        content = str(chunk.message)
                        if content:
                            full_response += content
                            placeholder.markdown(full_response + "▌")
                except:
                    pass
        
        placeholder.markdown(full_response)
        
        # Save to memory
        memory.append({"role": "user", "content": user_input})
        memory.append({"role": "assistant", "content": full_response})
        
        return full_response
        
    except Exception as e:
        error_msg = f"⚠️ Agent error: {e}"
        placeholder.markdown(error_msg)
        return error_msg