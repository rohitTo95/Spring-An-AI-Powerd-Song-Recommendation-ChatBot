import openai
import os
import json
import pywhatkit
import Voice_Assistant  # Correct the import if needed

# Load API key and prompt from config file
current_file = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file)
config_file_path = os.path.join(current_directory, 'config.json')

try:
    with open(config_file_path, 'r') as file:
        data = json.load(file)
        api_key = data.get('api_key', '')
        prompt = data.get('prompt', '')
except FileNotFoundError:
    print("Config file not found at:", config_file_path)
    api_key = ''
    prompt = ''
except json.JSONDecodeError:
    print("Error decoding JSON in config file.")
    api_key = ''
    prompt = ''

openai.api_key = api_key

def chatBot(input_of_user):
    user_message_list = []  # Moved inside the function to reset for each interaction
    response_message_list = []  # Moved inside the function to reset for each interaction

    if input_of_user.startswith("/play "):
        video_name = input_of_user[6:]  # Extract the video name
        pywhatkit.playonyt(video_name)
        return ''
    elif input_of_user.lower() == "/spring assistant mode":
        Voice_Assistant.start_voice_assistant()  # Remove the extra indent
        return "Voice Assistant mode activated. You can now use voice commands."
    else:
        user_message_list.append({'role': 'user', 'content': prompt})
        user_message_list.append({'role': 'user', 'content': input_of_user})
        user_query = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=user_message_list,
            max_tokens=500,
            n=1,
            stop=None,
        )
        chat_response = user_query['choices'][0]['message']['content']
        response_message_list.append({'role': 'assistant', 'content': chat_response})
        return chat_response

print('Welcome To Spring, an AI ChatBot Song Recommender. Ready to chat? (Commands: /Play {Song Name}, /Spring assistant mode)')
while True:
    user_input = input().lower()
    response = chatBot(user_input)
    print(response)
