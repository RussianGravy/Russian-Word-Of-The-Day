from pathlib import Path
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("gemini_api_key")

setting = "Gas Station"

def generateNewWords(api_key:str, setting:str):
    with open("words.txt", "r+") as file:
        prompt = f"""Without including the prompt in your response, please generate thirty Russian nouns in cyrillic script with their english translations in parenthesis and each on its own line. The nouns should be loosely related to {setting}, as well."""
        client = genai.Client(api_key = api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=(prompt)
        )
        file.write(response.text)
        print(response.text)
        return response.text

def getTodaysWords():
    path = Path("words.txt")
    with path.open("r+") as file:
        try: 
            words = [file.readline(), file.readline()]
            text = file.read()
            if (len(text) == 0):
                words = ["There was an issue generating your words today"]
            path.write_text(text)
            file.close()
        except Exception as e:
            print(e)
        return words

if __name__ == "__main__":
    generateNewWords(gemini_api_key, setting)