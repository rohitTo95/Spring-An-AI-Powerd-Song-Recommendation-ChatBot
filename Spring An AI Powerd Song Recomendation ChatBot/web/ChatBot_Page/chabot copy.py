import openai
import re
import webbrowser
import json
from youtube_search import YoutubeSearch
import os
import eel


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
    api_key = data['api_key']  
    
     
openai.api_key = api_key

user_message_list = []
response_message_list = []

def check_song_is_extracted(is_song_extracted, songs):
  if is_song_extracted:
        # Prompt the user to enter the serial number of the song
        selected_serial_number = eel.prompt()()
        # selected_serial_number = input("Enter the serial number of the song to play (or press Enter to skip): ")
        if selected_serial_number:
            selected_song_index = int(selected_serial_number) - 1
            if 0 <= selected_song_index < len(songs):
                selected_song, selected_artist = songs[selected_song_index]
                res = f"Playing: {selected_song} - By {selected_artist}"
                play_youtube_video(selected_song)
                return res
            else:
                return "Invalid serial number."
            
            
def song_extractor(response):
    tmp_song_list = []
    # Extract song names and artist names using regex
    song_pattern = r'\d+\.\s+"([^"]+)"\s+-\s+By\s+(.*)'
    songs = re.findall(song_pattern, response)
    is_song_extracted = False

    # Check if there are any songs extracted
    if songs:
        is_song_extracted = True
        # Print the extracted song names and artist names
        for i, (song, artist) in enumerate(songs, start=1):
            print(f"{i}. {song} - By {artist}")
            tmp_song_list.append(f"{i}. {song} - By {artist}")
            
    check_song_is_extracted(is_song_extracted, songs)

    # Print other conversation messages
    conversation = response.split('\n\n')
    for message in conversation:
        if message.startswith('1.'):
            break
        return message.strip()

    



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
        play_youtube_video(video_name)
        return ''
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


@eel.expose
def startChatBot(user_input):
   while True:
     response = chatBot(user_input.lower())
     if response:
        song_extractor(response)

if "__name__" =="__main__":
   eel.init("web")
   eel.start("index.html")