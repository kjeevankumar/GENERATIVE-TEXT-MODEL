from transformers import pipeline

# Load GPT-2 text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Prompt input
prompt = "Once upon a time in a world powered by artificial intelligence,"

# Generate output
results = generator(prompt, max_length=100, num_return_sequences=1)

# Print the result
print("📝 Generated Text:\n")
print(results[0]['generated_text'])
