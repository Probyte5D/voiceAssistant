# Voice Assistant - Weather, News, and Commands

This is a voice-controlled assistant built in Python that allows you to interact with weather, news, and various other functionalities using speech commands. The assistant utilizes several libraries such as `pyttsx3`, `speech_recognition`, `requests`, `googletrans`, and `tkinter` for a simple graphical user interface (GUI).

### Features:
- **Weather Updates**: Get the current weather of any city by simply asking the assistant.
- **News Headlines**: Get the latest news headlines from TechCrunch, translated into Italian.
- **Voice Interaction**: Speak to the assistant to ask about the time, weather, and more.
- **Custom Commands**: The assistant can perform various tasks such as greeting the user, providing the current time, and more.
  
### Technologies Used:
- **Python**: The main programming language used for the assistant.
- **pyttsx3**: A Python library for text-to-speech conversion, enabling the assistant to speak responses.
- **SpeechRecognition**: Used for speech-to-text conversion, allowing the assistant to understand spoken commands.
- **requests**: Used to make API requests to get real-time data like weather and news.
- **googletrans**: A library to translate news articles into Italian.
- **Tkinter**: A built-in library for creating the GUI for the assistant.

### Setup Instructions:

1. **Clone or Download the Repository**:
   - Clone the repository using: 
     ```
     git clone https://github.com/yourusername/voice-assistant.git
     ```
   - Or, simply download the ZIP file from the repository and extract it.

2. **Install Dependencies**:
   - Install the required Python libraries using `pip`. Open your terminal and run the following commands:
     ```
     pip install pyttsx3
     pip install requests
     pip install speechrecognition
     pip install googletrans==4.0.0-rc1
     pip install python-dotenv
     pip install pyaudio
     ```

3. **Set up API Keys**:
   - This assistant requires two API keys:
     - **Weather API** (from [OpenWeatherMap](https://openweathermap.org/api)).
     - **News API** (from [NewsAPI](https://newsapi.org/)).
   - Create a `.env` file in the project root directory with the following contents:
     ```
     API_KEY=your_weather_api_key
     API_KEY_NEWS=your_news_api_key
     ```

4. **Running the Assistant**:
   - Once all dependencies are installed and API keys are set up, run the assistant:
     ```
     python main.py
     ```

5. **Interacting with the Assistant**:
   - After launching the program, you will see a simple GUI with a button labeled "🎤 Listen".
   - Click the button or use the microphone to speak commands such as:
     - "What’s the weather in [city]?"
     - "What time is it?"
     - "Give me the latest news."
   - The assistant will respond to your commands with both speech and text.

### Example Commands:
- "What’s the weather in Rome?"
- "Give me the latest news."
- "What time is it?"
- "How are you?"
- "Say hello!"

### Notes:
- Ensure that your microphone is properly configured and accessible for the `speech_recognition` library to work correctly.
- The assistant uses `pyttsx3` for speech output. If you experience issues with speech quality or language, check your system’s installed voices and adjust settings in the code as necessary.

### License:
This project is licensed under the MIT License - MIT License

Copyright (c) 2025 [ProByte]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FIT


### Tags:
`Python` `Voice Assistant` `Weather App` `News Reader` `Speech Recognition` `Text-to-Speech` `Tkinter GUI` `OpenWeatherMap API` `NewsAPI` `Speech-to-Text`

