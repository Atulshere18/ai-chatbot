from fastapi import FastAPI, UploadFile, File, Form
from pdf_utils import extract_text_chunks
from fastapi.middleware.cors import CORSMiddleware
from embed_utils import embed_chunks, load_or_create_index, search_similar_chunks
from qa_utils import generate_answer
import shutil

app = FastAPI()

# Load or create index at startup
index, chunk_data = load_or_create_index()

# CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    print("🟡 Received file:", file.filename)

    with open("temp.pdf", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print("🟢 File saved. Starting extraction...")

    chunks = extract_text_chunks("temp.pdf")

    if not chunks:
        print("🔴 No chunks extracted.")
        return {"error": "No text extracted from PDF."}

    print(f"🟢 Extracted {len(chunks)} chunks. Starting embedding...")

    # Declare global before assigning
    global index, chunk_data
    index, chunk_data = embed_chunks(chunks)

    print("✅ Embedding completed.")
    return {"message": f"Uploaded and embedded {len(chunks)} chunks."}

@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    if index is None or chunk_data is None:
        return {"error": "Please upload a PDF first."}

    context = search_similar_chunks(question, index, chunk_data)
    answer = generate_answer(context, question)
    return {"answer": answer}
