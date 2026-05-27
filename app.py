# app.py

import streamlit as st
from src.rag_pipeline import StudentGuidanceRAG

# ─── Page Config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Student Guidance AI",
    page_icon="🎓",
    layout="centered"
)

# ─── Header ───────────────────────────────────────────────────
st.title("🎓 Student Guidance AI created by PRASAD")
st.caption(
    "Your 24/7 AI counselor for learning paths, "
    "placement preparation, and career guidance."
)

# ─── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")

    groq_api_key = st.text_input(
        "Groq API Key",
        type="password",
        help="Get free key at https://console.groq.com"
    )

    if not groq_api_key:
        st.warning("Please enter your Groq API key.")

    st.divider()

    st.markdown("### 💡 What I can help with:")
    st.markdown("""
- 📚 Learning paths (Python, AI/ML, DSA)
- 💼 Placement preparation
- 📝 Resume tips
- 🎯 Interview preparation
- 🗺️ Career guidance
- 📖 Course recommendations
    """)

    st.divider()

    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        if "rag" in st.session_state:
            st.session_state.rag.clear_history()
        st.rerun()

    st.divider()
    st.markdown("### 💬 Sample Questions:")
    sample_questions = [
        "How do I start learning Python?",
        "How to prepare for coding interviews?",
        "Should I choose AI/ML or Web Dev?",
        "How to write a good resume?",
        "What is the DSA roadmap?",
        "Which companies hire freshers?",
    ]
    for q in sample_questions:
        if st.button(q, key=q):
            st.session_state.sample_question = q
            st.rerun()

# ─── Initialize session state ─────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

if "rag" not in st.session_state:
    st.session_state.rag = None

# ─── Initialize RAG pipeline ──────────────────────────────────
if groq_api_key and st.session_state.rag is None:
    with st.spinner("📚 Loading knowledge base..."):
        try:
            st.session_state.rag = StudentGuidanceRAG(
                groq_api_key=groq_api_key
            )
            st.success("✅ Knowledge base loaded!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# ─── Display chat messages ─────────────────────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ─── Welcome message ──────────────────────────────────────────
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown("""
👋 **Hello! I'm your Student Guidance AI.**

I can help you with:
- 🗺️ **Learning paths** for Python, AI/ML, DSA, Web Dev
- 💼 **Placement preparation** and interview tips
- 📝 **Resume writing** guidance
- 🎯 **Career decisions** and domain selection
- 📚 **Course and resource recommendations**

**Ask me anything!** For example:
> *"How should I prepare for product company interviews?"*
        """)

# ─── Handle sample question from sidebar ──────────────────────
if "sample_question" in st.session_state:
    user_input = st.session_state.sample_question
    del st.session_state.sample_question

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    if st.session_state.rag:
        with st.chat_message("assistant"):
            with st.spinner("🤔 Thinking..."):
                answer = st.session_state.rag.ask(user_input)
                st.markdown(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })
    st.rerun()

# ─── Chat input ───────────────────────────────────────────────
user_input = st.chat_input("Ask your question here...")

if user_input:
    if not groq_api_key:
        st.warning("Please enter your Groq API key in the sidebar.")
        st.stop()

    if not st.session_state.rag:
        st.warning("Knowledge base is loading. Please wait.")
        st.stop()

    # ✅ Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # ✅ Generate answer
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            try:
                answer = st.session_state.rag.ask(user_input)
                st.markdown(answer)

                # ✅ Add assistant message
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(f"❌ Error: {e}")