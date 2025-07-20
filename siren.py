#!/usr/bin/env python3

##################################
### TITLE: siren.py            ###
### AUTHOR: Boardleash (Derek) ###
### DATE: Friday, July 18 2025 ###
##################################
#
###################
### DESCRIPTION ###
###################
#
# This is a speech program in Python that will \
# take certain voice commands and run appropriate actions \
# based on those commands.
# Required installs:
#   --> pip install keyboard
#   --> pip install pyttsx3 
#   --> pip install SpeechRecognition
#   --> "play" on a Linux system
#   --> pip install gtts-cli (to be used with os.system) Linux


# Import needed libraries.
import keyboard
import os
import pyttsx3
import speech_recognition

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

##############################
### MUSIC PLAYER FUNCTIONS ###
##############################

def playMusic():
    '''Opens the Strawberry music player and starts playing music.'''
    os.system('gtts-cli "Playing music now..." | play -t mp3 -')
    os.system('strawberry --quiet -p &')

def stopMusic():
    '''Stops music from playing on Strawberry music player.'''
    os.system('gtts-cli "Stopping music now..." | play -t mp3 -')
    os.system('strawberry --quiet -s &')

def volumeUp():
    '''Turn volume up on the Strawberry music player.'''
    os.system('strawberry --quiet --volume-up &')

def volumeDown():
    '''Turn volume down on the Strawberry music player.'''
    os.system('strawberry --quiet --volume-down &')

#########################
### WEATHER FUNCTIONS ###
#########################

def currentWeather():
    '''Get basic current weather information.'''
    ### NEED TO STILL WORK ON THIS ###
    os.system('curl wttr.in/?format="%l+%t" > weather')
    os.system('gtts-cli -f weather')

def forecastWeather():
    '''Get the weather forecast in a PNG image and have it open up for presentation.'''
    os.system('wget wttr.in/Mooresville.png')
    os.system('xdg-open ./Mooresville.png')
    os.system('gtts-cli "Your weather forecast for the week is on your desktop" | play -t mp3 -')

##############################
### DESKTOP SETUP FUNCTION ###
##############################

### NEEDS WORKED ON ###
def setupDesktop():
    '''Open typical applications that I use'''
    os.system('gtts-cli "Setting up your desktop..." | play -t mp3 -')
    keyboard.press_and_release('ctrl+shift+n')
    keyboard.write('brave-browser')
    keyboard.press_and_release('enter')

####################
### MAIN PROGRAM ###
####################

def misunderstanding():
    '''Tell user that there is a misunderstanding'''
    os.system('gtts-cli "I do not understand." | play -t mp3 -')

listening = True
while listening:
    # Configure a microphone to be used as a source.
    with speech_recognition.Microphone() as source:
        # At this point, speak into the microphone.
        # Store what is spoken into a variable.
        audio = listener.listen(source)
        # Use Google to transcribe the received audio.
        rcvd_audio = listener.recognize_google(audio)
        # The below print call is a check to verify it got the right message.
        print("Text: "+listener.recognize_google(audio))
        # Conditional statements based on key phrases.
        if rcvd_audio == 'siren play music':
            try:
                playMusic() 
            except:
                misunderstanding()
        elif rcvd_audio == 'siren stop music':
            try:
                stopMusic()
            except:
                misunderstanding()
        elif rcvd_audio == 'siren volume up':
            try:
                volumeUp()
            except:
                misunderstanding()
        elif rcvd_audio == 'siren volume down':
            try:
                volumeDown()
            except:
                misunderstanding()
        elif rcvd_audio == 'siren current weather':
            try:
                currentWeather()
            except:
                misunderstanding()
        elif rcvd_audio == 'siren forecast':
            try:
                forecastWeather()
            except:
                misunderstanding()
        elif rcvd_audio == 'siren set up':
            try:
                setupDesktop()
            except:
                misunderstanding()
        else:
            misunderstanding()
            listening = False

# EOF

###################
### PARKING LOT ###
###################
#
# Find alternatives to gtts-cli, gtts and espeak
#
# Need to fine tune to only have the program recognize 'siren' and then other key words
# Need to silence the output info messages from the audio program on the terminal
# Need to configure a service file to run this at startup (debating whether to always have it running)
# i,e. always listening
#
# Look into a different audio recognition interpreter (google is used in this example; not bad,
# but what else is there?)

#flatpak run org.strawberrymusicplayer.strawberry &
#strawberry -p &
    # Try to display what was spoken, using google in this example
    #try:
    #    print("Text: "+listener.recognize_google(audio_text))
    # Throw and exception if the speech was unrecognizable
    #except:
    #    print("I did not understand.")
