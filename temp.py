
def main():
    url = os.getenv("langbase_url")
    api_key = os.getenv("langbase_api_key")
    load_dotenv()
    data = {
        "messages": [{"role":"user", "content": "Hello, this is a test! What is content field for?"}],
        "stream": False,
        "variables": [{"name": "setting","value": "Gas Station"}],
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response.json().get("completion"))
    except Exception as e:
        print(f"Error: {e}")
        return
