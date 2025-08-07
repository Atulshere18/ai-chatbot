import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def embed_chunks(chunks):
    if not chunks:
        raise ValueError("No chunks to embed.")
    
    embeddings = model.encode(chunks)

    # Create FAISS index
    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(np.array(embeddings))

    # Save index and chunks
    faiss.write_index(index, "index.faiss")
    with open("chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    return index, chunks

def load_or_create_index():
    try:
        index = faiss.read_index("index.faiss")
        with open("chunks.pkl", "rb") as f:
            chunks = pickle.load(f)
        return index, chunks
    except:
        return None, None

def search_similar_chunks(query, index, chunks, top_k=3):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), top_k)
    return " ".join([chunks[i] for i in I[0]])
