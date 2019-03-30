# PIP INSTALLING REQUIRED
# pip install pywin32 pypiwin32 pyttsx3
import os
import sys
import pyttsx3

engine = pyttsx3.init()
engine.say('hello world ')
engine.runAndWait()