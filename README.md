# Agentic-AI-project

This project demonstrates the implementation of an **Agentic AI system** using the [phi](https://pypi.org/project/phi/) framework.  
The system is designed as a **multi-agent architecture**, where specialized agents collaborate to answer user queries by reasoning, delegating tasks, and using external tools.

---

## 🚀 Key Features

- **Agentic AI Architecture**
  - Agents can reason about the query and decide which specialized agent/tool should be used.
  - Supports delegation between sub-agents for complex queries.

- **Specialized Agents**
  - **Financial Agent** → Handles stock price, analyst recommendations, fundamentals, and company news via Yahoo Finance.
  - **Web Search Agent** → Retrieves general web information with DuckDuckGo and provides sources.
  - **Multi-AI Coordinator Agent** → Dynamically chooses the right agent to handle queries.

- **Tool Augmentation**
  - Yahoo Finance integration for financial data.
  - DuckDuckGo integration for real-time search.

- **Agent Instructions & Behavior**
  - Financial queries → routed to Financial Agent.
  - Non-financial queries → routed to Web Search Agent.
  - Responses are structured with **tables, markdown, and sources**.

- **Security**
  - Uses `.env` file to store API keys securely.
  - `.gitignore` configured to prevent sensitive data leaks.

---

## 🛠️ Tech Stack

- **Language**: Python 3.12  
- **Framework**: Phi (Multi-Agent Framework)  
- **LLM Provider**: Groq (`llama-3.3-70b-versatile`)  
- **Tools**:
  - DuckDuckGo (Web Search)  
  - YFinance (Financial Data & News)  


