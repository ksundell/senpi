import time
import os

def hello():
    os.system("espeak \"hello\"")
    time.sleep(0.1)
    os.system("espeak \"my name is senpai\"")
    time.sleep(0.1)
    os.system("espeak \"i am a voice recognition assistant designed for the fort hays state university maker space\"")