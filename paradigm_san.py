from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
import pandas as pd
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
from psychopy.hardware import keyboard
import pyttsx3

# read trial details from csv and print the zeroth coutdown number
trial_order_list=pd.read_csv("trial_orders.csv")
print(trial_order_list.COUNTDOWN_NUMBER[0])


# initialize all parameters of the experiment
frame_refresh_rate = 60.0
beep_sound_duration = 0.5

#number_of_trials = 5
number_of_trials = trial_order_list.COUNTDOWN_NUMBER.size # number of trials initialization
speech_engine = pyttsx3.init() #initializing the speech engine
trial_duration = 30.0 #trial duration in seconds

###"""SETTINGS FOR RATE< VOLUME and VOICE of the speech engine"""###

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

speech_engine.say("Welcome to the Glorius fMRI Experiment")
speech_engine.runAndWait()


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'trial'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/spark/Documents/RHUL_Workspace/Scott_Nick_Ayan_Paradigm/trial_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

frameTolerance = 0.001  # how close to onset before 'same' frame

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / frame_refresh_rate  # could not measure, so go with hardcoded value


# total experiment time in sec

experiment_time = trial_duration * number_of_trials
trial_frames = trial_duration / frameDur
experiment_frames = experiment_time / frameDur
trialTimer = core.CountdownTimer()








# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()



trial_counter=-1

Instructions = visual.TextStim(win=win, ori=0, name='Next_Scan_Ready',
  text=u'Waiting for Scanner',    font='Arial',
  units='deg', pos=[0, 0],alignHoriz='center',height=1,  wrapWidth=18, bold=True,
  color='white', colorSpace='rgb', opacity=1)
Instructions.draw()
win.flip()


Status = visual.TextStim(win=win, ori=0, name='Within trial status',
  text=u'',    font='Arial',
  units='deg', pos=[0, 0],alignHoriz='center',height=1,  wrapWidth=18, bold=True,
  color='Green', colorSpace='rgb', opacity=1)



#wait for trigger and sychronize
event.waitKeys(maxWait=6400, keyList=['5'], timeStamped=True)
logging.flush()


Status.setText("Trigger Received, Baseline Recording")
Status.setColor("Green")
Status.setAutoDraw(True)
win.flip()
core.wait(10)



while trial_counter < number_of_trials-1:

    trial_counter = trial_counter+1
    print ("We are in trial number ", trial_counter)
    beep_sound = sound.Sound('400', secs=beep_sound_duration, stereo=True, hamming=True, name='beep_sound')
    beep_sound.setVolume(1.0)
    beep_sound.play()
    core.wait(1)
    current_frame_number = 0
    print(str(trial_order_list.COUNTDOWN_NUMBER[trial_counter]))
    speech_engine.say(str(trial_order_list.COUNTDOWN_NUMBER[trial_counter]))
    speech_engine.runAndWait()
    trialTimer.add(trial_duration)
    
    
    Status.setText("In Trial "+str(trial_counter+1))
    Status.setColor("Green")
    Status.setAutoDraw(True)
    win.flip()

    # -------Run Routine "trial"-------
    while trialTimer.getTime() > 0:
    

        current_frame_number = current_frame_number + 1 
        win.flip()
        
        if defaultKeyboard.getKeys(keyList=["6"]):
            Status.setText("Button Pressed, Trial Started")
            win.flip()
            
        if defaultKeyboard.getKeys(keyList=["7"]):
            Status.setText("Button Pressed, Trial Ended.\nWaiting 5 Sec")
            Status.setColor("Red")
            win.flip()
            core.wait(5)
            break
        
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()





win.close()
core.quit()







#    # get current time
#    t = trialClock.getTime()
#    tThisFlip = win.getFutureFlipTime(clock=trialClock)
#    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
#    current_frame_number = current_frame_number + 1  # number of completed frames (so 0 is the first frame)
#    # update/draw components on each frame
#    # start/stop beep_sound
#    if beep_sound.status == NOT_STARTED and t >= 0.0-frameTolerance:
#        # keep track of start time/frame for later
#        beep_sound.current_frame_numberStart = current_frame_number  # exact frame index
#        beep_sound.tStart = t  # local t and not account for scr refresh
#        beep_sound.tStartRefresh = tThisFlipGlobal  # on global time
#        beep_sound.play()  # start the sound (it finishes automatically)
#    if beep_sound.status == STARTED:
#        # is it time to stop? (based on global clock, using actual start)
#        if tThisFlipGlobal > beep_sound.tStartRefresh + beep_sound_duration-frameTolerance:
#            # keep track of stop time/frame for later
#            beep_sound.tStop = t  # not accounting for scr refresh
#            beep_sound.current_frame_numberStop = current_frame_number  # exact frame index
#            win.timeOnFlip(beep_sound, 'tStopRefresh')  # time at next scr refresh
#            beep_sound.stop()
#    
#    # check for quit (typically the Esc key)
#    if defaultKeyboard.getKeys(keyList=["escape"]):
#        core.quit()
#    
#    # check if all components have finished
#    if not continueTrial:  # a component has requested a forced-end of Routine
#        break
#    continueTrial = False  # will revert to True if at least one component still running

#    # refresh the screen
#    if continueTrial:  # don't flip if this routine is over or we'll get a blank screen
#        win.flip()










## Flip one final time so any remaining win.callOnFlip() 
## and win.timeOnFlip() tasks get executed before quitting


## these shouldn't be strictly necessary (should auto-save)
#thisExp.saveAsWideText(filename+'.csv', delim='auto')
#thisExp.saveAsPickle(filename)
#logging.flush()
## make sure everything is closed down
#thisExp.abort()  # or data files will save again on exit
#win.close()
#core.quit()







speech_engine.stop()
