# AYA — Your Local Therapist Assistant 💬🧠

AYA is a desktop-based AI therapist application that runs locally on your system using [Ollama](https://ollama.com/) and models like Mistral. It's built with Python and Tkinter, offering a simple GUI where you can chat with AYA, a kind and understanding therapist.

## ✨ Features

- 🧠 Local AI assistant powered by Mistral via Ollama
- 🖥️ Lightweight and offline desktop app (Python + Tkinter)
- 💬 Friendly and therapeutic chat experience
- 💾 Saves chat history (JSON-based)
- 🔌 No internet or cloud dependency — fully private

## 🚀 How It Works

AYA uses your inputs and responds in a calm, compassionate tone using a local LLM. Your entire chat is stored locally so the app can "remember" your past messages for better context.

## 🛠️ Installation

### 1. Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com/) installed and running
- Mistral model pulled locally:
  ```bash
  ollama pull mistral