#!/usr/bin/env python3

##################################
### TITLE: nicole.py           ###
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
    os.system('strawberry --quiet -p &')

def stopMusic():
    '''Stops music from playing on Strawberry music player.'''
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
    os.system('curl wttr.in/?format="%l+%t"')

def forecastWeather():
    '''Get the weather forecast in a PNG image and have it open up for presentation.'''
    os.system('wget wttr.in/Mooresville.png')
    os.system('xdg-open ./Mooresville.png')

##############################
### DESKTOP SETUP FUNCTION ###
##############################

### NEEDS WORKED ON ###
def setupDesktop():
    '''Open typical applications that I use'''
    keyboard.press_and_release('ctrl+shift+n')
    keyboard.write('brave-browser')
    keyboard.press_and_release('enter')

####################
### MAIN PROGRAM ###
####################

unsure = "I do not understand."
listening = True
while listening:
    # Configure a microphone to be used as a source.
    with speech_recognition.Microphone() as source:
        # At this point, speak into the microphone.
        # Store what is spoken into a variable.
        received_audio = listener.listen(source)
        # Use Google to transcribe the received audio.
        transcribed_audio = listener.recognize_google(received_audio)
        # The below print call is a check to verify it got the right message.
        print("Text: "+listener.recognize_google(received_audio))
        # Conditional statements based on key phrases.
        if transcribed_audio == 'Nicole play music':
            try:
                playMusic() 
            except:
                print(unsure)
        elif transcribed_audio == 'Nicole stop music':
            try:
                stopMusic()
            except:
                print(unsure)
        elif transcribed_audio == 'Nicole volume up':
            try:
                volumeUp()
            except:
                print(unsure)
        elif transcribed_audio == 'Nicole volume down':
            try:
                volumeDown()
            except:
                print(unsure)

        elif transcribed_audio == 'Nicole current weather':
            try:
                currentWeather()
            except:
                print(unsure)
        elif transcribed_audio == 'Nicole forecast':
            try:
                forecastWeather()
            except:
                print(unsure)
        elif transcribed_audio == 'Nicole set up':
            try:
                setupDesktop()
            except:
                print(unsure)
        else:
            print(unsure)
            listening = False

# EOF

###################
### PARKING LOT ###
###################
#
# Need to incorporate the text to speech library so that the print calls
# are read out, vice printed
#
# Need to add conditional statements that perform actions based on what was received
# Need to fine tune to only have the program recognize 'nicole' and then other key words
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
