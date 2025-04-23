from sentence_transformers import SentenceTransformer
import numpy as np

def embed_chunks(chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    return np.array(embeddings), model
