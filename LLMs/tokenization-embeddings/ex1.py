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
    print(f"Query: {query}")
    print(f"Tokens: {tokens}\n")

"""
Next, let's convert tokens to numerical IDs. Models work with numbers, not text, so this conversion is essential. Examine the encoded output to understand what information is captured.
"""
# Encode a query to get token IDs
# query = "How do I reset my password?"
query = "The first 5 characters of the alphabet are ABCDE" # Note this will tokenize ## for ABCDE as it is a sequence, with ##de
encoded = tokenizer(query, return_tensors="pt", padding=True, truncation=True)
input_ids = encoded["input_ids"]
attention_mask = encoded["attention_mask"]

print(f"Query: {query}")
print(f"Input IDs: {input_ids}")
print(f"Attention Mask: {attention_mask}")