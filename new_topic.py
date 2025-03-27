from dotenv import load_dotenv
import os
import llm

load_dotenv()

gemini_api_key = os.getenv("gemini_api_key")

llm.getNewTopic(gemini_api_key)
