#!/usr/bin/env python

# Apply embbedings - test similarity

# Import dependencies
import torch
import numpy as np
import matplotlib.pyplot as plt
from transformers import DistilBertTokenizer, DistilBertModel
from sklearn.metrics.pairwise import cosine_similarity

"""
Now let's put embeddings to work by computing similarity between queries. This is a common use case in customer support systems for matching user questions to existing FAQs.
"""

# Load the tokenizer
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

# Sample customer support queries
queries = [
    "How do I reset my password?",
    "What are your business hours?",
    "Where is my order number 12345?",
    "The first 5 characters of the alphabet are ABCDE",
    "How are you today?"
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

# Function to generate embeddings, replaced to get better similarity readings
def get_embedding(text):
    encoded = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**encoded)

    hidden = outputs.last_hidden_state          # (1, seq_len, 768)
    mask = encoded['attention_mask'].unsqueeze(-1)  # (1, seq_len, 1)

    # Masked mean pooling
    masked_hidden = hidden * mask
    summed = masked_hidden.sum(dim=1)
    counts = mask.sum(dim=1)
    embedding = (summed / counts).numpy()       # (1, 768)

    return embedding


# Generate embeddings for all queries
embeddings = [get_embedding(query) for query in queries]

"""
Calculate cosine similarity scores between query embeddings. Cosine similarity measures how similar two vectors are, with scores ranging from -1 (opposite) to 1 (identical).
"""

# Compute cosine similarity between embeddings
similarity_matrix = cosine_similarity(
    np.vstack(embeddings)  # yields shape (N, 768)
)
# Display the similarity matrix
for i, query1 in enumerate(queries):
    for j, query2 in enumerate(queries):
        if i < j:  # Avoid duplicates
            print(f"Similarity between '{query1}' and '{query2}': {similarity_matrix[i][j]:.4f}")

# Generate embeddings for all queries
embeddings = [get_embedding(query) for query in queries]

"""
Calculate cosine similarity scores between query embeddings. Cosine similarity measures how similar two vectors are, with scores ranging from -1 (opposite) to 1 (identical).
"""

# Compute cosine similarity between embeddings
similarity_matrix = cosine_similarity(
    np.vstack(embeddings)  # yields shape (N, 768)
)
# Display the similarity matrix
for i, query1 in enumerate(queries):
    for j, query2 in enumerate(queries):
        if i < j:  # Avoid duplicates
            print(f"Similarity between '{query1}' and '{query2}': {similarity_matrix[i][j]:.4f}")

"""
Examine the similarity scores. Queries with higher scores are more semantically similar. In a real customer support system, you could use these scores to match incoming questions to the most relevant FAQ or support article.

These ranges are widely used in semantic search and intent detection:

0.85 - 1.00 — Very similar meaning  
Often paraphrases or nearly identical intent.

0.70 - 0.85 — Clearly related  
Same topic or intent, but not identical wording.

0.50 - 0.70 — Somewhat related  
Shares concepts but not the same question or purpose.

0.30 - 0.50 — Weakly related  
Might share a few words but not meaningfully similar.

0.00 - 0.30 — Unrelated  
No meaningful semantic overlap.

Negative values — Opposing direction in vector space  
Rare in practice with modern embeddings; usually indicates noise or very different contexts.

These are guidelines, not strict rules. Different models produce slightly different distributions.

For better sentence similarities look at;
- sentence-transformers/all-MiniLM-L6-v2
- sentence-transformers/all-distilroberta-v1
- sentence-transformers/paraphrase-MiniLM-L12-v2
"""