from app.services.embedding_service import generate_embedding

embedding = generate_embedding(
    "Akash is building an AI document intelligence platform"
)

print(len(embedding))
print(embedding[:10])

