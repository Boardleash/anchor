#!/usr/bin/env python3

###################
### DESCRIPTION ###
###################
#
# This is a secondary Python scriipt to hold the agenda function.
# This is a test; should be imported into alt-maris.py.

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

#######################
### AGENDA FUNCTION ###
#######################

def Agenda():
    '''Create or read from an agenda file to let the user know their "todos".'''
    with speech_recognition.Microphone() as source:
        listener = speech_recognition.Recognizer()
        audio = listener.listen(source)
        cmd_audio = listener.recognize_google(audio)
        print("FUNCTION TEXT: "+cmd_audio)
        if cmd_audio == 'create agenda':
            try:
                proc1 = subprocess.Popen(["gtts-cli", "Ok; what do you need to get done?"], stdout=subprocess.PIPE)
                proc2 = subprocess.Popen(["play", "-t", "mp3", "-"], stdin=proc1.stdout, stderr=subprocess.PIPE)
                proc2.communicate()
                listening = True
                while listening:
                    agenda_audio = listener.listen(source)
                    todo_audio = listener.recognize_google(agenda_audio)
                    with open("temp.tmp", "a") as file:
                        file.write(todo_audio+"\n")
                    if todo_audio == "all done":
                        file.close()
                        proc1 = subprocess.Popen(["gtts-cli", "Your agenda has been created."], stdout=subprocess.PIPE)
                        proc2 = subprocess.Popen(["play", "-t", "mp3", "-"], stdin=proc1.stdout, stderr=subprocess.PIPE)
                        proc2.communicate()
                        listening = False
                        phrasetoremove = "all done"
                        with open("temp.tmp", "r") as file_in, open("agenda", "w") as file_out:
                            tasks = file_in.readlines()
                            updated_tasks = [task.replace(phrasetoremove, "") for task in tasks]
                            file_out.writelines(updated_tasks)
                            file_in.close()
                            file_out.close()
                            subprocess.Popen(["rm", "temp.tmp"])
                return quit()
            except speech_recognition.UnknownValueError:
                Misunderstanding()
        elif cmd_audio == 'what is my agenda':
            try:
                proc1 = subprocess.Popen(["gtts-cli", "-f", "agenda"],
                        stdout=subprocess.PIPE)
                proc2 = subprocess.Popen(["play", "-t", "mp3", "-"],
                        stdin=proc1.stdout, stderr=subprocess.PIPE)
                proc2.communicate()
                return quit()
            except speech_recognition.UnknownValueError:
                Misunderstanding()

# EOF

# Want to add ability to add or delete items to the agenda file
# That's on the 'todo'list
