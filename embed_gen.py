from qgenie.integrations.langchain import QGenieEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import json


embedding = QGenieEmbeddings()
vector_store = Chroma(
    collection_name="transcript_dl",
    embedding_function=embedding,
    persist_directory="./chroma_langchain_db",
)
def json_to_store(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    # print(data)
    documents = []
    for key,val in data.items():
        segments= val
        for segment in segments:
            print(segment)
            doc = Document(page_content=segment["transcription"], metadata={"video_name":key, "start_time": segment["start_time"], "end_time": segment["end_time"]})
            documents.append(doc)
    vector_store.add_documents(documents)

json_to_store('trans_playlist.json')





# from langchain_chroma import Chroma
# from qgenie.integrations.langchain import QGenieEmbeddings

# # Load the persisted vector store
# embedding = QGenieEmbeddings()
# vector_store = Chroma(
#     collection_name="transcript_dl",
#     embedding_function=embedding,
#     persist_directory="./chroma_langchain_db",  # Adjust path if needed
# )

# # Perform a similarity search
# query = "explain computational graph"
# results = vector_store.similarity_search(query, k=5)
# print(results)
# results[0].p
