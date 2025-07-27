#!/usr/bin/env python3

###################
### DESCRIPTION ###
###################
#
# This is a secondary Python scriipt to hold the agenda function.
# This is a test; should be imported into alt-anchor.py.

# Import necessary libraries
import json
import pyttsx3
import re
import speech_recognition
import subprocess
import time
import vosk

# Initialize SppechRecognition adn PyTTSx3.
listener = speech_recognition.Recognizer()
speaker = pyttsx3.init()

########################
### PYTTSX3 SETTINGS ###
########################

#speech_rate = speaker.setProperty('rate', 125)
#speech_volume = speaker.setProperty('volume', 0.75)
#speech_language = speaker.getProperty('voices')
#speech_voice = speaker.setProperty('voice', speech_language[23].id)

#######################
### AGENDA FUNCTION ###
#######################

def Agenda():
    '''Create or read from an agenda file to let the user know their "todos".'''
    with speech_recognition.Microphone() as source:
        audio = listener.listen(source)
        rcvd_audio = listener.recognize_vosk(audio)
        if re.findall("create agenda", rcvd_audio):
            try:
                speaker.say("Ok; what do you need to get done?")
                speaker.runAndWait()
                time.sleep(3)
                listening = True
                while listening:
                    agenda_audio = listener.listen(source)
                    task_audio = listener.recognize_vosk(agenda_audio)
                    audio_to_parse = json.loads(task_audio)
                    parsed_audio = audio_to_parse["text"]
                    with open('temp.tmp', 'a') as temp_file:
                        temp_file.write(parsed_audio+'\n')
                    if re.findall("complete", task_audio):
                        temp_file.close()
                        speaker.say("Your agenda has been created.")
                        speaker.runAndWait()
                        listening = False
                        removal = "complete"
                        with open('temp.tmp', 'r') as temp_in, open('agenda', 'w') as agenda_out:
                            tasks = temp_in.readlines()
                            for task in tasks:
                                scrubbed_tasks = task.replace(removal, "")
                                agenda_out.write(scrubbed_tasks)
                            subprocess.Popen(["rm", "temp.tmp"])
                            temp_in.close()
                            agenda_out.close()
                return quit()
            except speech_recognition.UnknownValueError:
                speaker.say("I do not understand.")
                speaker.runAndWait()
        elif re.findall("what is my agenda", rcvd_audio):
            try:
                with open('agenda', 'r') as agenda:
                    tasks = agenda.readlines()
                    speaker.say(tasks)
                    speaker.runAndWait()
                    agenda.close()
                return quit()
            except speech_recognition.UnknownValueError:
                speaker.say("I do not understand.")
                speaker.runAndWait()

# EOF
