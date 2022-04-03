# MIA 
Mia is an open source virtual desktop assistant built using Python. 

# Motivation
Mia is built both as a test project to learn AI and Machine Learning elements, and also to create a free and open source alternative to Desktop Assistants.

# Build Status
## v0.1
Currently Implemented Functions:
    Repeat text back to the user|Perform a DuckDuckGo search|Play High Low, a number guessing game

# Code Style
Main functionality is handled by the mia.py file. 

The core directory handles core logic such as the logic behind the bot or the gui.

The functions directory handles various functions like Searching or Playing Games.

# Dependancies
pyttxs3 for text to voice|SpeechRecognition for voice to text|PyAudio is needed for SpeechRecognition to get Mic input

# Installation
Install using the requirements.txt file. 

**NOTE: If PyAudio doesn't install correctly, you may need to use a wheels file for it.**