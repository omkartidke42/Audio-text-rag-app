import faiss
import numpy as np

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def retrieve_relevant_chunks(query, chunks, index, embed_model, k=3):
    query_vector = embed_model.encode([query])
    D, I = index.search(np.array(query_vector), k)
    return "\n".join([chunks[i] for i in I[0]])
