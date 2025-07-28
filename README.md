# Anchor

I wanted to work on a program that utilizes text-to-speech and speech-to-text features in Python.  This project is the outcome of that, although, there is still plenty to fine tune on it for sure.  The intent with this is to have your computer (laptop or desktop) take voice commands and perform certain functions based on those commands.

I had a lot of fun with this and learned some interesting things when it comes to voice control through a system.  Hopefully someone else can explore/have the same kind of experience :).

This program consists of four major functions:
	--> Agenda Creation and Readout
	--> Desktop Setup (opening terminal and Brave in this case for now)
	--> Music Control (playing, stopping, controlling volume and closing)
	--> Weather (current weather and forecasted weather)

# Getting Started

## Prerequisites

This program uses Python, which will need to be installed/available on your machine.  In addition to that, there are several modules that need to be installed/available on your machine.

Python Libraries:

>	--> pip install pyttsx3
>	--> pip install sounddevice
>	--> pip install SpeechRecognition
>	--> pip install vosk

PyTTSx3 is a text-to-speech library for Python that is capable of running in an offline environment.  More information on this is located here:
https://pypi.org/project/pyttsx3/

Sounddevice is a library in Python for 'portaudio' bindings.  The only reason this is being imported at the moment is because it prevents the ALSA messages on my Linux machines from being thrown.  As of yet, this does not appear to be an issue on Windows.  More information on sounddevice library is located here:
https://pypi.org/project/sounddevice/

SpeechRecognition is Python's speech-to-text-library.  There are several option that can be used with the SpeechRecognition library.  More information on this library is located here:
https://pypi.org/project/SpeechRecognition/

VOSK is a speech recognizer that I decided to implement and can work offline, provided you download the model.  I have downloaded the English model (small) and placed it in this working directory for use.  Guidance and addition information on VOSK is located here:
https://alphacephei.com/vosk/

## How to Use 

There is one primary script called "anchor.py" that can either be downloaded or ran.  The current set of voice commands that can be provided are broken down in the following tree:
    --> **Agenda Voice Commands**:

        --> *anchor agenda create*
            - create an agenda; will continuously listen until the word "COMPLETE" is spoken

        --> *anchor agenda read*
            - reads the agenda that was created back to the user

    --> **Desktop Voice Commands**:

        --> *anchor desktop*
            - opens a Brave browser session and terminal session on Linux; opens Brave browser session and VSCode on Windows

    --> **Music Voice Commands**:

        --> *anchor music play*
            - opens the native media player on Windows; opens Strawberry (if installed) on Linux

        --> *anchor music stop*
            - stops currently playing music on Strawberry media player (Linux)

        --> *anchor volume up*
            - increases the Strawberry media player volume by 4% (Linux)

        --> *anchor volume down*
            - decreases the Strawberry media player volume by 4% (Linux)

        --> *anchor next*
            - skips to next song on Strawberry media player (Linux)

        --> *anchor close*
            - closes Strawberry media player (Linux)

    --> **Weather Voice Commands**:

        --> *anchor current weather*
            - reads out current weather conditions, with data pulled from wttr.in

        --> *anchor weather forecast*
            - pulls a PNG file from wttr.in that consists of three days worth of weather forecast and opens it on the desktop

### NOTES

There is
