# Anchor

I wanted to work on a program that utilizes text-to-speech and speech-to-text features in Python.  This project is the outcome of that, although, there is still plenty to fine tune on it for sure.  The intent with this is to have your computer (laptop or desktop) take voice commands and perform certain functions based on those commands.

At the moment, there are four basic functions that the program will perform.  They revolve around:
	--> Agenda Creation and Readout
	--> Desktop Setup (opening terminal and Brave in this case for now)
	--> Music Control (playing, stopping, controlling volume and closing)
	--> Weather (current weather and forecasted weather)

# Getting Started

## Prerequisites

This program uses Python, which will need to be installed/available on your machine.  In addition to that, there are several modules that need to be installed/available on your machine.

Python Libraries:

	--> pip install pyttsx3
	--> pip install sounddevice
	--> pip install SpeechRecognition
	--> pip install vosk

PyTTSx3 is a text-to-speech library for Python that is capable of running in an offline environment.  More information on this is located here:
https://pypi.org/project/pyttsx3/

Sounddevice is a library in Python for 'portaudio' bindings.  The only reason this is being imported at the moment is because it prevents the ALSA messages on my Linux machines from being thrown.  As of yet, this does not appear to be an issue on Windows.  More information on sounddevice library is located here:
https://pypi.org/project/sounddevice/

SpeechRecognition is Python's speech-to-text-library.  There are several option that can be used with the SpeechRecognition library.  More information on this library is located here:
https://pypi.org/project/SpeechRecognition/

VOSK is a speech recognizer that I decided to implement and can work offline, provided you download the model.  I have downloaded the English model (small) and placed it in this working directory for use.  Guidance and addition information on VOSK is located here:
https://alphacephei.com/vosk/

## Using the Scripts

There is one primary script called "anchor.py" that can either be downloaded or ran.  The current set of voice commands that can be provided are:
	--> Create Agenda
	--> What is my agenda?
	--> Desktop
	--> Play music
	--> Stop music
	--> Volume up
	--> Volume down
	--> Next
	--> Close music
	--> Current weather
	--> weather forecast