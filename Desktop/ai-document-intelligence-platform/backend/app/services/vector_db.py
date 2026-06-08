import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="documents"
)

def store_chunks(chunks):

    existing = collection.get()

    if existing["ids"]:
        collection.delete(
            ids=existing["ids"]
        )

    for index, chunk in enumerate(chunks):
        collection.add(
            ids=[str(index)],
            documents=[chunk]
        )

    print(f"{len(chunks)} chunks stored")