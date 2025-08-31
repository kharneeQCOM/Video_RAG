from qgenie.integrations.langchain import QGenieEmbeddings,QGenieChat
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
memory= []

llm = QGenieChat(model="Turbo")
embedding = QGenieEmbeddings()
vector_store = Chroma(
    collection_name="transcript_dl",
    embedding_function=embedding,
    persist_directory="./chroma_langchain_db",
)

def retrieve_similar_docs(query, k=5):
    results = vector_store.similarity_search(query, k=k)
    return results

def prepare_source(docs):
    sources={}
    priority=[]
    for doc in docs:
        meta= doc.metadata
        if meta['video_name'] not in priority:
            priority.append(meta['video_name'])
        if sources.get(meta['video_name']) is None:
            sources[meta['video_name']]=[meta["start_time"], meta["end_time"]]
        else:
            sources[meta['video_name']][0]= min(sources[meta['video_name']][0], meta["start_time"])
            sources[meta['video_name']][1]= max(sources[meta['video_name']][1], meta["end_time"])
    return sources,priority

def rag_response(user_query):
    global memory
    similar_docs = retrieve_similar_docs(user_query, k=5)
    sources, priority = prepare_source(similar_docs)
    print("------------------------------------------------------------------------")
    print("SOURCES:")
    for p in priority:
        if sources.get(p):
            if(sources[p][1]-sources[p][0]<2):
                continue
            print(f"{p}: {sources[p][0]} to {sources[p][1]}")
    print("------------------------------------------------------------------------")
    memory_string= "\n".join(f"{mem.__class__.__name__}: {mem.content}" for mem in memory)
    context = "\n".join([doc.page_content for doc in similar_docs])
    prompt = f"Memory: {memory_string} Context: {context}\n\nQuestion: {user_query}\nAnswer:"
    print("response:")
    # response = llm.invoke(prompt)
    overall_response=""
    for chunk in llm.stream(prompt):
        overall_response+=chunk.content
        print(chunk.content, end='', flush=True)
    print("\n------------------------------------------------------------------------")
    memory+=[HumanMessage(user_query), AIMessage(overall_response)]
    return overall_response


if __name__ == "__main__":
    cur_messages = [SystemMessage(content="You are a helpful assistant, who has access to video transcripts. Use the context provided to answer the question.")]
    memory+=cur_messages
    while True:
        user_query = input("Enter your question (or 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break
        rag_response(user_query)