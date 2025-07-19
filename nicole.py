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
# This is a speech-to-text program in Python that will \
# take certain voice commands and run appropriate actions \
# based on those commands.

# Import needed libraries.
import os
#import pyttsx3
import speech_recognition as sr

# Initialize SpeechRecognition and PyTTSx3.
listener = sr.Recognizer()
#speaker = pyttsx3.init()

# Configure PyTTSx3 settings.
#speech_rate = speaker.setProperty('rate', 115)
#speech_volume = speaker.setProperty('volume', 0.75)
#speech_language = speaker.getProperty('voices')
#speech_voice = speaker.setProperty('voice', speech_language[24].id)
#speaker.say("Good afternoon Derek!")
#speaker.runAndWait()

##########################
### MUSIC PLAYER CLASS ###
##########################

# Create class for controlling Strawberry music player. 
class Music:
    def playMusic(self):
        '''Opens the Strawberry music player and starts playing music.'''
        return os.system('strawberry --quiet -p &')

    def stopMusic(self):
        '''Stops music from playing on Strawberry music player.'''
        return os.system('strawberry --quiet -s &')

    def volumeUp(self):
        '''Turn volume up on the Strawberry music player.'''
        return os.system('strawberry --quiet --volume-up &')

    def volumeDown(self):
        '''Turn volume down on the Strawberry music player.'''
        return os.system('strawberry --quiet --volume-down &')

# Initialize the Music class.
music = Music()

#####################
### WEATHER CLASS ###
#####################

# Create class for getting relevant weather information for the day.
class Weather:
    def currentWeather(self):
        '''Get basic current weather information.'''
        ### NEED TO STILL WORK ON THIS ###
        return os.system('curl wttr.in/?format="%l+%t"')

    def forecastWeather(self):
        '''Get the weather forecast in a PNG image and have it open up for presentation.'''
        os.system('wget wttr.in/Mooresville.png')
        os.system('xdg-open ./Mooresville.png')

# Initialize the Weather class.
weather = Weather()

####################
### MAIN PROGRAM ###
####################

listening = True
while listening:
    # Configure a microphone to be used as a source.
    with sr.Microphone() as source:
        print("Hello!  What can I do for you?")
        # At this point, speak into the microphone.
        # Store what is spoken into a variable.
        received_audio = listener.listen(source)
        transcribed_audio = listener.recognize_google(received_audio)
        print("Text: "+listener.recognize_google(received_audio))
        if transcribed_audio == 'play music':
            try:
                music.playMusic() 
            except:
                print("I did not understand.")
        elif transcribed_audio == 'stop music':
            try:
                music.stopMusic()
            except:
                print("I did not understand.")
        elif transcribed_audio == 'music volume up':
            try:
                music.volumeUp()
            except:
                print("I did not understand.")
        elif transcribed_audio == 'music volume down':
            try:
                music.volumeDown()
            except:
                print("I did not understand.")

        elif transcribed_audio == 'current weather':
            try:
                weather.currentWeather()
            except:
                print("I did not understand.")
        elif transcribed_audio == 'forecast':
            try:
                weather.forecastWeather()
            except:
                print("I did not understand.")
        else:
            print("I do not understand.")
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
