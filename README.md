# 🤖 SQLGenAI: Natural Language to SQL with Ollama and LangChain

**SQLGenAI** is an AI-powered interface that translates natural language queries into executable MySQL statements. It uses **LangChain**, **Ollama (TinyLlama)**, and a live **MySQL database** connection to generate precise, machine-readable SQL queries based on user prompts.

---

## 🚀 Features

- ✅ Convert plain English queries into SQL
- ✅ Uses a local Ollama LLM (TinyLlama)
- ✅ Returns **strictly machine-readable JSON**
- ✅ Connects to any MySQL database
- ✅ Designed for use in **AI-driven database assistants**

---

## 🧠 How It Works

1. Connects to your **MySQL database** using LangChain's SQL utilities
2. Loads **TinyLlama** model from **Ollama**
3. Uses `SQLDatabaseChain` to send the prompt and get a structured SQL response
4. Enforces strict output rules for clean JSON parsing
5. Logs query execution time

---
