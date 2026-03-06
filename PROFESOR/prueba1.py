from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.

client = genai.Client(api_key="AIzaSyC7x7a4HCrkI56QbAqF_43VgOqEgJet2Jw")

continuar = "S" 
while continuar.upper() == "S":
    contenido = input("¿Qué consulta deseas efectuar?:")
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=contenido
    )
    print(response.text)
    continuar = input("¿Desea efectuar otra consulta (S/N)?")
print("Fin del programa...")
