#!/usr/bin/env python3

###################
### DESCRIPTION ###
###################
#
# This is a secondary Python scriipt to hold the Weather function.
# Primarily used for testing out the function.
# Tested on:
#   --> Fedora 42 GNOME Shell Python v3.13.5
#   --> Windows 11 PowerShell v7.5.2 Python v3.12.10

# Import necessary libraries
from PIL import Image
import pyttsx3
import re
import requests
import speech_recognition
import subprocess
import sys
import vosk

# Initialize SpeechRecognition and PyTTSx3.
listener = speech_recognition.Recognizer()
speaker = pyttsx3.init()

########################
### PYTTSX3 SETTINGS ###
########################

#speech_rate = speaker.setProperty('rate', 150)
#speech_volume = speaker.setProperty('volume', 0.50)
#speech_language = speaker.getProperty('voices')
#speech_voice = speaker.setProperty('voice', speech_language[23].id)

########################
### WEATHER FUNCTION ###
########################

def Weather():
    '''Provide weather information to user.'''
    with speech_recognition.Microphone() as source:
        audio = listener.listen(source)
        rcvd_audio = listener.recognize_vosk(audio)
        if re.findall("current weather", rcvd_audio):
          try:
            current_weather = requests.get('https://wttr.in/?format=3')
            speaker.say(current_weather.text)
            speaker.runAndWait()
            return quit()
          except speech_recognition.UnknownValueError:
            speaker.say("I don't understand.")
            speaker.runAndWait()
        elif re.findall("weather forecast", rcvd_audio):
          try:
            weather_forecast = requests.get('https://wttr.in/Mooresville.png')
            with open("Mooresville.png", 'wb') as forecast:
                forecast.write(weather_forecast.content)
                forecast.close()
            if sys.platform == "linux":
              subprocess.Popen(["xdg-open", "Mooresville.png"])
            elif sys.platform == "win32":
              forecast_image = Image.open('Mooresville.png')
              forecast_image.show()
            speaker.say("Your weather forecast for the week is on your desktop.")
            speaker.runAndWait()
            return quit()
          except speech_recognition.UnknownValueError:
            speaker.say("I don't understand.")
            speaker.runAndWait()

# EOF
