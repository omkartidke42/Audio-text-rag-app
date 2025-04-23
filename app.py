from flask import Flask, render_template, request
import os
from audio_processing.transcriber import transcribe_audio
from text_processing.chunker import chunk_text
from text_processing.embedder import embed_chunks
from retrieval.retriever import build_faiss_index, retrieve_relevant_chunks
from generation.qa_generator import generate_answer

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        audio_file = request.files["audio"]
        question = request.form["question"]

        if audio_file:
            file_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
            audio_file.save(file_path)

            transcript = transcribe_audio(file_path)
            chunks = chunk_text(transcript)
            embeddings, embed_model = embed_chunks(chunks)
            index = build_faiss_index(embeddings)
            context = retrieve_relevant_chunks(question, chunks, index, embed_model)
            answer = generate_answer(question, context)

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
