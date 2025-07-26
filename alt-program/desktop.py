#!/usr/bin/env python3

###################
### DESCRIPTION ###
###################
#
# This is a secondary Python script to hold the Desktop \
# setup function.  This is a test; should be imported into \
# alt-anchor.py.

# Import necessary libraries
import pyttsx3
import re
import speech_recognition
import subprocess
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

##############################
### DESKTOP SETUP FUNCTION ###
##############################

def setupDesktop():
    '''Open typical applications that I use on the Desktop.'''
    with speech_recognition.Microphone() as source:
        audio = listener.listen(source)
        rcvd_audio = listener.recognize_vosk(audio)
        if re.findall("desktop", rcvd_audio):
            try:
                speaker.say("Setting up your desktop...")
                speaker.runAndWait()
                subprocess.Popen(["ptyxis", "-s"])
                subprocess.call(["brave-browser"])
                return quit()
            except speech_recognition.UnknownValueError:
                speaker.say("I do not understand.")
                speaker.runAndWait()
# EOF
