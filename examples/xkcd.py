#!/usr/bin/env python
"""
This example is using the XKCD downloader (https://github.com/1995eaton/xkcd_downloader)
"""
import os
import numpy as np
import scipy.misc
import plusminus
import glob

# Basic example with black theme
class Basic(plusminus.PlusMinus):
    def __init__(self):
        plusminus.PlusMinus.__init__(self)
        self.height = 1200 # window height in px
        self.id, self.image  = self.get_random_image() # initial image
        self.status = None # initial status
        self.leftmsg.emit("XKCD %d" %self.id)
        
    def get_random_image(self):
        os.system('./xkcd_downloader/xkcd_downloader.py --random 1 -d')
        try:
            filename = glob.glob('./*.png')[0]
        except IndexError:
            return self.get_random_image()
        img = scipy.misc.imread(filename)
        os.system('rm *.png')
        if img.ndim == 3:
            img = img[:,:,0]
        return int(filename[2:-4]), np.rot90(np.invert(img).astype(np.float), -1)/255.

    def first(self):
        self.update.emit() # update canvas and other GUI elements        
            
    def next(self):
        self.id, self.image = self.get_random_image() # next image
        self.status = None # next status
        self.leftmsg.emit("XKCD %d" %self.id)
        self.update.emit() # update canvas and other GUI elements

    def prev(self):
        self.id, self.image  = self.get_random_image() # prev image
        self.status = None # prev status
        self.leftmsg.emit("XKCD %d" %self.id)
        self.update.emit() # update canvas and other GUI elements
            
    def plus(self):
        self.status = True # plus status
        # Do Something here....

    def minus(self):
        self.status = False # minus status
        # Do something here....

# Start plusminus GUI with random google image
basic = Basic()
plusminus.opengui(basic, theme='black')

# Remove files
os.system('rm *.png')
os.system('rm *.jpg')
