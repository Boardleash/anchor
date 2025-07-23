#!/usr/bin/env python3

###################
### DESCRIPTION ###
###################
#
# This is a secondary Python script to hold the Desktop \
# setup function.  This is a test; should be imported into \
# alt-maris.py.

# Import necessary libraries
import speech_recognition
import subprocess

#################################
### MISUNDERSTANDING FUNCTION ###
#################################

def Misunderstaning():
    '''Tell user that speech was not recognizable.'''
    proc1 = subprocess.Popen(["gtts-cli", "I do not understand."],
            stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(["play", "-t", "mp3", "-"),
            stdin=proc1.stdout, stderr=subprocess.PIPE)
    proc2.communicate()

##############################
### DESKTOP SETUP FUNCTION ###
##############################

def setupDesktop():
    '''Open typical applications that I use on the Desktop.'''
    with speech_recognition.Microphone() as source:
        listener = speech_recognition.Recognizer()
        audio = listener.listen(source)
        cmd_audio = listener.recognize_google(audio)
        print("FUNCTION TEXT: "+cmd_audio)
        if cmd_audio == 'set up':
          try:
            proc1 = subprocess.Popen(["gtts-cli", "Setting up your desktop..."],
                    stdout=subprocess.PIPE)
            proc2 = subprocess.Popen(["play", "-t", "mp3", "-"),
                    stdin=proc1.stdout, stderr=subprocess.PIPE)
            proc2.communicate()
            subprocess.Popen(["ptyxis", "-s"])
            subprocess.call(["brave-browser"])
          except speech_recognition.UnknownValueError:
            Misunderstanding()
# EOF
