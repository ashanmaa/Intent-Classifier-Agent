# Intent-Classifier-Agent
People often misread intent in text conversations, leading to responses that are logically correct but emotionally wrong. This is not just an AI that answers, it helps people communicate better.

# 🧠 Intent Classifier Agent
An AI-powered communication assistant that helps users respond better by understanding intent behind messages.

## 🚀 Live Demo
🔗 https://intent-classifier-agent-790917605301.europe-west1.run.app

## 💡 Problem
People often misread intent in text conversations, leading to responses that are logically correct but emotionally wrong. Most people default to giving solutions, even when emotional support is needed.

## ✨ Solution
This project introduces a Communication Intent Agent that:
- Classifies user messages into:
  - EMOTIONAL_SUPPORT
  - NEEDS_SOLUTION
  - NEUTRAL
- Generates a human-like response suggestion
- Adapts tone and language based on context
Instead of just generating replies, this system helps users respond appropriately.

## 🧩 Features
- Intent classification (3 categories)
- Confidence scoring (0–1)
- Human-like response suggestion
- Language adaptation (auto-detect)
- Tone adaptation (empathetic vs practical vs neutral)
- API-based deployment via Cloud Run

## ⚙️ Tech Stack
- Python
- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash
- Google Cloud Run
- Docker

## 🧠 Example Output

Input: I feel really overwhelmed lately
Output:
{
"intent": "EMOTIONAL_SUPPORT",
"confidence": 0.95,
"suggested_response": "hey… I’m here for you, you’re not alone in this"
}

## 🏗️ Architecture

1. User sends message
2. Agent receives input via HTTP
3. Gemini processes the message
4. Intent is classified
5. Response suggestion is generated
6. Output returned in JSON

## 🚀 Deployment

Using Google ADK CLI:
uvx --from google-adk==1.14.0 \
adk deploy cloud_run \
  --project=$PROJECT_ID \
  --region=europe-west1 \
  --service_name=intent-classifier-agent \
  --with_ui \
  . \
  -- \
  --labels=project=intent-classifier \
  --service-account=$SERVICE_ACCOUNT

## 📸 Demo



## 👤 Author
Nur Muhamad Abdussalam
