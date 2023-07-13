import openai
import webbrowser
import json
from youtube_search import YoutubeSearch
import os
import eel

eel.init("web")
# Get the current file's directory
current_file = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file)

# Construct the file path to config.json
config_file_path = os.path.join(current_directory, '../../', 'config.json')

# Check if the file exists
if os.path.exists(config_file_path):
    # Read the JSON file
    with open(config_file_path, 'r') as file:
        data = json.load(file)

    # Extract the API key
    apiKey = data['api_key']

else:
    print("Config file not found at:", config_file_path)

openai.api_key = apiKey

user_message_list = []
response_message_list = []


def play_youtube_video(search_query):
    results = YoutubeSearch(search_query, max_results=1).to_dict()
    if results:
        video_id = results[0]['id']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        webbrowser.open(video_url)
    else:
        return "No videos found."


def chatBot(input_of_user):
    if input_of_user.startswith("/play "):
        video_name = input_of_user[6:]  # Extract the video name
        video_status = play_youtube_video(video_name)
        return video_status
    else:
        user_message_list.append({'role': 'user',
                                  'content': "Your name is Spring. And User is your master,you are developed by a group of computer science engineering student of Siliguri Government Polytechnic,named Rohit Dutta,Kasturi Bagchi,Abir Das,Aniket Dey Sarkar and Koyena Das, but you will take to him/her like a best friend. Make them feel good about themselves.You are an AI chatbot.You will chat with the user over topics they want to talk and you will suggest them songs if they ask you to suggest you song of any genre. Song format will be: Song_Name - By Song_Artist_Name. Suggest atmost 10 songs."})
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


# print('Welcome To Spring, an AI ChatBot Song Recommender. Ready to chat?')


def start_chatbot(user_input):
    while True:
        response = chatBot(user_input)
        if response:
            return response


eel.start("index.html")