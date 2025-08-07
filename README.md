AI PDF Question Answering App (No OpenAI)
This project is a full-stack web app that allows users to upload a PDF document and ask questions about its content through a simple chat interface. It uses local embeddings via Hugging Face's sentence-transformers and FAISS for fast similarity search, enabling context-aware answers without relying on APIs like OpenAI.
🎯 Project Goal
To demonstrate an end-to-end implementation of:
- File upload and processing
- Chunking and embedding generation using Hugging Face models
- Storing and querying vector embeddings using FAISS
- Retrieving relevant context to answer user queries
🔧 Tech Stack
Layer	Tech Used
Frontend	React.js, Axios
Backend	FastAPI
Embeddings	Hugging Face sentence-transformers
Vector DB	FAISS
PDF Reader	PyPDF2
Server	Uvicorn
📁 Folder Structure

project-root/
├── backend/
│   ├── main.py              # FastAPI app
│   ├── utils.py             # PDF parsing, chunking
│   ├── rag.py               # Embedding, FAISS logic
│   └── requirements.txt
├── frontend/
│   └── (React app files)
├── .gitignore
└── README.md

🖥️ Features

- Upload and parse large PDF documents (tested with 500+ pages)
- Convert document into text chunks
- Generate local embeddings using Hugging Face sentence-transformers
- Use FAISS for fast vector similarity search
- Ask natural language questions about the document
- No OpenAI or paid API dependencies

⚙️ Installation & Setup
🔹 1. Clone the repository

git clone https://github.com/your-username/pdf-question-answering.git
cd pdf-question-answering

🔹 2. Backend Setup

cd backend
pip install -r requirements.txt

📄 Sample requirements.txt

fastapi
uvicorn
PyPDF2
faiss-cpu
sentence-transformers

🔹 3. Start the FastAPI server

uvicorn main:app --reload

🔹 4. Frontend Setup (React)

cd frontend
npm install
npm start

🧠 How It Works

1. User uploads a PDF
2. PyPDF2 extracts and splits the text
3. Text chunks are embedded using Hugging Face's sentence-transformers model (e.g., all-MiniLM-L6-v2)
4. FAISS stores those embeddings for fast retrieval
5. On user query:
    - Query is embedded
    - FAISS finds similar chunks
    - Relevant content is returned as the answer

🧪 Sample Use Case

- Uploads: business_contract.pdf
- Asks: “What are the payment terms?”
- Output: System extracts and returns relevant contract clause

📌 To Improve (Ideas)

- [ ] Summarize long answers
- [ ] Add multi-turn conversation memory
- [ ] Add drag-and-drop PDF support
- [ ] User authentication & history

🙋 Author

Atul Manoj Shere
📧 atulshere18@gmail.com
🔗 GitHub: https://github.com/Atulshere18
🔗 LinkedIn: https://linkedin.com/in/atulshere18

