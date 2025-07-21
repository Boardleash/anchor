#########################################
### TITLE: speech-to-text-template.py ###
### AUTHOR: Boardleash (Derek)        ###
### DATE: Wednesday, July 9 2025      ###
#########################################
#
###################
### DESCRIPTION ###
###################
#
# This is a base template using Python's speech recognition library
# The variable 'engine' is just an exmaple to store and initilize
# the speech_recognition library; change as necessary

# Import SpeechRecognition library as 'sr'
import speech_recognition as sr

# Initialize the engine
engine = sr.Recognizer()

# Use a microphone as source
with sr.Microphone() as source:
    # Ask the user to speak
    print("Please talk now...")
    # Store the speech into a variable
    audio_text = engine.listen(source)
    # Let the user know that the program is done listening
    print("All out of time.  No longer listening...")

    # Try to display to user what they said, using google in this example
    try:
        print("Text: "+engine.recognize_google(audio_text))
    # Throw an exception if the speech was unrecognizable
    except:
        print("I did not understand.")

# EOF
