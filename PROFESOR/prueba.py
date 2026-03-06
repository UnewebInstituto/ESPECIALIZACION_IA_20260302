from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.

client = genai.Client(api_key="AIzaSyC7x7a4HCrkI56QbAqF_43VgOqEgJet2Jw")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Dame la ubicación geográfica de Venezuela"
)
print(response.text)