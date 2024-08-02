from pinecone import Pinecone, ServerlessSpec


pc = Pinecone(api_key="b452bfeb-70f3-4f8a-8c14-3bf3b50405ce")

# Create the index
pc.create_index(
    name="newin",
    dimension=6, 
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)


index = pc.Index("newin")


query_vector = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]


vectors = [
    {"id": "project1", "values": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0], "metadata": {"client": "A", "budget": 200}},
    {"id": "person2", "values": [11.0, 22.0, 33.0, 44.0, 55.0, 66.0], "metadata": {"client": "B", "budget": 100}},
    {"id": "person3", "values": [1.0, 22.0, 3.0, 44.0, 5.0, 66.0], "metadata": {"client": "B", "budget": 100}}
]


index.upsert(vectors)


f = index.query(vector=query_vector, top_k=1, include_metadata=True)


for match in f["matches"]:
    print(f"ID: {match['id']}, Score: {match['score']}, Metadata: {match['metadata']}")
