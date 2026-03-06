from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyAbXgKcG0vJryMnxdQmTISuJSE4ywRmt-I")

cotinuar = "S"
while continuar.uper()=="S":
    contenido=input("que consulta desweas efectuar")
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=contenido

    )
    print(response.text)
    contiuar =input("desea efectuar otraconsulta ?")
print("fin del programa")
