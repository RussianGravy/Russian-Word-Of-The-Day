from google import genai

def getSpentWords():
    file = open("used_words.txt", "r")
    return file.read()

def getTodaysWords(provider_api_key:str, setting:str):
    try:
        used_words = getSpentWords()
        client = genai.Client(api_key = provider_api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=(
                f"""
                Without rephrasing my prompt, 
                generate three common Russian nouns with english translations to use at a {setting}.  
                Seperate the words with commas and do not use any of these words: {used_words} 
                """)
        )
        # save response as yesterdays words
        file = open("used_words.txt", "a")
        file.write(response.text)
        # return response
        return response.text.split(", ")
    except Exception as e:
        print(e)
        return "Unfortunately, an issue occurred generating your words today."

def getNewTopic(provider_api_key:str):
    try:
        # get current topic
        curT_file = open("current_topic.txt", "w")
        # get used topics
        usedTs_file = open("used_topics.txt")
        used_topics = usedTs_file.read()
        # prompt ai for new topic
        prompt = f"""
            WIthout rephrasing my prompt generate one commonplace setting that is at most two words. Do not use any of these: {used_topics}. \
        """
        client = genai.Client(api_key = provider_api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=(prompt)
        )
        # update txt files && return new topic
        curT_file.write(response.text)
        usedTs_file = open("used_topics.txt", "a")
        usedTs_file.write(response.text)
        usedWs_file = open("used_words.txt", "w")
        usedWs_file.write("")
        return response.text
    except Exception as e:
        # use last topic in case of exception
        print(e)
        curT_file = open("current_topic.txt")
        return curT_file.read()