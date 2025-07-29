# Anchor

I wanted to work on a program that utilizes text-to-speech and speech-to-text features in Python.  This project is the outcome of that, although, there is still plenty to fine tune on it for sure.  The intent with this is to have your computer (laptop or desktop) take voice commands and perform certain functions based on those commands.

This is a work-in-progress and is still being ironed out, but is fun nonetheless.  I learned some interesting things when it comes to voice control through an OS.  Hopefully someone else can explore/have the same kind of experience that I had :smiley:.

This program consists of four major functions:
- **Agenda**
    - Create an agenda
    - Read the created agenda
- **Desktop Setup**
    - Open Brave Browser (assuming installed)
    - Open terminal session (Linux) or VSCode (Windows)
- **Music**
    - Open music player
    - Stop currently playing music (Strawberry on Linux)
    - Increase volume by 4% (Strawberry on Linux)
    - Decrease volume by 4% (Strawberry on Linux)
    - Skip to next song (Strawberry on Linux)
    - Close music player (Strawberry on Linux)
- **Weather**
    - Get current weather conditions
    - Get a three day weather forecast presented via PNG file

## Pre-Requisites

This program uses Python, which will need to be installed/available on your machine.  In addition to that, there are several modules that need to be installed/available on your machine.  You can install necessary Python libraries with the below commands:

>- pip install pyttsx3
>- pip install sounddevice
>- pip install SpeechRecognition
>- pip install vosk

**PyTTSx3** is a text-to-speech library for Python that is capable of running in an offline environment.  More information on this is located here:

[PyTTSx3](https://pypi.org/project/pyttsx3/)

**Sounddevice** is a library in Python for 'portaudio' bindings.  The only reason this is being imported at the moment is because it prevents the ALSA messages on my Linux machines from being thrown.  As of yet, this does not appear to be an issue on Windows.  More information on sounddevice library is located here:

[SoundDevice](https://pypi.org/project/sounddevice/)

**SpeechRecognition** is Python's speech-to-text-library.  There are several option that can be used with the SpeechRecognition library.  More information on this library is located here:

[SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

**VOSK** is a speech recognizer that I decided to implement and can work offline, provided you download the model.  I have downloaded the English model (small) and placed it in this working directory for use.  Guidance and addition information on VOSK is located here:

[VOSK](https://alphacephei.com/vosk/)

## Caveats

This program has been tested on my local machines and VMs.  I have annotated the Python versions and OS versions that were tested (though, the OS versions shouldn't really matter when using Python).  Strawberry is the music player that I use on Linux, and, therefore, is the one called in this program.  The intent is to call programs that are native to the host system's OS.  It is worth noting that I need to include command functions for those native programs.

Windows has been a little bit more difficult to work with for this prgoram.  The subprocess library has been extremely smooth with Linux, however, with Windows, there have been some unique issues, even with the speech_recognition library (compared to Linux).  That said, some of the items on my list of "todos" include a lot of trying to correct this.  My "todos" are stored in this GitHub repo as a file named "tasks" for those that may be interested.

## How to Use 

There is one primary script called **anchor.py** that can be downloaded and ran.  The current set of voice commands that can be provided are broken down in the following tree (phrases in Italics are what should be spoken when running the program):
- **Agenda Voice Commands**:
    - *anchor agenda create*
        - create an agenda; will continuously listen until the word "COMPLETE" is spoken
    - *anchor agenda read*
        - reads the agenda that was created back to the user

- **Desktop Voice Commands**:
    - *anchor desktop*
        - opens a Brave browser session and terminal session on Linux; opens Brave browser session and VSCode on Windows

- **Music Voice Commands**:
    - *anchor music play*
        - opens the native media player on Windows; opens Strawberry (Linux)
    - *anchor music stop*
        - stops currently playing music on Strawberry media player (Linux)
    - *anchor volume up*
        - increases the Strawberry media player volume by 4% (Linux)
    - *anchor volume down*
        - decreases the Strawberry media player volume by 4% (Linux)
    - *anchor next*
        - skips to next song on Strawberry media player (Linux)
    - *anchor close*
        - closes Strawberry media player (Linux)

- **Weather Voice Commands**:
    - *anchor current weather*
        - reads out current weather conditions, with data pulled from wttr.in
    - *anchor weather forecast*
        - pulls a PNG file from wttr.in that consists of three days worth of weather forecast and opens it on the desktop
