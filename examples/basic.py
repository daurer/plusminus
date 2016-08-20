#!/usr/bin/env python
import numpy as np
import plusminus

# Basic example with black theme
class Basic(plusminus.PlusMinus):
    def __init__(self):
        plusminus.PlusMinus.__init__(self)
        self.height = 1200 # window height in px
        self.image  = np.random.random((200,100)) # initial image
        self.status = None # initial status
            
    def next(self):
        self.image = np.random.random((200,100)) # next image
        self.status = None # next status
        self.update.emit() # update canvas and other GUI elements

    def prev(self):
        self.image  = np.random.random((200,100)) # prev image
        self.status = None # prev status
        self.update.emit() # update canvas and other GUI elements
            
    def plus(self):
        self.status = True # plus status

    def minus(self):
        self.status = False # minus status

basic = Basic()
plusminus.opengui(basic, theme='black')
