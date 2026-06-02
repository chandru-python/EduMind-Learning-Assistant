from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM
import torch

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

print("=" * 50)
print("Loading TinyLlama...")
print("=" * 50)

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

llm = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32,
    device_map="cpu"
)

print("=" * 50)
print("TinyLlama Loaded Successfully")
print("=" * 50)


def generate_answer(question, retrieved_chunks):

    print("Building Context...")

    context = "\n\n".join(
        [str(chunk) for chunk in retrieved_chunks[:3]]
    )

    prompt = f"""
You are an expert educational tutor.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}

Provide a clear and concise answer.
"""

    print("Tokenizing...")

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )

    print("Generating Answer...")

    with torch.no_grad():

        outputs = llm.generate(
            **inputs,
            max_new_tokens=120,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )

    generated_text = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    # Remove prompt from output
    answer = generated_text.replace(
        prompt,
        ""
    ).strip()

    # Fallback
    if len(answer) < 10:
        answer = "Answer could not be generated from the available context."

    print("Generation Complete")

    return answer