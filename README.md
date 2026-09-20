# 🤖 Multi-Agent AI Chatbot

A full-stack AI chatbot that uses an **LLM-based Router Agent** to understand the user's query and automatically route it to the most suitable specialized AI agent.

The chatbot currently supports:

- 💻 Coding Agent
- 💼 Career Agent
- 📄 Resume Agent
- 🌐 General Agent

The application uses **FastAPI** for the backend, **Node.js + HTML/CSS/JavaScript** for the frontend, and **Google Gemini** for AI-powered routing and responses.

---

## ✨ Features

- 🤖 LLM-based intelligent query routing
- 💻 Specialized Coding Agent
- 💼 Specialized Career Agent
- 📄 Specialized Resume Agent
- 🌐 General-purpose AI Agent
- ⚡ FastAPI REST API
- 🟢 Node.js frontend server
- 🧠 Google Gemini integration
- 🔐 Environment variable based API key
- 🌐 CORS configuration
- 💬 Interactive full-screen chatbot dashboard
- ✨ Typing animation
- 📝 AI response formatting
- 💻 Code block rendering
- 🔄 New Chat functionality
- ⚠️ Basic error handling
- 📱 Responsive UI

---

# 🏗️ System Architecture

```text
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │  Node.js        │
                  │  Frontend       │
                  │  Chat Dashboard │
                  └────────┬────────┘
                           │
                           │ HTTP POST /chat
                           ▼
                  ┌─────────────────┐
                  │    FastAPI      │
                  │    Backend      │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   Router Agent  │
                  │  LLM Intent     │
                  │  Classification │
                  └────────┬────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
    ┌───────────┐    ┌───────────┐    ┌───────────┐
    │  Coding   │    │  Career   │    │  Resume   │
    │   Agent   │    │   Agent   │    │   Agent   │
    └─────┬─────┘    └─────┬─────┘    └─────┬─────┘
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   General   │
                    │    Agent    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Google    │
                    │   Gemini    │
                    └──────┬──────┘
                           │
                           ▼
                     AI RESPONSE
                           │
                           ▼
                    NODE.JS FRONTEND