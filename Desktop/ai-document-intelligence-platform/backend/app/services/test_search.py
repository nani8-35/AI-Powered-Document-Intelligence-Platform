from app.services.vector_db import collection

results = collection.query(
    query_texts=["What are the mathematics marks?"],
    n_results=3
)

print(results["documents"])