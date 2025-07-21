#!/usr/bin/env python3

###################
### DESCRIPTION ###
###################
#
# This is a secondary Python scriipt to hold the Weather \
# function.  This is a test; should be imported into siren.py.

# Import necessary libraries
import os
import speech_recognition

########################
### WEATHER FUNCTION ###
########################

def Weather():
    '''Provide weather information to user.'''
    if rcvd_audio == 'siren':
      with speech_recognition.Microphone() as source:
        audio = listener.listen(source)
        cmd_audio = listener.recognize_google(audio)
        if cmd_audio == 'current weather':
          try:
            os.system('curl wttr.in/?format="%l+%t" > weather')
            os.system('gtts-cli -f weather')
            os.system('rm weather')
          except:
            misunderstanding()
        elif cmd_audio == 'weather forecast':
          try:
            os.system('wget wttr.in/Mooresville.png')
            os.system('xdg-open ./Mooresville.png')
            os.system('gtts-cli "Your weather forecast for the week is on your desktop" | play -t mp3 -')
          except:
            misunderstanding()
        else:
          misunderstanding()

# EOF

# Need to look into a different way to tell the user the current weather \
# instead of creating a file and then removing it