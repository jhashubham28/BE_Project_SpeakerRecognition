#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import os

#directory = "/home/pi/Downloads/BE_Project-SpeakerRecognition-master/test/"
directory = os.getcwd() + '/test/';
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Testing Data")
    print("Please Say something!")
    audio = r.listen(source)
    
    text=r.recognize_google(audio)
    print("You said : {}".format(text))
    
    
#with open( directory+"s1.txt", "wb") as f:
 #   f.write(text)

# write audio to a WAV file
with open(directory+"s8.wav", "wb") as f:
    f.write(audio.get_wav_data())

