#!/usr/bin/env python

"""
Tokenize a longer, more complex query and analyze how the tokenizer handles it. Pay attention to subword tokens and the total token count.
"""

# Import dependencies
import torch
import numpy as np
import matplotlib.pyplot as plt
from transformers import DistilBertTokenizer, DistilBertModel
from sklearn.metrics.pairwise import cosine_similarity

# Complex query
complex_query = "I need help resetting my password because I forgot my email address."

# Load the tokenizer
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

# Tokenize
tokens = tokenizer.tokenize(complex_query)
print(f"Complex Query: {complex_query}")
print(f"Tokens: {tokens}")

# Analyze the tokens
print("\nAnalysis:")
special_tokens = [token for token in tokens if token.startswith("##")]
print(f"Subword tokens (with ##): {special_tokens}")
print(f"Total token count: {len(tokens)}")

"""
Notice how DistilBERT handles longer, more complex text. You'll see more subword tokens (those with "##" prefix) as the tokenizer breaks down less common words. This approach helps the model handle vocabulary it hasn't seen before.
"""