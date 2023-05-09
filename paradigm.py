#from psychopy import sound

#hello = sound.Sound("audio_files/file_example_WAV_1MG.wav")
#hello.play()

import pyttsx3
import random

speech_engine = pyttsx3.init()

#""" RATE"""
#rate = speech_engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
#speech_engine.setProperty('rate', 200)     # setting up new voice rate


#"""VOLUME"""
#volume = speech_engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
#speech_engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

#"""VOICE"""
#voices = speech_engine.getProperty('voices')       #getting details of current voice
##speech_engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#speech_engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

speech_engine.say("0")
#speech_engine.say(str(random.randrange(1, 11)))
#speech_engine.say('My current speaking rate is ' + str(rate))
speech_engine.runAndWait()
speech_engine.stop()
