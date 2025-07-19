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
# This is a speech-to-text program in Python that will
# take certain voice commands and run appropriate actions
# based on those commands.

# Import needed libraries
import os
#import pyttsx3
import speech_recognition as sr

# Initialize SpeechRecognition and PyTTSx3
listener = sr.Recognizer()
#speaker = pyttsx3.init()

# Configure PyTTSx3 settings
#speech_rate = speaker.setProperty('rate', 115)
#speech_volume = speaker.setProperty('volume', 0.75)
#speech_language = speaker.getProperty('voices')
#speech_voice = speaker.setProperty('voice', speech_language[24].id)
#speaker.say("Good afternoon Derek!")
#speaker.runAndWait()

##########################
### MUSIC PLAYER CLASS ###
##########################

# Create class for Music
class Music:
  def openStrawberry(self):
    return os.system('strawberry --quiet &')

  def playMusic(self):
    return os.system('strawberry --quiet -p &')

  def stopMusic(self):
    return os.system('strawberry --quiet -s &')

  def pauseMusic(self):
    return os.system('strawberry --quiet -u &')

  def volumeUp(self):
    return os.system('strawberry --quiet --volume-up &')

  def volumeDown(self):
    return os.system('strawberry --quiet --volume-down &')

# Initialize Music class
music = Music()

# Configure a microphone to be used as a source
with sr.Microphone() as source:
  print("Hello!  What can I do for you?")
  # At this point, speak into the microphone
  # Store what is spoken into a variable
  audio_text = listener.listen(source)
  transcribed_text = listener.recognize_google(audio_text)
  if transcribed_text == 'music':
    # Try to display what was spoken, using google in this example
    try:
        music.playMusic() 
        print("Text: "+listener.recognize_google(audio_text))
    # Throw and exception if the speech was unrecognizable
    except:
        print("I did not understand.")
  elif transcribed_text == 'stop music':
    try:
        music.stopMusic()
        print("Text: "+listener.recognize_google(audio_text))
    except:
        print("I did not understand.")

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
