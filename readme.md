# Smart City AI Platform
## Overview
An AI-powered Smart City Dashboard built with Google Cloud Platform.
## Features
- BigQuery accident analytics
- Vertex AI (Gemini)
- Natural language to SQL
- AI-generated answers
- Looker Studio dashboard
- Flask web application
## Tech Stack
- Python
- Flask
- BigQuery
- Vertex AI
- Looker Studio
- HTML/CSS/JavaScript
## Architecture
User
↓
Flask
↓
Vertex AI (Generate SQL)
↓
BigQuery
↓
Vertex AI (Summarize Results)
↓
Response
## Schema
year
police_station
zone
accident_date
place_of_occurrence
road_name
vehicle_at_fault
victim
accident_type
persons_injured
persons_killed
total_persons
severity
## 💬 Example Questions

You can ask the AI assistant natural language questions about the accident dataset. Here are some examples:

### 📊 Overall Statistics
- Total accidents
- Total persons injured
- Total persons killed
- Total FIRs
- Total severe accidents

### 👮 Police Station Analysis
- Which police station has the highest accidents?
- Top 5 police stations by accidents
- How many accidents occurred at Connaught Place police station?
- Show accident count for each police station

### 📍 Zone Analysis
- Which zone has the highest accidents?
- Top 10 accident-prone zones
- How many accidents occurred in South Zone?

### 📅 Year-wise Analysis
- Total accidents in 2023
- Total accidents in 2024
- Show accident trend by year
- Which year had the highest accidents?

### 🛣️ Road Analysis
- Which road has the highest accidents?
- Top 10 accident-prone roads
- How many accidents occurred on Ring Road?

### ⚠️ Severity Analysis
- Accidents by severity
- How many fatal accidents occurred?
- Which severity is most common?

### 👥 Victim Analysis
- Total injured persons
- Total killed persons
- Average persons injured per accident

### 🚗 Vehicle Analysis
- Which vehicle is most at fault?
  
- Top 5 vehicles responsible for accidents

### 🚦 Accident Type Analysis
- Most common accident type
- Top 10 accident types
