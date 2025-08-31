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
### 1. Transcribe Videos
Run `Whisper_Run.ipynb` to process videos, generate transcripts.

### 2. Generate Embeddings and save to Chroma DB
Run `embeg_gen.py` to process  transcripts to generate embeddings and save to DB.

### 3. Interact with the RAG Agent
The `rag_agent.py` script contains the logic for the RAG agent. You can interact with it to query your video content.

### File Structure
-   `Whisper_Run.ipynb`: Jupyter notebook for video transcription.
-   `embed_gen.py`: Script responsible for generating embeddings from transcript.
-   `rag_agent.py`: Main script for the Retrieval Augmented Generation agent.
-   `trans_playlist.json`: Stores information about transcribed videos or playlists.

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

## Sample chat
------------------------------------------------------------------------
Enter your question (or 'exit' to quit): explain transformers encoder alone                                     
------------------------------------------------------------------------
SOURCES:
Transformers and Self-Attention (DL 19): 120 to 1050
------------------------------------------------------------------------
response:


Let's break down the transformer encoder alone.

The transformer encoder is a neural network architecture that takes in a sequence of words, such as a sentence or a document, and produces a sequence of vectors that represent the meaning of the input.

Here's how it works:

1. The input sequence of words is first embedded into a matrix of word embeddings, where each row is the embedding of a different word.
2. The matrix of word embeddings is then passed through a series of self-attention blocks, which compute the attention weights for each word in the input sequence, based on the similarity between the word and all the other words in the sequence.
3. The self-attention mechanism allows the model to focus on the most relevant words when generating the output.
4. The output of the self-attention mechanism is then passed through a feed-forward network (FFN), which is a fully connected neural network that takes the output of the self-attention mechanism and produces a new vector that represents the meaning of the input sequence.
5. The output of the FFN is then passed through another self-attention block, which computes the attention weights for each word in the output sequence.
6. The final output of the transformer encoder is a sequence of vectors that represent the meaning of the input sequence.

The key innovation of the transformer encoder is the use of self-attention mechanisms, which allow the model to capture long-range dependencies between words in the input sequence. This is particularly useful for tasks like machine translation, where the model needs to capture the meaning of the entire sentence to generate the correct translation.

In the example shown, the transformer encoder is trained on a document in English, and it produces an encoding of the document that captures the meaning of the sentence. This encoding can then be used as input to another neural network to generate the translation of the sentence into another language.
------------------------------------------------------------------------
Enter your question (or 'exit' to quit):

