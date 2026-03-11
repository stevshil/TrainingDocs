#!/usr/bin/env python

"""
Generate embeddings for individual tokens within a query and analyze their similarity. This will help you understand how the model represents individual words in context.
"""

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
    print(f"Query: {query}")
    print(f"Tokens: {tokens}\n")

# Choose a query
query = "How do I reset my password?"
"""
Load the DistilBERT model and generate embeddings for our sample queries. We'll use the [CLS] token embedding as a representation of the entire sentence.
"""
# Load the DistilBERT model
model = DistilBertModel.from_pretrained("distilbert-base-uncased")
model.eval()  # Set to evaluation mode


# Tokenize and get embeddings for each token
encoded = tokenizer(query, return_tensors="pt", padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**encoded)
token_embeddings = outputs.last_hidden_state[0].numpy()  # Shape: (num_tokens, 768)

# Get tokens (excluding [CLS] and [SEP])
tokens = tokenizer.convert_ids_to_tokens(encoded["input_ids"][0])[1:-1]
print(f"Tokens: {tokens}")

# Compute similarity between "reset" and "password"
reset_idx = tokens.index("reset")
password_idx = tokens.index("password")
reset_embedding = token_embeddings[reset_idx]
password_embedding = token_embeddings[password_idx]
token_similarity = cosine_similarity([reset_embedding], [password_embedding])[0][0]

print(f"\nSimilarity between 'reset' and 'password': {token_similarity:.4f}")

# Analyze the result
print("\nAnalysis:")
if token_similarity > 0.5:
    print("These tokens are moderately similar, possibly due to related context.")
else:
    print("These tokens are not very similar, indicating distinct meanings.")


"""
The similarity between individual tokens reveals their semantic relationship in this context. Word-level embeddings can be useful for tasks like keyword extraction, named entity recognition, or identifying important terms in user queries.
"""