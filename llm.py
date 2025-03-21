from google import genai

def getSpentWords():
    file = open("used_words.txt", "r")
    return file.read()

def getTodaysWords(provider_api_key:str, setting:str):
    try:
        used_words = getSpentWords()
        print(used_words)
        client = genai.Client(api_key = provider_api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=(
                f"""
                Do not use words \
                {used_words} \
                Respond directly, without rephrasing my query. \
                Generate 3 nouns in russian with english translations that \
                a person would commonly need to refer to items in this setting: {setting} \
                """)
        )
        # save response as yesterdays words
        file = open("used_words.txt", "a")
        file.write(response.text)
        # return response
        return response.text
    except Exception as e:
        print(e)
        return "Unfortunately, an issue occurred generating your words today."