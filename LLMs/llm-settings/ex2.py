#!/usr/bin/env python

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# For demonstration, we'll use a small GPT-2 model
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
# GPT‑2 has no pad token → define one # Next line helps remove the attention_mask
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(model_name,
                                             pad_token_id=tokenizer.eos_token_id).to(device)
model.generation_config.pad_token_id = tokenizer.pad_token_id

model.eval()

"""
Experimenting with Temperature

Temperature controls the randomness of predictions. Lower values make outputs more deterministic and focused, while higher values increase creativity and randomness.
"""
def generate_with_temperature(prompt, temperature):
    # input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    # To remove the attention_mask warning set input_ids as below.  This is a fault in GPT2, not having different tokenizers.
    input_ids = tokenizer(
      prompt,
      return_tensors="pt",
      padding=True,
      truncation=True
    ).to(device)

    with torch.no_grad():
        output_ids = model.generate(
            # input_ids,
            # To remove the attention_mask warning
            **input_ids,
            max_length=60,
            do_sample=True,
            temperature=temperature,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

prompt = "Describe a futuristic city in one paragraph:"
for temp in [0.2, 0.7, 1.2]:
# for temp in [0.01, 0.5, 1.5]:  # Try these
    text = generate_with_temperature(prompt, temp)
    print(f"\nTemperature {temp}:\n{text}")

"""
**Expected Observations:**
- **Temperature 0.2**: More concise and consistent descriptions. The model is "safe" and less imaginative.
- **Temperature 0.7**: A balance of creativity and coherence with vibrant language.
- **Temperature 1.2**: Greater randomness with more whimsical or potentially nonsensical descriptions.

**Reflect:**
- How does the writing style change as temperature increases?
- Is the text more coherent at lower temperatures?

# Note: Temperature 0.0 often yields the most predictable outputs, while temperature 1.5 can produce imaginative or disjointed details.
"""