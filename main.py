import sys
from audio_processing.transcriber import transcribe_audio
from text_processing.chunker import chunk_text
from text_processing.embedder import embed_chunks
from retrieval.retriever import build_faiss_index, retrieve_relevant_chunks
from generation.qa_generator import generate_answer

def main(audio_path, query):
    print("🔊 Transcribing audio...")
    transcript = transcribe_audio(audio_path)

    print("🧩 Chunking transcript...")
    chunks = chunk_text(transcript)

    print("📌 Embedding chunks...")
    embeddings, embed_model = embed_chunks(chunks)

    print("🔍 Building index...")
    index = build_faiss_index(embeddings)

    print("🤔 Retrieving relevant chunks...")
    context = retrieve_relevant_chunks(query, chunks, index, embed_model)

    print("✍️ Generating answer...")
    answer = generate_answer(query, context)
    print("\n💬 Answer:", answer)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])