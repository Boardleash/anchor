#!/usr/bin/env python3

###################
### DESCRIPTION ###
###################
#
# This is a secondary Python scriipt to hold the Weather \
# function.  This is a test; should be imported into alt-maris.py.

# Import necessary libraries
import requests
import speech_recognition
import subprocess

#################################
### MISUNDERSTANDING FUNCTION ###
#################################

def Misunderstanding():
    '''Tell user that the speech was not recognizable.'''
    proc1 = subprocess.Popen(["gtts-cli", "I do not understand."],
            stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(["play", "-t", "mp3", "-"],
            stdin=proc1.stdout, stderr=subprocess.PIPE)
    proc2.communicate()

########################
### WEATHER FUNCTION ###
########################

def Weather():
    '''Provide weather information to user.'''
    with speech_recognition.Microphone() as source:
        listener = speech_recognition.Recognizer()
        audio = listener.listen(source)
        cmd_audio = listener.recognize_google(audio)
        print("FUNCTION TEXT: "+cmd_audio)
        if cmd_audio == 'current weather':
          try:
            current_weather = requests.get('https://wttr.in/?format=3')
            proc1 = subprocess.Popen(["gtts-cli", current_weather.text],
                    stdout=subprocess.PIPE)
            proc2 = subprocess.Popen(["play", "-t", "mp3", "-"],
                    stdin=proc1.stdout, stderr=subprocess.PIPE)
            proc2.communicate()
            return quit()
          except speech_recognition.UnknownValueError:
            Misunderstanding()
        elif cmd_audio == 'weather forecast':
          try:
            weather_forecast = requests.get('https://wttr.in/Mooresville.png')
            with open("./Mooresville.png", 'wb') as forecast:
                forecast.write(weather_forecast.content)
                forecast.close()
            subprocess.Popen(["xdg-open", "Mooresville.png"])
            proc1 = subprocess.Popen(["gtts-cli", "Your weather forecast for the week is on your desktop.  The file will be removed in 30 seconds."],
                    stdout=subprocess.PIPE)
            proc2 = subprocess.Popen(["play", "-t", "mp3", "-"],
                    stdin=proc1.stdout, stderr=subprocess.PIPE)
            proc2.communicate()
            return quit()
          except speech_recognition.UnknownValueError:
            Misunderstanding()

# EOF
