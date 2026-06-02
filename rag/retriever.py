from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load once when server starts
embedding_model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

def retrieve(question,
             chunks,
             embeddings,
             top_k=5):

    # Convert question to embedding
    query_embedding = embedding_model.encode(
        question
    )

    similarities = cosine_similarity(
        [query_embedding],
        embeddings
    )[0]

    top_indices = np.argsort(
        similarities
    )[-top_k:][::-1]

    results = []

    for idx in top_indices:
        results.append(
            chunks[idx]
        )

    return results