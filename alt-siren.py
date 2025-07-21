#!/usr/bin/env python3

##################################
### TITLE: alt-siren.py        ###
### AUTHOR: Boardleash (Derek) ###
### DATE: Monday, July 21 2025 ###
##################################
#
###################
### DESCRIPTION ###
###################
#
# This is an alternate Python script to the siren.py.
# This is to test out importing separate funciton scripts \
# in order to determine if the code would look cleaner with \
# with separate calls vice storing all functions inside of \
# the main script.  Kinda just playing around...

#########################
### REQUIRED INSTALLS ###
#########################
#
# The followinig will need to be installed:
#   --> pip install keyboard
#   --> pip install pyaudio
#   --> pip install pyttsx3 
#   --> pip install SpeechRecognition 
#   --> pip install gtts-cli (on a Linux host)
#   --> "play" on a Linux host 

# Import needed libraries
import pyttsx3
import speech_recognition

# Import locally created, but external functions
import ./functions/agenda-function.py as agenda
import ./functions/desktop-function.py as desktop
import ./functions/music-function.py as music
import ./functions/weather-function.py as weather

# Initialize SpeechRecognition and PyTTSx3.
listener = speech_recognition.Recognizer()
#speaker = pyttsx3.init()

########################
### PYTTSX3 SETTINGS ###
########################

#speech_rate = speaker.setProperty('rate', 115)
#speech_volume = speaker.setProperty('volume', 0.75)
#speech_language = speaker.getProperty('voices')
#speech_voice = speaker.setProperty('voice', speech_language[24].id)
#speaker.say("Good afternoon Derek!")
#speaker.runAndWait()

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
# listener.recognize_google_cloud
# listener.recognize_wit
# listener.recognize_bing
# listener.recognize_houndify
# listener.recognize_ibm
# listener.recognize_vosk (works offline)
# listener.recognize_whisper (works offline)
# listener.recognize_faster_whisper
# listener.recognize_openai
# listener.recognize_groq

########################
### MISUNDERSTANDING ###
########################

def Misunderstanding():
  '''If the listener does not understand, let the user know with this function.'''
  os.system('gtts-cli "I do not understand." | play -t mp3 -')

####################
### MAIN PROGRAM ###
####################

listening = True
while listening:
  with speech_recognition.Microphone() as source:
    audio = listener.listen(source)
    rcvd_audio = listener.recognize_google(audio)
    print("TEXT: "+listener.recognize_google(audio))
    if rcvd_audio == 'siren':

# EOF

# Need to determine if I should hold the trigger word for the mic to \
# listen to within each function script or in this main script.