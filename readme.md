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
## Example Questions
- Total accidents
- Top 10 police stations
- Most dangerous zone
- Total persons killed
- Accidents in 2024
- Highest severity accidents
## Run
```bash
pip install -r requirements.txt
python app.py
```
