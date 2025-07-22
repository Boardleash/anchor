#!/usr/bin/env python3

###################
### DESCRIPTION ###
###################
#
# This is a secondary Python scriipt to hold the Desktop \
# setup function.  This is a test; should be imported into \
# siren.py.

# Import necessary libraries
import keyboard
import os
import speech_recognition

##############################
### DESKTOP SETUP FUNCTION ###
##############################

def setupDesktop():
    '''Open typical applications that I use on the Desktop.'''
      with speech_recognition.Microphone() as source:
        listener = speech_recognition.Recognizer()
        audio = listener.listen(source)
        cmd_audio = listener.recognize_google(audio)
        print("FUNCTION TEXT "+cmd_audio)
        if cmd_audio == 'set up':
          try:
            os.system('gtts-cli "Setting up your desktop..." | play -t mp3 -')
            keyboard.press_and_release('ctrl+shift+n')
            keyboard.write('brave-browser')
            keyboard.press_and_release('enter')
            os.system('gtts-cli "Desktop setup complete.')
          except speech_recognition.UnknownValueError:
            os.system('gtts-cli "I do not understand." | play -t mp3 -')
        else:
            os.system('gtts-cli "I do not understand." | play -t mp3 -')
# EOF
