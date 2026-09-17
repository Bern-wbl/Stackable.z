import gradio as gr
from transformers import pipeline

chatbot = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", max_new_tokens=300)

def chat_fn(message, history):
    prompt = f"<|user|>\n{message}\n<|assistant|>\n"
    out = chatbot(prompt, max_new_tokens=300, do_sample=True, temperature=0.7)
    reply = out[0]['generated_text'][len(prompt):].split("<|user|>")[0].strip()
    return reply

demo = gr.ChatInterface(
    fn=chat_fn,
    title="Snackable.z 🍿",
    description="Snackable.z - Bite-sized AI answers. Built from Ghana 🇬🇭"
)
import os
demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 10000)))
