#!/usr/bin/env python3

##################################
### TITLE: anchor.py           ###
### AUTHOR: Boardleash (Derek) ###
### DATE: Friday, July 18 2025 ###
##################################
#
###################
### DESCRIPTION ###
###################
#
# This is a speech program in Python that will take certain \
# voice commands and run appropriate actions based on those commands.
# Tested on:
#   --> Fedora 42 GNOME Shell Python v3.13.5
#   --> Windows 11 PowerShell v7.5.2 Python v3.12.10

# Required installs:
#   --> pip install pyttsx3
#   --> pip install sounddevice
#   --> pip install SpeechRecognition
#   --> pip install vosk

# Import needed libraries.
import json
import pyttsx3
import re
import requests
import sounddevice
import speech_recognition
import subprocess
import sys
import time
import vosk
from PIL import Image
from vosk import SetLogLevel

# Initialize SpeechRecognition and PyTTSx3.
listener = speech_recognition.Recognizer()
speaker = pyttsx3.init()

########################
### PYTTSX3 SETTINGS ###
########################

speech_rate = speaker.setProperty('rate', 125)
speech_volume = speaker.setProperty('volume', 0.75)
speech_language = speaker.getProperty('voices')
speech_voice = speaker.setProperty('voice', speech_language[23].id)

########################
### AGENDA FUNCTIONS ###
########################

def createAgenda():
    '''Create an agenda file with a task list.'''
    speaker.say("Ok, what do you need to get done?")
    speaker.runAndWait()
    if sys.platform == "linux":
        time.sleep(3)
    else:
        pass
    listening = True
    while listening:
        with speech_recognition.Microphone() as source:
            agenda_audio = listener.listen(source)
            task_audio = listener.recognize_vosk(agenda_audio)
            audio_to_parse = json.loads(task_audio)
            parsed_audio = audio_to_parse["text"]
            if re.findall("complete", task_audio):
                temp_file.close()
                listening = False
                removal = "complete"
                with open('temp.tmp', 'r') as temp_in, open('agenda', 'w') as agenda_out:
                    tasks = temp_in.readlines()
                    for task in tasks:
                        scrubbed_tasks = task.replace(removal, "")
                        agenda_out.write(scrubbed_tasks)
                temp_in.close()
                agenda_out.close()
                if sys.platform == "linux":
                    subprocess.Popen(["rm", "./temp.tmp"])
                elif sys.platform == "win32":
                    subprocess.Popen(["powershell.exe", "rm", "./temp.tmp"])
                speaker.say("Your agenda has been created.")
                speaker.runAndWait()
                return quit()
            else:
                with open('temp.tmp', 'a') as temp_file:
                    temp_file.write(parsed_audio+'\n')

def readAgenda():
    '''Read the agenda that a user created.'''
    with open('agenda', 'r') as agenda:
        tasks = agenda.readlines()
        speaker.say(tasks)
        speaker.runAndWait()
        agenda.close()
    return quit()

##############################
### DESKTOP SETUP FUNCTION ###
##############################

def Desktop():
    '''Open typical applications that I use on the Desktop.'''
    speaker.say("Setting up your desktop...")
    speaker.runAndWait()
    if sys.platform == "linux":
        subprocess.Popen(["ptyxis", "-s"])
        subprocess.call(["brave-browser"])
    elif sys.platform == "win32":
        subprocess.Popen(["powershell.exe", "-command", "code"])
        brave_path = Path('"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"')
        subprocess.Popen(["powershell.exe","start-process", brave_path])
    return quit()

##############################
### MUSIC PLAYER FUNCTIONS ###
##############################

def playMusic():
    '''Open the native music player.'''
    if sys.platform == "linux":
        subprocess.Popen(["strawberry", "--quiet", "-p"])
        return quit() 
    elif sys.platform == "win32":
        subprocess.Popen(["powershell.exe", "start-process", "MediaPlayer.exe"])

def stopMusic():
    '''Stop any music that may be playing.'''
    subprocess.Popen(["strawberry", "--quiet", "-s"])
    return quit() 

def upVolume():
    '''Adjust music volume in an upward direction.'''
    subprocess.Popen(["strawberry", "--quiet", "--volume-up"])
    return quit() 

def downVolume():
    '''Adjust music volume in a downward direction.'''
    subprocess.Popen(["strawberry", "--quiet", "--volume-down"])
    return quit() 

def nextSong():
    '''Skip to next song.'''
    subprocess.Popen(["strawberry", "--quiet", "-f"])
    return quit()

def closeMusic():
    '''Close the music player.'''
    proc1 = subprocess.check_output(["pgrep", "--full", "strawberry --quiet -p"], encoding='utf-8').strip()
    subprocess.Popen(["kill", "-s", "SIGTERM", proc1])
    return quit()

#########################
### WEATHER FUNCTIONS ###
#########################

def currentWeather():
    '''Provide current weather information to user.'''
    current_weather = requests.get('https://wttr.in/?format=3')
    speaker.say(current_weather.text)
    speaker.runAndWait()
    return quit()

def forecastWeather():
    '''Provide 3 day weather forecast displayed on desktop.'''
    weather_forecast = requests.get('https://wttr.in/Mooresville.png')
    with open("Mooresville.png", 'wb') as forecast:
        forecast.write(weather_forecast.content)
        forecast.close()
    if sys.platform == "linux":
      subprocess.Popen(["xdg-open", "Mooresville.png"])
    elif sys.platform == "win32":
      forecast_image = Image.open('Mooresville.png')
      forecast_image.show()
    speaker.say("Your weather forecast for the next three days is on your desktop.")
    speaker.runAndWait()
    return quit()

#####################
### MAIN FUNCTION ###
#####################

def Main():
    # Suppress log output from VOSK.
    SetLogLevel(-1)

    # Set condition for while loop.
    listening = True

    while listening:
        with speech_recognition.Microphone() as source:
            audio = listener.listen(source)
            rcvd_audio = listener.recognize_vosk(audio)
            print(rcvd_audio)
            if re.findall("anchor agenda create", rcvd_audio):
                createAgenda()
            elif re.findall("anchor agenda read", rcvd_audio):
                readAgenda()
            elif re.findall("anchor desktop", rcvd_audio):
                Desktop()
            elif re.findall("anchor music play", rcvd_audio):
                playMusic()
            elif re.findall("anchor music stop", rcvd_audio):
                stopMusic()
            elif re.findall("anchor volume up", rcvd_audio):
                upVolume()
            elif re.findall("anchor volume down", rcvd_audio):
                downVolume()
            elif re.findall("anchor next", rcvd_audio):
                nextSong()
            elif re.findall("anchor close", rcvd_audio):
                closeMusic()
            elif re.findall("anchor current weather", rcvd_audio):
                currentWeather()
            elif re.findall("anchor weather forecast", rcvd_audio):
                forecastWeather()
            else:
                speaker.say("I apologize, but I don't understand.")
                speaker.runAndWait()
                listening = False

# Execute the script.
Main()

# EOF
