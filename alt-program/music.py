#!/usr/bin/env python3

###################
### DESCRIPTION ###
###################
#
# This is a secondary Python script to hold the music player \
# function.  This is a test; should be imported into siren.py.

# Import necessary libraries
import os
import speech_recognition

######################
### MUSIC FUNCTION ###
######################

def Music():
    '''Control the onboard music player.'''
    with speech_recognition.Microphone() as source:
        listener = speech_recognition.Recognizer()
        audio = listener.listen(source)
        cmd_audio = listener.recognize_google(audio)
        print("FUNCTION TEXT "+cmd_audio)
        if cmd_audio == 'play music':
          try:
            os.system('gtts-cli "Playing music now..." | play -t mp3 -')
            os.system('strawberry --quiet -p &')
          except speech_recognition.UnknownValueError:
            os.system('gtts-cli "I do not understand." | play -t mp3 -')
        elif cmd_audio == 'stop music':
          try:
            os.system('gtts-cli "Stopping music now..." | play -t mp3 -')
            os.system('strawberry --quiet -s &')
          except speech_recognition.UnknownValueError:
            os.system('gtts-cli "I do not understand." | play -t mp3 -')
        elif cmd_audio == 'volume up':
          try:
            os.system('strawberry --quiet --volume-up &')
          except speech_recognition.UnknownValueError:
            os.system('gtts-cli "I do not understand." | play -t mp3 -')
        elif cmd_audio == 'volume down':
          try:
            os.system('strawberry --quiet --volume-down &')
          except speech_recognition.UnknownValueError:
            os.system('gtts-cli "I do not understand." | play -t mp3 -')

# EOF
