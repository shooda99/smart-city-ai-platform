import vertexai
from vertexai.generative_models import GenerativeModel
PROJECT_ID = "natural-region-435917-r8"
LOCATION = "us-central1"
vertexai.init(
   project=PROJECT_ID,
   location=LOCATION
)
model = GenerativeModel("gemini-2.5-flash")

TABLE_SCHEMA = """
Table:
natural-region-435917-r8.smart_city.accidents
Columns:
year
police_station
zone
fir_no
accident_date
accident_time
place_of_occurrence
road_name
vehicle_at_fault
victim
accident_type
persons_injured
persons_killed
total_persons
accident_timestamp
accident_id
severity
"""

def generate_sql(question):
   prompt = f"""
You are an expert Google BigQuery SQL generator.
Generate ONLY a valid BigQuery SQL query.
Rules:
1. Output ONLY SQL.
2. No explanation.
3. No markdown.
4. No ```sql blocks.
5. Use only this table:
`natural-region-435917-r8.smart_city.accidents`
Schema:
{TABLE_SCHEMA}
Examples:
Question:
Total accidents
SQL:
SELECT COUNT(*) AS total_accidents
FROM `natural-region-435917-r8.smart_city.accidents`;
Question:
Top 10 police stations
SQL:
SELECT
police_station,
COUNT(*) AS accidents
FROM `natural-region-435917-r8.smart_city.accidents`
GROUP BY police_station
ORDER BY accidents DESC
LIMIT 10;
Question:
Total persons killed
SQL:
SELECT SUM(persons_killed) AS total_killed
FROM `natural-region-435917-r8.smart_city.accidents`;
Question:
Most dangerous zone
SQL:
SELECT
zone,
COUNT(*) AS accidents
FROM `natural-region-435917-r8.smart_city.accidents`
GROUP BY zone
ORDER BY accidents DESC
LIMIT 1;
Now generate SQL for:
{question}
"""
   response = model.generate_content(prompt)
   sql = response.text.strip()
   sql = sql.replace("```sql", "")
   sql = sql.replace("```", "")
   return sql