#!/usr/bin/env python

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# For demonstration, we'll use a small GPT-2 model
# Use https://huggingface.co/models to find other available models
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name,
                                             pad_token_id=tokenizer.eos_token_id).to(device)
model.generation_config.pad_token_id = tokenizer.pad_token_id

model.eval()

"""
Exploring Top-k Sampling

Top-k sampling limits the model to choosing from only the k most likely next tokens. This helps control the vocabulary diversity in generated text.
"""

def generate_with_top_k(prompt, top_k):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            max_length=60,
            do_sample=True,
            top_k=top_k,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

def version1():
  prompt = "Write a short poem about the ocean:"
  for k in [5, 50, 500]:
      text = generate_with_top_k(prompt, k)
      print(f"\nTop-k = {k}:\n{text}")

def generate_with_top_p(prompt, top_p):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            max_length=60,
            do_sample=True,
            top_p=top_p,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

def version2():
  prompt = "Provide suggestions for a healthy breakfast:"
  for p in [0.8, 0.9, 1.0]:
      text = generate_with_top_p(prompt, p)
      print(f"\nTop-p = {p}:\n{text}")

def generate_with_top_pk(prompt, top_p, top_k):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            max_length=60,
            do_sample=True,
            top_p=top_p,
            top_k=top_k,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

def version3():
  prompt = "Write a short poem about the ocean:"
  for p in [0.8, 0.9, 1.0]:
    for k in [5, 50, 500]:
      text = generate_with_top_pk(prompt, p, k)
      print(f"\nTop-p/k = {p}/{k}:\n{text}")

# version1()
# version2()
version3()

"""
**Expected Observations:**
- **Top-k = 5**: The poem might use simpler or more common words, potentially feeling repetitive.
- **Top-k = 50**: Usually a sweet spot for GPT-2, mixing variety and coherence.
- **Top-k = 500**: Allows GPT-2 to consider a wide vocabulary range, often producing unique but sometimes chaotic word choices.

**Reflect:**
- Does a low k value (e.g., 5) feel more limited in word choice?
- Does a high k value (e.g., 500) lead to more varied text?

Try adjusting the k value and combining it with different temperatures. For example, experiment with `(top_k=50, temperature=0.7)` or `(top_k=10, temperature=1.0)` and compare the poetic style or complexity.
"""