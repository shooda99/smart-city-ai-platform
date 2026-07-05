import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(
    project="natural-region-435917-r8",
    location="us-central1",
)

model = GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Hello")

print(response.text)