RAG Audio Q&A Application

This is a Retrieval-Augmented Generation (RAG) application that allows users to upload an audio file, ask a question, and receive a text-based answer. The system uses Whisper for transcribing audio, SentenceTransformers for creating vector embeddings, and FAISS for fast retrieval of relevant text chunks. The answer is then generated using GPT.

Make sure you have the following installed:

Python 3.7+ (Recommended version: 3.8 or 3.9)

Git (for version control)

FFmpeg (required for audio processing)

FFmpeg Installation:
Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```


macOS (using Homebrew):

```bash
brew install ffmpeg
```
Windows: Download FFmpeg from ffmpeg.org and follow installation instructions.

⚙️ Setup
1. Clone the Repository
First, clone the repository to your local machine:

```bash

git clone https://github.com/yourusername/RAG-Audio-QA.git
cd RAG-Audio-QA
```


2. Create a Virtual Environment
Create a virtual environment to manage dependencies:

```bash

python3 -m venv venv
```

Activate the virtual environment:

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

3. Install Dependencies
Install the required Python libraries:

```bash
pip install -r requirements.txt
```

🚀 Running the Application
1. Set Flask App Environment Variable

Set the FLASK_APP environment variable to your main Flask app:

Linux/macOS:

```bash
export FLASK_APP=app.py
```

Windows:

```bash

set FLASK_APP=app.py
```

2. Run the Application

Start the Flask development server:

```bash
flask run
```

This should output something like:

```bash

 * Running on http://127.0.0.1:5000
 ```

 3. Open in Browser
Open your web browser and go to http://127.0.0.1:5000 to interact with the application.

4. Upload Audio & Ask a Question
Upload an audio file (e.g., .mp3, .wav).

Type a question related to the content of the audio.

Click Submit, and the app will return an answer based on the transcribed text.

📂 Folder Structure
Here's an overview of the folder structure:

```bash
RAG-Audio-QA/
├── .gitignore                  # Git ignore file
├── app.py                      # Main Flask app entry point
├── requirements.txt            # All Python dependencies
├── audio_processing/           # Audio transcription related files
│   ├── transcriber.py
├── text_processing/            # Text chunking and embedding
│   ├── chunker.py
│   ├── embedder.py
├── retrieval/                  # FAISS for efficient retrieval
│   ├── retriever.py
├── generation/                 # Answer generation (using GPT)
│   ├── qa_generator.py
├── static/                     # Static files (CSS, JS, images)
│   ├── style.css
├── templates/                  # HTML files for the frontend
│   ├── index.html
├── venv/                       # Virtual environment (ignored by Git)
└── README.md                   # Documentation (this file)
```


🧑‍💻 Git Ignore
The .gitignore file will ignore unnecessary files like:

Virtual environments (venv/)

Large model files (*.pt, *.h5, etc.)

System-specific files (.DS_Store, Thumbs.db)

Logs, temporary files, and more.

Here's a quick view of what the .gitignore excludes:


```bash
# Python
*.pyc
*.pyo
*.pyd
__pycache__/
venv/
*.egg-info/

# Flask
instance/
*.db
*.sqlite

# Virtual Environment
venv/
env/
ENV/
*.env

# Model files (large files)
*.h5
*.bin
*.pt
*.ckpt
*.model

# Temporary files
*.log
*.tmp
*.swp

# System-specific files
.DS_Store
Thumbs.db
```