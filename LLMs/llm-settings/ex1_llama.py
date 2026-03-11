#!/usr/bin/env python

import torch, os
from transformers import AutoModelForCausalLM, AutoTokenizer
from dotenv import load_dotenv

# Requires login to Hugging face before use
# huggingface-cli login

load_dotenv('lab.env')
hf_token = os.getenv("HF_TOKEN")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Choose a Llama 3 model
# model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
model_name = "LiquidAI/LFM2-2.6B"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    token=hf_token,
    trust_remote_code=True        # Required for Llama 3
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    token=hf_token,
    trust_remote_code=True,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)

# Llama models need pad_token_id = eos_token_id
tokenizer.pad_token = tokenizer.eos_token
model.generation_config.pad_token_id = tokenizer.eos_token_id

model.eval()

prompt = "Explain how quantum computers differ from classical computers:"
input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

with torch.no_grad():
    output_ids = model.generate(
        input_ids,
        max_length=200,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id
    )

generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(generated_text)
