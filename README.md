# Spring-An-AI-Powerd-Song-Recommendation-ChatBot
# Spring ChatBot 🤖🌸

Welcome to Spring, your friendly AI ChatBot! Spring is designed to chat with you on a wide range of topics and even recommend songs. Let's dive into how this works and how you can use it. 🎉

## How it Works

Spring is powered by the OpenAI GPT-3 model and comes with a few handy features:

- **ChatBot Mode**: Engage in a conversation with Spring. Ask questions, seek advice, or just chat for fun.

- **YouTube Video Player**: Spring can play YouTube videos for you. Just ask it to play a song, and it will open the video in your web browser.

- **Voice Assistant Mode**: Activate Spring's voice assistant mode and control it with your voice commands.

## Getting Started

To use Spring, follow these simple steps:

1. **Clone the Repository**: Clone this GitHub repository to your local machine.

   ```bash
   git clone https://github.com/your-username/spring-chatbot.git
   cd spring-chatbot
   
2. **install Dependencies**: Install the required Python packages using 'pip' in a Virtual Enviourment 

   ```bash
   python -m venv venv  # Create a virtual environment 
   venv\Scripts\activate  # Activate the virtual environment (Windows)
   pip install -r requirements.txt  # Install the required packages

3. **Configuration**: Create a config.json file in the project directory with your OpenAI API key and a custom prompt (as specified in the provided example).

   ```bash
   {
    "api_key": "YOUR_OPENAI_API_KEY",
    "prompt": "Your custom prompt here..."
   }

4.  **Run Spring**: Start the chatbot and have fun!

     ```bash

     python chatbot.py

**Usage**

**ChatBot Mode**

    Type your message/question.

    Spring will respond with a thoughtful answer.

**YouTube Video Player**

    To play a song on YouTube, type: /play {Song Name} (e.g., /play Despacito).

**Voice Assistant Mode**

    To activate voice assistant mode, type: /spring assistant mode.

    You can now use voice commands to interact with Spring.

    And to go back to cahtbot mode, say: /spring assistant mode.

Enjoy Chatting with Spring! 🌼

Feel free to explore, chat, and have fun with Spring. If you encounter any issues or have ideas for improvements, please open an issue or contribute to the project.

Happy chatting! 🗨️🎶
