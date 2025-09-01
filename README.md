# AI Buzz Phase 2 Submission

## Idea Details
- Team Name: Video RAG
- Idea Title: Video Retrieval Augmented Generation (RAG) System
- Idea url: <!-- Link to your idea in AI Buzz portal - Please fill this in as needed -->
- Team Members
  - <!-- Member 1 -->
  - <!-- Member 2 -->
- Programming language used: Python
- AI Hub Model links
  - <!-- link 1 - Please fill this in as needed -->
  - <!-- link 2 - Please fill this in as needed -->
- Target device
  - [x] PC
  - [ ] Mobile
  - [ ] Others: <!-- Specify the device --> 


## Implementation Summary
This project implements a Retrieval Augmented Generation (RAG) system for video content. It utilizes Hugging Face's Whisper to transcribe audio from videos, generates embeddings from these transcriptions, and stores them in a ChromaDB vector store. A RAG agent then uses this data to answer user queries related to the video content, leveraging the QGenie API.

### Navigation and Key Files:
-   `Whisper_Run.ipynb`: This Jupyter notebook is used solely for transcribing audio from videos using Whisper. The generated transcripts are then used by `embed_gen.py` to create embeddings.
-   `embed_gen.py`: Contains the core logic for generating vector embeddings from textual data.
-   `rag_agent.py`: Implements the RAG agent, responsible for querying the ChromaDB and formulating responses based on retrieved video content.
-   `trans_playlist.json`: Stores metadata or processed information about transcribed videos or playlists.
-   `chroma_langchain_db/`: This directory houses the ChromaDB vector store, where all the generated embeddings are persistently stored.
-   `rag/`: This directory might contain additional modules, utility scripts, or components specific to the RAG implementation.

### Limitations:
-   Current implementation focuses on local processing and may require significant computational resources for large video datasets.
-   Relies on OpenAI Whisper, which might have rate limits or cost implications for heavy usage.

### Future Scope:
-   Integration with various video sources (e.g., YouTube API, local video files).
-   Enhancement of the RAG agent for more complex query understanding and response generation.
-   Optimization for performance and scalability.
-   Development of a user interface for easier interaction.

## Installation & Setup steps
To set up and run the project, follow these detailed steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/video_rag.git # Replace with actual repo URL
    cd video_rag
    ```

2.  **Create a virtual environment** (highly recommended):
    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```
    pip install -r requirements.txt
    ```

4.  **Set up environment variables**:

    For Windows PowerShell, you can set the environment variable directly:
    ```powershell
    $env:QGENIE_API_KEY="your_qgenie_api_key_here"
    ```

5.  **Generate Embeddings and Database**:
    After setting up the environment variables and transcribing videos using `Whisper_Run.ipynb`, run `embed_gen.py` to process the transcripts and generate embeddings, storing them in the ChromaDB:
    ```
    python embed_gen.py
    ```

6.  **Run RAG Agent**:
    Once the embeddings are generated, you can start the RAG agent to query the video content:
    ```
    python rag_agent.py
    ```

## Expected output / behaviour
The system is designed to provide intelligent answers to queries related to video content.

### Workflow:
1.  **Video Processing**:
    -   `Whisper_Run.ipynb` is executed to transcribe the audio from specified videos, generating raw transcripts.
    -   `embed_gen.py` then takes these transcripts, generates text chunks and their corresponding embeddings, and stores these embeddings in the `chroma_langchain_db/` directory.
    -   You should see progress outputs during transcription and embedding generation.
2.  **Querying**: Once embeddings are generated, `rag_agent.py` can be used to query the video content.
    -   Provide a natural language question.
    -   The agent will retrieve relevant text segments from the ChromaDB.
    -   It will then use an LLM (via LangChain) to synthesize a coherent answer based on the retrieved information.
    -   The expected output is a concise answer to your question, derived directly from the video content.

### Validation:
-   To validate, run `Whisper_Run.ipynb` on a small video.
-   After successful completion, run `rag_agent.py` and ask questions directly related to the content of the video you processed.
-   The responses should be accurate and contextually relevant to the video.

## Any additional steps required for running
- [ ] NA
<!-- 
Mention any additional requirements here. If not, leave the NA.
-->

## Submission Checklist
- [ ] Recorded video
- [x] Readme updated with required fields
- [x] Dependency installation scripts added
- [x] Startup script added
- [ ] Idea url updated in Readme
