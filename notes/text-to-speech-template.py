#########################################
### TITLE: text-to-speech-template.py ###
### AUTHOR: Boardleash (Derek)        ###
### DATE: Thursday, July 10 2025      ###
#########################################
#
###################
### DESCRIPTION ###
###################
#
# This is a base template using Python's text-to-speech library
# The variable "engine" is just an example; change as necessary

# Import the text-to-speech library
import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Set speaking rate and get current rate (unchanged)
#rate = engine.getProperty('rate')
#print(f"Current speaking rate: {rate}")

# Set new speaking rate (200 is max)
#engine.setProperty('rate', 125) # Example

# Get current volume level
#volume = engine.getProperty('volume')
#print(f"Current volume level: {volume}")

# Set new volume level (1.0 is max)
#engine.setProperty('volume', 0.5) # Example

# Get list of available voices
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)

# Select a voice
#engine.setProperty('voice', voices[<index number of voice id].id)

# Add text to be spoken
#engine.say("Good morning")

# Run the speech engine
#engine.runAndWait()

# Save the speech to an audio file
#engine.save_to_file("Good morning", "test.mp3")

# EOF
