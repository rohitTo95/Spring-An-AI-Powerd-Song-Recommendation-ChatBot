import os
import json
import pyttsx3
import speech_recognition as sr
import win32com.client
import openai
import pywhatkit

# Import standard library modules
# Import third-party modules
# Import your own modules (if any)

current_file = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file)

# Construct the file path to config.json
config_file_path = os.path.join(current_directory, 'config.json')

# Check if the file exists and handle potential errors
try:
    with open(config_file_path, 'r') as file:
        data = json.load(file)

    # Extract the API key and prompt
    api_key = data['api_key']
    prompt = data['prompt']

except FileNotFoundError:
    print("Config file not found at:", config_file_path)
    api_key = ""
    prompt = ""

except json.JSONDecodeError:
    print("Error decoding JSON in config file.")
    api_key = ""
    prompt = ""

openai.api_key = api_key
user_message_list = []
response_message_list = []


def chatBot(input_of_user):
    user_message_list.append({'role': 'system', 'content': prompt})
    user_message_list.append({'role': 'user', 'content': input_of_user})

    user_query = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=user_message_list
    )

    chat_response = user_query['choices'][0]['message']['content']
    response_message_list.append({'role': 'assistant', 'content': chat_response})
    return chat_response


speaker = win32com.client.Dispatch("SAPI.SpVoice")


def speak(message):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set the index of the desired female voice
    engine.say(message)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 4000  # Adjust this value based on your microphone sensitivity
        audio = r.listen(source, phrase_time_limit=3)  # Set the maximum length of an utterance
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Some Error Occurred: {e}")
        return ""


def start_voice_assistant():
    print('Welcome to ChatBot')
    speak("Hello, I am Spring. How can I help you?")  # Use the modified speak function
    while True:
        print("Listening...")
        query = takeCommand()
        if "play" in query:
            song_name = query.replace("play", "").strip()
            pywhatkit.playonyt(song_name)
            response = f"Playing {song_name} on YouTube. Enjoy!"
        elif "spring chatbot mode" in query.lower():
            break
        else:
            response = chatBot(query)
        print(f"Spring: {response}")
        speak(response)
