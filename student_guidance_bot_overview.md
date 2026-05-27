# 🎓 Student Guidance AI — RAG-Based Conversational Chatbot

A production-grade RAG (Retrieval Augmented Generation) based conversational AI system that provides 24/7 guidance to students on learning paths, placement preparation, interview tips, and career decisions — deployed live on Hugging Face Spaces.

🔗 **Live Demo:** https://huggingface.co/spaces/komaraprasad/student-guidance-bot

---

## 🎯 Problem It Solves

> Students often struggle with questions like:
> - "Which programming language should I learn first?"
> - "How do I prepare for product company interviews?"
> - "What projects should I build for my resume?"
> - "Should I choose AI/ML or Web Development?"
>
> This AI bot answers all these questions instantly, 24/7 — no human counselor needed.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 💬 Conversational AI | ChatGPT-like chat interface for natural conversations |
| 🧠 RAG Pipeline | Retrieves relevant knowledge before generating answers |
| 💾 Conversation Memory | Remembers previous messages in the session |
| 📚 Rich Knowledge Base | Covers Python, AI/ML, DSA, placement prep, career guidance |
| ⚡ Fast Responses | Powered by Groq LLM (fastest inference available) |
| 🌐 24/7 Availability | Deployed on Hugging Face Spaces — always online |
| 🎯 Sample Questions | Quick-access buttons for common student queries |
| 🔒 Secure | No API keys stored — users provide their own |

---

## 🏗️ Architecture

```
Student asks question (Streamlit Chat UI)
              ↓
Question sent to RAG Pipeline
              ↓
FAISS Semantic Search
(finds top 4 relevant chunks from knowledge base)
              ↓
Retrieved context + conversation history
              ↓
Groq LLM (llama-3.3-70b-versatile)
              ↓
Detailed, accurate answer generated
              ↓
Displayed in chat interface
```

---

## 🛠️ Tech Stack

```
LangChain          — RAG pipeline orchestration
FAISS              — Vector similarity search
HuggingFace        — Sentence embeddings (all-MiniLM-L6-v2)
Groq               — Ultra-fast LLM inference
Streamlit          — Chat UI frontend
HuggingFace Spaces — Free cloud deployment
Python             — Core language
```

---

## 📁 Project Structure

```
student-guidance-bot/
│
├── app.py                        — Streamlit chat UI
├── requirements.txt              — Python dependencies
├── .gitignore                    — Git ignore rules
│
├── data/
│   └── student_guidance.txt      — Knowledge base (custom content)
│
└── src/
    ├── __init__.py
    ├── vectorstore.py            — FAISS build + retrieval
    ├── llm.py                    — Groq LLM configuration
    └── rag_pipeline.py           — Core RAG logic + memory
```

---

## ⚙️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/student-guidance-bot.git
cd student-guidance-bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get free API key
```
Groq API Key (free): https://console.groq.com
```

### 4. Run the app
```bash
streamlit run app.py
```

### 5. Enter API key in sidebar and start chatting!

---

## 🔑 API Keys Required

| Key | Purpose | Get it here | Cost |
|---|---|---|---|
| `GROQ_API_KEY` | LLM inference | console.groq.com | Free |

---

## 💡 How RAG Works

```
Step 1 — Build Knowledge Base:
student_guidance.txt
        ↓
Split into 51 chunks (500 chars each)
        ↓
Convert to embeddings (HuggingFace)
        ↓
Store in FAISS vectorstore

Step 2 — Answer Questions:
Student question
        ↓
Convert to embedding
        ↓
Find top 4 similar chunks (semantic search)
        ↓
Pass chunks + question to Groq LLM
        ↓
LLM generates grounded answer
```

---

## 📚 Knowledge Base Coverage

```
✅ Learning Paths
   — Python (Beginner → Advanced)
   — AI/ML (Foundation → GenAI/LLM)
   — Data Science
   — DSA (Beginner → Advanced)
   — Web Development (Frontend + Backend)

✅ Placement Preparation
   — Resume writing tips
   — Coding round preparation
   — Technical interview preparation
   — System design interview
   — HR interview preparation
   — Salary negotiation tips

✅ Career Guidance
   — How to choose your domain
   — 6-month roadmap for freshers
   — What companies look for
   — Top hiring companies in India

✅ Course Recommendations
   — Free resources for every topic
   — Certifications worth getting
   — YouTube channels to follow

✅ Interview Q&A
   — Common Python questions with answers
   — Common ML questions with answers
   — Common AI/LLM questions with answers

✅ Placement Statistics
   — Interview process at Google, Microsoft, Amazon
   — Salary expectations for freshers
   — Tips to stand out
```

---

## 🎯 Sample Questions You Can Ask

```
"How should I start learning Python?"
"How do I prepare for coding interviews?"
"Should I choose AI/ML or Web Development?"
"How to write a good resume as a fresher?"
"What is the DSA roadmap?"
"Which companies hire freshers in India?"
"What is RAG and how does it work?"
"How do I prepare for system design interviews?"
"What are the best free resources for ML?"
"How to crack Google interview?"
```

---

## 🧠 Conversation Memory

```
Student: "How do I learn Python?"
Bot: "Start with basics — variables, loops..."

Student: "What resources did you mention?"
Bot: "I mentioned Corey Schafer YouTube,
      CS50P, and Python.org docs..."
      ↑
      Remembers previous conversation! ✅
```

---

## 📊 Performance

```
Knowledge Base : 51 semantic chunks
Embedding Model: sentence-transformers/all-MiniLM-L6-v2
LLM Model      : llama-3.3-70b-versatile (Groq)
Response Time  : 2-5 seconds
Availability   : 24/7 (Hugging Face Spaces)
Cost           : $0 (completely free)
```

---

## 🌐 Deployment

```
Platform  : Hugging Face Spaces (free tier)
Framework : Streamlit
URL       : https://huggingface.co/spaces/komaraprasad/student-guidance-bot
Status    : Live 24/7
```

---

## 📦 Requirements

```
langchain
langchain-community
langchain-groq
langchain-huggingface
langchain-text-splitters
faiss-cpu
sentence-transformers
streamlit
python-dotenv
```

---

## 🔮 Future Improvements

```
⏳ Add more knowledge base content
⏳ Support PDF upload for custom knowledge base
⏳ Add voice input/output
⏳ Multi-language support (Hindi, Telugu)
⏳ Analytics dashboard — most asked questions
⏳ Student progress tracking
⏳ Integration with Telegram/WhatsApp
```

---

## 🙋 Author

**Komara Prasad**
AI Engineer | LLM Systems | RAG Pipelines | Agentic AI

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)(www.linkedin.com/in/prasadkpk)]
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/Prasad-Goud-collab)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Live%20Demo-yellow)](https://huggingface.co/spaces/komaraprasad/student-guidance-bot)
