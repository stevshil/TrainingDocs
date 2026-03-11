#!/usr/bin/env python

# Generate embedings with DistilBert

# Import dependencies
import torch
import numpy as np
import matplotlib.pyplot as plt
from transformers import DistilBertTokenizer, DistilBertModel
from sklearn.metrics.pairwise import cosine_similarity

"""
Embeddings are numerical representations of text that capture semantic meaning. Each word or sentence is converted into a vector of numbers that represents its meaning in a high-dimensional space.
"""

# Load the tokenizer
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

# Sample customer support queries
queries = [
    "How do I reset my password?",
    "What are your business hours?",
    "Where is my order number 12345?",
    "The first 5 characters of the alphabet are ABCDE"
]

# Tokenize the queries
for query in queries:
    tokens = tokenizer.tokenize(query)

# Encode a query to get token IDs
# query = "How do I reset my password?"
query = "The first 5 characters of the alphabet are ABCDE" # Note this will tokenize ## for ABCDE as it is a sequence
encoded = tokenizer(query, return_tensors="pt", padding=True, truncation=True)
input_ids = encoded["input_ids"]
attention_mask = encoded["attention_mask"]

"""
Load the DistilBERT model and generate embeddings for our sample queries. We'll use the [CLS] token embedding as a representation of the entire sentence.
"""
# Load the DistilBERT model
model = DistilBertModel.from_pretrained("distilbert-base-uncased")
model.eval()  # Set to evaluation mode

# Function to generate embeddings
def get_embedding(text):
    encoded = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**encoded)
    # Use the [CLS] token embedding (first token) as the sentence embedding
    embedding = outputs.last_hidden_state[:, 0, :].numpy()
    return embedding

# Generate embeddings for all queries
embeddings = [get_embedding(query) for query in queries]

# Print shapes to confirm
for query, embedding in zip(queries, embeddings):
    print(f"Query: {query}")
    print(f"Embedding Shape: {embedding.shape}\n")

"""
Each embedding is a 768-dimensional vector. These dimensions capture different aspects of the text's meaning, learned during the model's training. Similar texts will have similar embeddings, which makes them useful for tasks like search and similarity comparison.

Each number is a learned feature capturing some aspect of the token’s meaning or context.
You can think of it as a coordinate in a 768‑dimensional semantic space.
"""