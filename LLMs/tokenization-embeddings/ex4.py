#!/usr/bin/env python

# Visualise embeddings

"""
Visualizing high-dimensional embeddings can help us understand how the model perceives text relationships. We'll use dimensionality reduction to plot our 768-dimensional embeddings in 2D space.

Reduce embeddings to 2D using PCA (Principal Component Analysis) and create a scatter plot. This allows us to see which queries the model considers similar.
"""

#!/usr/bin/env python

# Import dependencies
import torch
import numpy as np
import matplotlib.pyplot as plt
from transformers import DistilBertTokenizer, DistilBertModel
from sklearn.metrics.pairwise import cosine_similarity

"""
Tokenization converts text into tokens (e.g., words or subwords) that a model can process. Let's explore how DistilBERT's tokenizer handles customer support queries.

Load DistilBERT's tokenizer and tokenize sample customer support queries. Observe how the tokenizer breaks down each query into individual tokens.
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

"""
Next, let's convert tokens to numerical IDs. Models work with numbers, not text, so this conversion is essential. Examine the encoded output to understand what information is captured.
"""
# Encode a query to get token IDs
# query = "How do I reset my password?"
query = "The first 5 characters of the alphabet are ABCDE" # Note this will tokenize ## for ABCDE as it is a sequence, with ##de
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

from sklearn.decomposition import PCA

# Reduce embeddings to 2D
pca = PCA(n_components=2)
embeddings_2d = pca.fit_transform(np.vstack(embeddings))

# Plot the embeddings
plt.figure(figsize=(8, 6))
for i, query in enumerate(queries):
    plt.scatter(embeddings_2d[i, 0], embeddings_2d[i, 1], label=query)
    plt.text(embeddings_2d[i, 0] + 0.1, embeddings_2d[i, 1], query, fontsize=9)
plt.title("2D Visualization of Query Embeddings")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend()
plt.show()