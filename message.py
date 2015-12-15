import pyaudio
import wave
import os
import speech_recognition as sr

#setup information for recording
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
p = pyaudio.PyAudio()

os.chdir("C:\Program Files (x86)\eSpeak\command_line")

def messageRecord():
    r = sr.Recognizer()
    while True:
        os.system("espeak \"record message for who\"")
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            person = r.recognize_google(audio)
            break
        except sr.UnknownValueError:
            os.system("espeak \"not recognized, try again\"")
        except sr.RequestError:
            os.system("espeak \"google speech recognition offline\"")
            return()
    if "never" in person:
        os.system("espeak \"backing out\"")
        return()
    while True:
        os.system("espeak \"should i record a message for {}\"".format(person))
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            response = r.recognize_google(audio)
        except sr.UnknownValueError:
            os.system("espeak \"not recognized, try again\"") #There is a crash hiding here. "local variable 'response' referenced before assignment"
        except sr.RequestError:
            os.system("espeak \"google speech recognition offline\"")
            return()
        if "yes" in response:
            break
        elif "no" in response:
            os.system("espeak \"backing out\"")
            return()
        else:
            os.system("espeak \"invalid response\"")
    os.system("espeak \"recording message for {}\"".format(person))
    
messageRecord()