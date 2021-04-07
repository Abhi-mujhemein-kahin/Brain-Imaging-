from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors #Import import libraries from PsychoPy to setup experiment
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER) #Import important constants

import numpy as np  # whole numpy lib is available
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
from psychopy.hardware import keyboard #import keyboard library

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2' #version of PsychoPy being used
expName = 'dictator game'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'Gender': ''} #Stores information about participant, session number and gender
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName) 
if dlg.OK == False:
    core.quit()  # If user presses cancel, experiment window will terminate
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add extensions like .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler helps to keep track of multiple loops within the file.
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\abhin\\OneDrive\\Desktop\\Dictator game\\dictator game.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # If Esc is pressed, experiment will be quit
frameTolerance = 0.001  # how close to onset before 'same' frame

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so use the standard.
    
#--Initialize all the components for the experiment
# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Welcome to the Dictator game! Imagine that you have Rs 1000 with you, and you have the ability to give any part of this money to another player who is a part of the experiment. Any allocation made by you cannot be rejected or turned down by the other participants in the experiment. You can choose to keep or give away all of the money allocated to you. Please note that your total residual endowment will consist of whatever money is left after the decision you make. Press SPACE to continue or ESC to exit the game.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='lightgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='The screen will display the name or number of the participant. A slider will be displayed which will contain denominations of 100 that can be given to the other participants of the study. You have to select the option which is consistent with the amount you want to allocate. Press SPACE if you want to continue to the game, or press ESC if you want to end the experiment. Press Space after every trial to move on to the next participant. It is assumed that you will have Rs 1000 for every new participant shown on the screen. The name of the participants will be visible to your for these trials.',
    font='Arial',
    units='norm', pos=(0, 0.3), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Trial1"
Trial1Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0.0, 
    color='lightblue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
slider = visual.Slider(win=win, name='slider',
    size=(0.8, 0.5 ), pos=(0, -0.3), units='norm',
    labels=(0,100,200,300,400,500,600,700,800,900,1000), ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), granularity=1.0,
    style='slider', styleTweaks=('triangleMarker',), opacity=1.0,
    color='Darkblue', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.07,
    flip=True, depth=-2, readOnly=False)

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='The screen will display the name or number of the participant. A slider will be displayed which will contain denominations of 100 that can be given to the other participants of the study. You have to select the option which is consistent with the amount you want to allocate. Press SPACE if you want to continue to the game, or press ESC if you want to end the experiment. Press Space after every trial to move on to the next participant. It is assumed that you will have Rs 1000 for every new participant shown on the screen. The name of the participants will be visible to your for these trials.',
    font='Arial',
    units='norm', pos=(0, 0.3), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Please_wait"
Please_waitClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Please Wait',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Trial2"
Trial2Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0.0, 
    color='lightblue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
slider_2 = visual.Slider(win=win, name='slider_2',
    size=(0.8, 0.5), pos=(0, -0.3), units='norm',
    labels=(0,100,200,300,400,500,600,700,800,900,1000), ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), granularity=1.0,
    style='slider', styleTweaks=('triangleMarker',), opacity=1.0,
    color='Darkblue', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.05,
    flip=True, depth=-2, readOnly=False)

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='THANKS FOR YOUR PARTICIPATION!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


