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
    if rcvd_audio == 'siren':
      with speech_recognition.Microphone() as source:
        audio = listener.listen(source)
        cmd_audio = listener.recognize_google(audio)
        if cmd_audio == 'set up':
          try:
            os.system('gtts-cli "Setting up your desktop..." | play -t mp3 -')
            keyboard.press_and_release('ctrl+shift+n')
            keyboard.write('brave-browser')
            keyboard.press_and_release('enter')
            os.system('gtts-cli "Desktop setup complete.')
          except:
            misunderstanding()
        else:
          misunderstanding()

# EOF