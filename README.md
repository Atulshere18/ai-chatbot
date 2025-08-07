
---

```md
# 🧠 AI PDF Question Answering App (No OpenAI)

This project is a full-stack web app that allows users to upload a PDF document and ask questions about its content through a simple chat interface. It uses local embeddings via Hugging Face's `sentence-transformers` and FAISS for fast similarity search, enabling context-aware answers **without relying on OpenAI or any paid APIs**.

---

## 🎯 Project Goal

To demonstrate an end-to-end implementation of:

- 📄 File upload and processing  
- ✂️ Chunking and embedding generation using Hugging Face models  
- 🧠 Storing and querying vector embeddings using FAISS  
- 💬 Retrieving relevant context to answer user queries

---

## 🔧 Tech Stack

| Layer     | Tech Used                         |
|-----------|-----------------------------------|
| Frontend  | React.js, Axios                   |
| Backend   | FastAPI                           |
| Embeddings| Hugging Face `sentence-transformers` |
| Vector DB | FAISS                             |
| PDF Reader| PyPDF2                            |
| Server    | Uvicorn                           |

---

## 📁 Folder Structure

```

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

````

---

## 🖥️ Features

- ✅ Upload and parse large PDF documents (tested with 500+ pages)
- ✅ Convert document into manageable text chunks
- ✅ Generate local embeddings using Hugging Face models
- ✅ Store and retrieve embeddings using FAISS
- ✅ Ask natural language questions about the PDF content
- ✅ No OpenAI or third-party APIs needed

---

## ⚙️ Installation & Setup

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-question-answering.git
cd pdf-question-answering
````

### 🔹 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

#### 📄 Sample `requirements.txt`

```
fastapi
uvicorn
PyPDF2
faiss-cpu
sentence-transformers
```

### 🔹 3. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

### 🔹 4. Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```

---

## 🧠 How It Works

1. 📤 User uploads a PDF
2. 🧾 PyPDF2 extracts and splits the text
3. 🔢 Text chunks are embedded using Hugging Face model (e.g., `all-MiniLM-L6-v2`)
4. 🧲 FAISS stores those embeddings
5. ❓ On user query:

   * Embeds the query
   * Searches similar chunks via FAISS
   * Returns the best-matching context as the answer

---

## 🧪 Sample Use Case

* **Upload:** `business_contract.pdf`
* **Query:** “What are the payment terms?”
* **Response:** System extracts and returns the relevant clause from the document.

---

## 📌 Future Improvements (Ideas)

* [ ] Summarize long answers
* [ ] Add multi-turn conversation memory
* [ ] Add drag-and-drop PDF support
* [ ] Implement user authentication & chat history

---

## 🙋 Author

**Atul Manoj Shere**
📧 [atulshere18@gmail.com](mailto:atulshere18@gmail.com)
🔗 [GitHub](https://github.com/Atulshere18)
🔗 [LinkedIn](https://linkedin.com/in/atulshere18)

```
