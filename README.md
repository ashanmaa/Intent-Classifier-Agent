# Intent Classifier Agent

Most people reply with logic when empathy is needed.

This project is built to fix that.

An AI-powered communication assistant that helps users respond appropriately by understanding the intent behind messages.

## 🚀 Live Demo
🔗 https://intent-classifier-agent-790917605301.europe-west1.run.app

## 💡 The Problem

In text conversations, intent is often misread.

This leads to responses that are:
- logically correct  
- but emotionally wrong  

People tend to jump into solutions, even when the other person just needs to be heard.

## ✨ The Solution

This agent analyzes a message and helps you respond the right way.

It:
- Classifies intent into:
  - EMOTIONAL_SUPPORT  
  - NEEDS_SOLUTION  
  - NEUTRAL  
- Generates a natural, human-like reply suggestion  
- Adapts tone and language based on context  

Instead of just generating answers, it helps users communicate better.

## 🧠 Example

**Input**
I feel really overwhelmed lately

**Output**
{
"intent": "EMOTIONAL_SUPPORT",
"confidence": 0.95,
"suggested_response": "hey… I’m here for you, you’re not alone in this"
}

## 🧩 Key Features

- Intent classification (3 categories)
- Confidence scoring (0–1)
- Human-like response suggestion
- Language & tone adaptation
- Real-time API deployment (Cloud Run)

## 🏗️ How It Works

1. User sends a message  
2. Agent processes input via HTTP  
3. Gemini analyzes intent  
4. System classifies the message  
5. A context-aware response is generated  
6. Output is returned in structured JSON  

## ⚙️ Tech Stack

- Python  
- Google ADK  
- Gemini 2.5 Flash  
- Cloud Run  
- Docker  

## 📸 Demo

(Add screenshots here)

## 👤 Author

Nur Muhamad Abdussalam
