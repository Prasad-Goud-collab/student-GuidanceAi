# src/llm.py

from langchain_groq import ChatGroq


def get_llm(api_key: str) -> ChatGroq:
    """
    Returns Groq LLM instance.

    Args:
        api_key (str): Groq API key

    Returns:
        ChatGroq: LLM instance
    """
    return ChatGroq(
        api_key=api_key,
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=1024
    )