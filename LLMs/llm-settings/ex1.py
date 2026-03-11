#!/usr/bin/env python

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# For demonstration, we'll use a small GPT-2 model
# Other models GPT-J-6B, GPT-NeoX-20B, gpt-medium(large|xl)
# Llama2 and 3, Mistral 7B, Mixtral, Zephyr, StarCoder(2), CodeGen, CodeParrot
# Bloom, Bloomz, Falcon-7B/40B, OPT, hf‑tiny‑random‑GPT2LMHeadModel, DistilGPT‑2
# model_name = "gpt2"
# model_name="EleutherAI/gpt-neo-1.3B" # Reasonable Download
model_name="mistralai/Mistral-7B-v0.1" # This is a big download
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name,pad_token_id=tokenizer.eos_token_id).to(device)
model.generation_config.pad_token_id = tokenizer.pad_token_id

model.eval()

"""
Generating Text with Default Settings

Let's start by generating text with the default settings to establish a baseline for comparison.
"""

prompt = "Explain how quantum computers differ from classical computers:"
input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
pad_token_id = tokenizer.pad_token_id


# Generate text with default settings
with torch.no_grad():
    output_ids = model.generate(
        input_ids,
        # max_length=50,
        max_length=100,
        do_sample=True,  # Enables sampling for more varied outputs
        pad_token_id=tokenizer.eos_token_id
    )

generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(generated_text)

"""
Note increasing max_length will provide more text, but you may also get a different answer everytime you run the code, even with the same length.

Torch and transforms do the on the fly LLM.
https://medium.com/@rajratangulab.more/pytorch-for-llms-and-transformers-a-complete-guide-with-hugging-face-9eefb2af4b08
"""