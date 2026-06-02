import pickle

def load_chunks():

    with open("chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    return chunks


def load_embeddings():

    with open("embeddings.pkl", "rb") as f:
        embeddings = pickle.load(f)

    return embeddings