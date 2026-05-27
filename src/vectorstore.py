# src/vectorstore.py

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


class StudentGuidanceVectorStore:
    """
    Loads student guidance text file,
    chunks it and builds FAISS vectorstore.
    """

    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vectorstore = None

    def build(self, file_path: str) -> None:
        """
        Loads text file, chunks and builds FAISS vectorstore.

        Args:
            file_path (str): Path to student_guidance.txt
        """
        # Load text file
        loader = TextLoader(file_path, encoding="utf-8")
        documents = loader.load()

        # Chunk documents
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=["\n\n", "\n", ".", " "]
        )
        chunks = splitter.split_documents(documents)
        print(f"✅ Created {len(chunks)} chunks from knowledge base.")

        # Build FAISS vectorstore
        self.vectorstore = FAISS.from_documents(chunks, self.embeddings)
        print("✅ FAISS vectorstore built successfully.")

    def retrieve(self, query: str, k: int = 4) -> str:
        """
        Retrieves top-k relevant chunks for the query.

        Args:
            query (str): Student question
            k (int): Number of chunks to retrieve

        Returns:
            str: Combined context from retrieved chunks
        """
        if not self.vectorstore:
            raise RuntimeError("Vectorstore not built.")

        docs = self.vectorstore.similarity_search(query, k=k)
        context = "\n\n".join([doc.page_content for doc in docs])
        return context

    def is_ready(self) -> bool:
        return self.vectorstore is not None