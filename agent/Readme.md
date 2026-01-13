📌 ServiceHive AI CRM – GenAI Sales Agent
🧠 Overview

ServiceHive AI CRM is a backend GenAI-powered conversational sales agent designed to assist website visitors, answer product-related questions, identify high-intent users, and automatically capture sales leads.

This project focuses on agent logic, intent detection, state management, and retrieval-based responses, similar to how real SaaS sales chatbots work behind the scenes.

❓ Problem Statement

Sales teams often lose potential customers because:

Visitors leave websites without interacting

Manual lead qualification is slow

Sales teams can’t respond instantly to every query

There is a need for an intelligent AI agent that can:

Answer product questions

Identify buying intent

Capture leads automatically

✅ Solution

ServiceHive AI CRM solves this by implementing a stateful conversational AI agent that:

Detects user intent (product query vs sales intent)

Responds with relevant product information

Initiates a lead capture flow for high-intent users

Stores captured leads automatically

🏗️ Architecture / Flow
User Message
   ↓
Intent Detection
   ↓
If Product Query → Retrieve info from product_docs (RAG)
If Sales Intent → Ask name → Ask email → Save lead


The agent maintains conversation state to ensure correct sequencing of user inputs.

✨ Features

🤖 Intent-based conversational agent

🧠 Stateful dialogue handling

📄 Retrieval-Augmented Generation (RAG) using product documents

🧾 Automated lead capture (CSV storage)

🧩 Modular and clean code structure

🛠️ Tech Stack

Language: Python

Architecture: Modular backend agent system

Core Concepts:

Intent Detection

State Management

Tool Execution

Retrieval-Augmented Responses

📂 Project Structure
agent/
├── app.py                 # Main application entry point
├── agent_logic.py         # Core agent decision logic
├── intent.py              # Intent detection logic
├── rag.py                 # Retrieval logic from product docs
├── data/
│   └── product_docs.txt   # Product knowledge base
├── tools/
│   └── lead_capture.py    # Lead capture tool (CSV)
└── leads.csv              # Auto-generated leads file

▶️ How to Run

Navigate to the agent folder:

cd agent


Run the application:

python app.py


Exit anytime using:

exit

🧪 Demo Flow (Recommended Test)
Product Query
User: what features do you have?
Agent: [returns product features from docs]

Sales Intent + Lead Capture
User: pricing
Agent: Sure! May I know your name?

User: Vineet
Agent: Thanks! Please share your email.

User: vineet@gmail.com
Agent: ✅ Your details are saved.


A leads.csv file is automatically created with captured details.

🚀 Future Improvements

Web UI / chat widget integration

Database-based lead storage

LLM-powered semantic retrieval

Deployment as a microservice

🧠 Key Learnings

Building stateful conversational agents

Managing conversation flow correctly

Separating agent logic and tools

Designing explainable GenAI systems

👤 Author

Vineet Singh
B.Tech – Artificial Intelligence & Data Science
Aspiring Data Scientist / AI Engineer