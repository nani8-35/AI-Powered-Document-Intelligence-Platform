from app.services.vector_db import collection

def retrieve_context(question):
    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    return "\n".join(results["documents"][0])
