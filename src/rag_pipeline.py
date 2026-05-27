# src/rag_pipeline.py

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from src.vectorstore import StudentGuidanceVectorStore
from src.llm import get_llm


class StudentGuidanceRAG:
    """
    RAG pipeline for student guidance chatbot.
    Retrieves relevant context from knowledge base
    and generates answers using Groq LLM.
    """

    def __init__(self, groq_api_key: str):
        self.vectorstore = StudentGuidanceVectorStore()
        self.llm = get_llm(groq_api_key)
        self.chat_history = []

        # Build vectorstore from knowledge base
        self.vectorstore.build("data/student_guidance.txt")

    def ask(self, question: str) -> str:
        """
        Answers student question using RAG pipeline.

        Args:
            question (str): Student question

        Returns:
            str: Generated answer
        """
        # Step 1 — Retrieve relevant context
        context = self.vectorstore.retrieve(question, k=4)

        # Step 2 — Build conversation history string
        history_text = ""
        for msg in self.chat_history[-6:]:  # last 3 exchanges
            if isinstance(msg, HumanMessage):
                history_text += f"Student: {msg.content}\n"
            elif isinstance(msg, AIMessage):
                history_text += f"Assistant: {msg.content}\n"

        # Step 3 — Build prompt
        prompt = f"""You are an expert AI student counselor and career guidance assistant.
You help students with learning paths, placement preparation, interview tips, and career decisions.
Answer questions in a friendly, encouraging, and detailed way.
Use the provided context to give accurate and helpful answers.
If the answer is not in the context, use your general knowledge but mention it.

Previous Conversation:
{history_text if history_text else "No previous conversation."}

Knowledge Base Context:
{context}

Student Question: {question}

Answer (be helpful, specific, and encouraging):"""

        # Step 4 — Generate answer
        result = self.llm.invoke([HumanMessage(content=prompt)])
        answer = result.content

        # Step 5 — Update chat history
        self.chat_history.append(HumanMessage(content=question))
        self.chat_history.append(AIMessage(content=answer))

        return answer

    def clear_history(self):
        """Clears conversation history."""
        self.chat_history = []