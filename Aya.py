import tkinter as tk
import json
import requests
from tkinter import scrolledtext

# Load or initialize chat history
try:
    with open("conversation.json", "r") as f:
        content = f.read().strip()
        if content:
            messages = json.loads(content)
        else:
            raise ValueError("Empty file")
except (FileNotFoundError, ValueError, json.JSONDecodeError):
    messages = [{"role": "system", "content": "You are a kind and understanding therapist who listens deeply."}]

# Function to call Ollama and get response
def ask_aya():
    user_input = user_entry.get()
    if not user_input.strip():
        return

    messages.append({"role": "user", "content": user_input})
    prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])

    response_box.insert(tk.END, f"\nYou: {user_input}\n")
    user_entry.delete(0, tk.END)

    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        if res.status_code == 200:
            reply = res.json()["response"]
            messages.append({"role": "assistant", "content": reply})
            response_box.insert(tk.END, f"AYA: {reply}\n")
        else:
            response_box.insert(tk.END, f"Error: {res.text}\n")
    except Exception as e:
        response_box.insert(tk.END, f"Connection error: {e}\n")

    # Save conversation
    with open("conversation.json", "w") as f:
        json.dump(messages, f, indent=2)

# ---------------- GUI SETUP ----------------

window = tk.Tk()
window.title("AYA - Your Local Therapist Assistant")

response_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20)
response_box.pack(padx=10, pady=10)

user_entry = tk.Entry(window, width=50)
user_entry.pack(padx=10, pady=(0, 10))

send_button = tk.Button(window, text="Send", command=ask_aya)
send_button.pack(pady=(0, 10))

window.mainloop()