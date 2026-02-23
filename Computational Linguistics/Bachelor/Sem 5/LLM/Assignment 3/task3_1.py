from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the small GPT-2 model and tokenizer
model_name = "openai-community/gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Input text
text = "Hi What's your name?"
inputs = tokenizer(text, return_tensors="pt")

# Get model output (logits)
with torch.no_grad():
    outputs = model(**inputs)
    next_token_logits = outputs.logits[0, -1, :]  # logits for next token

# Convert logits to log probabilities
log_probs = torch.log_softmax(next_token_logits, dim=-1)

# Get top 5 tokens and their log probabilities
top_log_probs, top_token_ids = torch.topk(log_probs, 5)

top_tokens = []
for token_id in top_token_ids:
    token = tokenizer.decode([token_id])
    top_tokens.append(token)

print("top 5 tokens: ", top_tokens)
print("top token ids: ", top_token_ids)
print("top log probs: ", top_log_probs)