# Video RAG System

## Project Description
This repository contains a system designed for Retrieval Augmented Generation (RAG) on video content. It leverages OpenAI's Whisper for transcribing audio from videos, generates embeddings from the transcribed text, and stores them in a ChromaDB vector store. A RAG agent then uses this data to answer queries related to the video content.

## Features
-   **Video Transcription**: Utilizes OpenAI Whisper to convert video audio into text transcripts.
-   **Embedding Generation**: Creates vector embeddings from transcriptions for efficient retrieval.
-   **Vector Database**: Employs ChromaDB to store and manage embeddings, integrated with LangChain.
-   **Retrieval Augmented Generation**: Answers user queries by retrieving relevant video segments and generating coherent responses.

## Installation
To set up the project, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/video_rag.git
    cd video_rag
    ```

2.  **Create a virtual environment** (recommended):
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt # (You may need to create this file)
    ```
    *Note: Ensure you have `pytorch` installed with the appropriate CUDA version if you plan to use GPU for Whisper. Refer to the PyTorch documentation for details.*

    ```
4.  **Install qgenie-sdk**:
    ```
    pip install qgenie-sdk -i https://devpi.qualcomm.com/qcom/dev/+simple --trusted-host devpi.qualcomm.com
    ```

5.  **Set api token**:
     $env:QGENIE_API_KEY=your_token

## Usage
### 1. Transcribe Videos and Generate Embeddings
Run `Whisper_Run.ipynb` to process videos, generate transcripts, and create embeddings stored in `chroma_langchain_db/`.

### 2. Interact with the RAG Agent
The `rag_agent.py` script contains the logic for the RAG agent. You can interact with it to query your video content.

### File Structure
-   `Whisper_Run.ipynb`: Jupyter notebook for video transcription and embedding generation.
-   `embed_gen.py`: Script responsible for generating embeddings.
-   `rag_agent.py`: Main script for the Retrieval Augmented Generation agent.
-   `trans_playlist.json`: Stores information about transcribed videos or playlists.
-   `chroma_langchain_db/`: Directory containing the ChromaDB vector store.
-   `rag/`: Additional modules or scripts related to the RAG implementation.

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

