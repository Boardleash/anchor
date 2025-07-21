#!/usr/bin/env python3

###################
### DESCRIPTION ###
###################
#
# This is a secondary Python scriipt to hold the agenda function.
# This is a test; should be imported into siren.py.

# Import necessary libraries
import os
import speech_recognition

#######################
### AGENDA FUNCTION ###
#######################

def Agenda():
    '''Create or read from an agenda file to let the user know their "todos".'''
    if rcvd_audio == 'siren':
      with speech_recognition.Microphone() as source:
        audio = listener.listen(source)
        cmd_audio = listener.recognize_google(audio)
        if cmd_audio == 'create agenda':
          try:
            os.system('gtts-cli "Ok; what do you need to get done?" | play -t mp3 -')
            agenda_audio = listener.listen(source)
            todo_audio = listener.recognize_google(agenda_audio)
            with open("agenda", "w") as file:
              file.write(todo_audio.get_raw_data())
              file.close
            os.system('gtts-cli "Agenda has been created." | play -t mp3 -')
          except:
            misunderstanding()
        elif cmd_audio == 'what is my agenda':
          try:
            os.system('gtts-cli -f agenda | play -t mp3 -')
          except:
            misunderstanding()
        else:
          misunderstanding()

# Want to add ability to add or delete items to the agenda file
# That's on the 'todo'list
