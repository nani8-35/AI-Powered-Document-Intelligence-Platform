from app.services.vector_db import collection

print("Count:", collection.count())

results = collection.get()

print("\nDocuments:\n")

for doc in results["documents"][:5]:
    print(doc[:200])
    print("-" * 50)

    print("PDF Uploaded:", file.filename)

text = extract_text_from_pdf(file_path)
print("Text Length:", len(text))

chunks = chunk_text(text)
print("Chunks Created:", len(chunks))

store_chunks(chunks)
print("Stored In ChromaDB")