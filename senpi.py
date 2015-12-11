#!/usr/bin/env python3

import speech_recognition as sr
import time
import sys
import os

exitvar = 1
recognitionString = "senpi" #Change this string to change the recognition keyword.
recognitionStringLength = len(recognitionString) + 1

def recognize(speech):
    global exitvar
    speech = speech.lower()
    if len(speech) > 7:
        speech = speech[recognitionStringLength:] #Need to make this a bit smarter- this implementation only works if the recognition string is at the beginning. Possibly only check if recognition string is at the beginning?
    else:
        print("Yes?")
        os.system("espeak \"Yes\"")
        return
    print(speech.lower())
    if "stop listening" in speech:  #Where the magic happens. This series of if/elif is where recognized speech is passed off to other programs.
        print("Shutting down.")
        os.system("espeak \"shutting down\"")
        exitvar = 0
        raise SystemExit
    else:
        print("I don't know how to {}".format(speech))
        os.system("espeak \"I don't know how to {}\"".format(speech))

# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        speech = recognizer.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + speech)
        if recognitionString in speech.lower():
            recognize(speech)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening
os.chdir("C:\Program Files (x86)\eSpeak\command_line")

# Loop to ensure continued operation
while exitvar == 1:
    time.sleep(.1)