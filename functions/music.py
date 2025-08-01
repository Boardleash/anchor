#!/usr/bin/env python3

###################
### DESCRIPTION ###
###################
#
# This is a secondary Python script to hold the music player function.
# Primarily used for testing out the function.
# Tested on:
#   --> Fedora 42 GNOME Shell Python v3.13.5
#   --> Windows 11 PowerShell v7.5.2 Python v3.12.10

# Import necessary libraries
import pyttsx3
import re
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

######################
### MUSIC FUNCTION ###
######################

def Music():
    '''Control the onboard music player.'''
    with speech_recognition.Microphone() as source:
        audio = listener.listen(source)
        rcvd_audio = listener.recognize_vosk(audio)
        if re.findall("play music", rcvd_audio):
            if sys.platform == "linux":
                try:
                    subprocess.Popen(["strawberry", "--quiet", "-p"])
                    return quit() 
                except speech_recognition.UnknownValueError:
                    speaker.say("I don't understand.")
                    speaker.runAndWait()
            elif re.findall("stop music", rcvd_audio):
                try:
                    subprocess.Popen(["strawberry", "--quiet", "-s"])
                    return quit() 
                except speech_recognition.UnknownValueError:
                    speaker.say("I don't understand.")
                    speaker.runAndWait()
            elif re.findall("volume up", rcvd_audio):
                try:
                    subprocess.Popen(["strawberry", "--quiet", "--volume-up"])
                    return quit() 
                except speech_recognition.UnknownValueError:
                    speaker.say("I don't understand.")
                    speaker.runAndWait()
            elif re.findall("volume down", rcvd_audio):
                try:
                    subprocess.Popen(["strawberry", "--quiet", "--volume-down"])
                    return quit() 
                except speech_recognition.UnknownValueError:
                    speaker.say("I don't understand.")
                    speaker.runAndWait()
            elif re.findall("next", rcvd_audio):
                try:
                    subprocess.Popen(["strawberry", "--quiet", "-f"])
                    return quit()
                except speech_recognition.UnknownValueError:
                    speaker.say("I don't understand.")
                    speaker.runAndWait()
            elif re.findall("close music", rcvd_audio):
                try:
                    proc1 = subprocess.check_output(["pgrep", "--full", "strawberry --quiet -p"], encoding='utf-8').strip()
                    subprocess.Popen(["kill", "-s", "SIGTERM", proc1])
                    return quit()
                except speech_recognition.UnknownValueError:
                    speaker.say("I don't understand.")
                    speaker.runAndWait()
        elif sys.platform == "win32":
                try:
                    subprocess.Popen(["powershell.exe", "start-process", "MediaPlayer.exe"])
                except speech_recognition.UnknownValueError:
                    speaker.say("I don't understand.")
                    speaker.runAndWait()
# EOF
