import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import pandas as pd

# Завантажуємо SentenceTransformer
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def load_dataset(dataset_path):
    """Завантажуємо датасет коктейлів"""
    df = pd.read_csv(dataset_path)
    if not {"name", "ingredients"}.issubset(df.columns):
        raise ValueError("No columns 'name' or 'ingredients'")
    df["embedding_text"] = df["name"] + " " + df["ingredients"]
    return df


def create_faiss_index(df):
    """Creating FAISS-index for cocktail search"""
    embeddings = embedding_model.encode(df["embedding_text"].tolist(), show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")

    embedding_dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(embedding_dim)
    index.add(embeddings)

    return index, embeddings


def search_similar_cocktails(query, index, df, top_k=5):
    """Searching for similar cocktails"""
    query_embedding = embedding_model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, top_k)
    return [df.iloc[idx]["name"] for idx in indices[0]]