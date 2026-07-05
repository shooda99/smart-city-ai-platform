from google.cloud import bigquery
client = bigquery.Client()

def execute_query(sql):
   query_job = client.query(sql)
   rows = query_job.result()
   result = []
   for row in rows:
       result.append(dict(row))
   return result