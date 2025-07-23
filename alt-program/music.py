#!/usr/bin/env python3

###################
### DESCRIPTION ###
###################
#
# This is a secondary Python script to hold the music player \
# function.  This is a test; should be imported into alt-maris.py.

# Import necessary libraries
import speech_recognition
import subprocess

#################################
### MISUNDERSTANDING FUNCTION ###
#################################

def Misunderstanding():
    '''Tell user that the speech was not recognizable.'''
    proc1 = subprocess.Popen(["gtts-cli", "I do not understand."],
            stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(["play", "-t", "mp3", "-"],
            stdin=proc1.stdout, stderr=subprocess.PIPE)
    proc2.communicate()

######################
### MUSIC FUNCTION ###
######################

def Music():
    '''Control the onboard music player.'''
    with speech_recognition.Microphone() as source:
        listener = speech_recognition.Recognizer()
        audio = listener.listen(source)
        cmd_audio = listener.recognize_google(audio)
        print("FUNCTION TEXT: "+cmd_audio)
        if cmd_audio == 'play music':
            try:
                subprocess.Popen(["strawberry", "--quiet", "-p"])
                return quit() 
            except speech_recognition.UnknownValueError:
                Misunderstanding()
        elif cmd_audio == 'stop music':
            try:
                subprocess.Popen(["strawberry", "--quiet", "-s"])
                return quit() 
            except speech_recognition.UnknownValueError:
                Misunderstanding()
        elif cmd_audio == 'volume up':
            try:
                subprocess.Popen(["strawberry", "--quiet", "--volume-up"])
                return quit() 
            except speech_recognition.UnknownValueError:
                Misunderstanding()
        elif cmd_audio == 'volume down':
            try:
                subprocess.Popen(["strawberry", "--quiet", "--volume-down"])
                return quit() 
            except speech_recognition.UnknownValueError:
                Misunderstanding()
        elif cmd_audio == 'next':
            try:
                subprocess.Popen(["strawberry", "--quiet", "-f"])
                return quit()
            except speech_recognition.UnknownValueError:
                Misunderstanding()
        elif cmd_audio == 'close music':
            try:
                proc1 = subprocess.check_output(["pgrep", "--full", "strawberry --quiet -p"], encoding='utf-8').strip()
                proc2 = subprocess.Popen(["kill", "-s", "SIGTERM", proc1])
                return quit()
            except speech_recognition.UnknownValueError:
                Misunderstanding()

# EOF
