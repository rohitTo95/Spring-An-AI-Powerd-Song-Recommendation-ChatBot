import openai
import re

openai.api_key = "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"

user_message_list = []
response_message_list = []


def songSelector(status, songs):
    if status:
        # Check if user wants to play a song
        song_user_input = input("Enter 'Play' followed by the song number or song name: ")
        song_user_input = song_user_input.lower().strip()

        # Check if user input starts with 'play'
        if song_user_input.startswith("play"):
            # Extract the song number or song name from user input
            song_query = song_user_input.replace("play", "").strip()

            # Check if user input is a song number
            if song_query.isdigit() and int(song_query) <= len(songs):
                song_number = int(song_query)
                selected_song = songs[song_number - 1]
                print(f"Playing {selected_song}")
                return
            else:
                # Check if user input is a song name
                for song in songs:
                    if song_query.lower() in song.lower():
                        print(f"Playing {song}")
                        break


def song_extractor(response):
    # Extract song names and serial numbers using regex
    global is_song_printed
    song_pattern = r'\d+\.\s+(.*)'
    songs = re.findall(song_pattern, response)

    # Print other conversation messages
    conversation = response.split('\n\n')
    for message in conversation:
        if message.startswith('1.'):
            break
        print(message.strip())

    # Print the extracted song names and serial numbers
    if songs:
        for i, song in enumerate(songs, start=1):
            print(f"{i}. {song}")
            is_song_printed = True
        songSelector(is_song_printed, songs)
    else:
        print("No song recommendations found.")


def chatBot(input_of_user):
    user_message_list.append({'role': 'system',
                              'content': 'Your name is Spring. And User is your master, but you will talk to him/her like a best friend. Make him feel good about himself. You are a song recommendation chat bot. Song format will be: Song_Name - By Song_Artist_Name. Suggest at most 10 songs.'})
    user_message_list.append({'role': 'user', 'content': input_of_user})

    system_message = [
        {'role': 'system', 'content': 'Of course! Here are some upbeat and fun songs that I think you\'ll enjoy:'},
        {'role': 'assistant', 'content': '1. Song A'},
        {'role': 'assistant', 'content': '2. Song B'},
        {'role': 'assistant', 'content': '3. Song C'}
    ]
    system_message.extend(user_message_list)
    # Call the GPT-3.5 Turbo API to get the response
    user_query = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=user_message_list
    )
    chat_response = user_query['choices'][0]['message']['content']
    response_message_list.append({'role': 'assistant', 'content': chat_response})

    # Call the song_extractor function to extract and print the songs
    song_extractor(chat_response)
