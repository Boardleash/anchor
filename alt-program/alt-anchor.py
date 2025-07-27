#!/usr/bin/env python3

##################################
### TITLE: alt-anchor.py       ###
### AUTHOR: Boardleash (Derek) ###
### DATE: Monday, July 21 2025 ###
##################################
#
###################
### DESCRIPTION ###
###################
#
# This is an alternate Python script to the anchor.py.
# This is to test out importing separate funciton scripts \
# in order to determine if the code would look cleaner with \
# with separate calls vice storing all functions inside of \
# the main script.  Kinda just playing around...

#########################
### REQUIRED INSTALLS ###
#########################
#
# The followinig will need to be installed:
#   --> pip install pyttsx3 
#   --> pip install sounddevice
#   --> pip install SpeechRecognition 
#   --> pip install vosk

# Import needed libraries
import json
import pyttsx3
import re
import sounddevice
import speech_recognition
import vosk
from vosk import SetLogLevel

# Import locally created, but external functions
import agenda
import desktop
import music
import weather

# Initialize SpeechRecognition and PyTTSx3.
listener = speech_recognition.Recognizer()
speaker = pyttsx3.init()

########################
### PYTTSX3 SETTINGS ###
########################

speech_rate = speaker.setProperty('rate', 150)
speech_volume = speaker.setProperty('volume', 0.50)
speech_language = speaker.getProperty('voices')
speech_voice = speaker.setProperty('voice', speech_language[23].id)

###################################
### SPEECH RECOGNITION SETTINGS ###
###################################

# Speech Recognition Dynamic Ambient Noise Setting (True or False)
#listener.dynamic_energy_threshold = True
# Speech Recognition Dynamic Ambient Noise Adjustment (Shouldn't need to modify)
#listener.dynamic_energy_adjustment_damping = 0.15
# Speech Recognition Minimum Length of Silence (seconds) \
# Smaller values = faster recognition, but will cut off slower speech
#listener.pause_threshold = 0.8
# Speech Recognition API Methods
# listener.recognize_google
# listener.recognize_vosk (works offline)

####################
### MAIN PROGRAM ###
####################

# Suppress log output from VOSK
SetLogLevel(-1)

listening = True
while listening:
  with speech_recognition.Microphone() as source:
    audio = listener.listen(source)
    rcvd_audio = listener.recognize_vosk(audio)
    print(rcvd_audio)
    if re.findall("anchor", rcvd_audio):
        try:
            agenda.Agenda() or \
            desktop.setupDesktop() or \
            music.Music() or \
            weather.Weather()
        except speech_recognition.UnknownValueError:
           speaker.say("I don't understand.")
           speaker.runAndWait()
    else:
        speaker.say("I apologize, but I don't understand.")
        speaker.runAndWait()
        listening = False

# EOF
