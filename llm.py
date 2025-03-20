from google import genai

def getTodaysWords(provider_api_key:str, setting:str):
    try:
        client = genai.Client(api_key = provider_api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=("Respond directly, without rephrasing my query. Generate 3 nouns in russian with english translations a person would commonly need to refer to items in this setting: "+setting)
        )
        return response.text
    except Exception as e:
        print(e)
        return "Unfortunately, an issue occurred generating your words today."