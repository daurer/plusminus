"""Colormaps for pyqtgraph image windows"""
import numpy as np
from matplotlib import cm

def cubehelix(gamma=1.0, s=0.5, r=-1.5, h=1.0):
    def get_color_function(p0, p1):
        def color(x):
            xg = x ** gamma
            a = h * xg * (1 - xg) / 2
            phi = 2 * np.pi * (s / 3 + r * x)
            return xg + a * (p0 * np.cos(phi) + p1 * np.sin(phi))
        return color    
    array = np.empty((256, 3))
    abytes = np.arange(0, 1, 1/256.)
    array[:, 0] = get_color_function(-0.14861, 1.78277)(abytes) * 255
    array[:, 1] = get_color_function(-0.29227, -0.90649)(abytes) * 255
    array[:, 2] = get_color_function(1.97294, 0.0)(abytes) * 255
    return array

def rainbow():
    array = np.empty((256, 3))
    abytes = np.arange(0, 1, 0.00390625)
    array[:, 0] = np.abs(2 * abytes - 0.5) * 255
    array[:, 1] = np.sin(abytes * np.pi) * 255
    array[:, 2] = np.cos(abytes * np.pi / 2) * 255
    return array

def hot():
    array = cm.hot(np.arange(256))
    return array[:,:3] * 255

def jet():
    array = cm.jet(np.arange(256))
    return array[:,:3] * 255

def bone(): 
    array = cm.bone(np.arange(256))
    return array[:,:3] * 255

def get_cmap(name):
    return getattr(name)
